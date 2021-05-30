import requests
import pandas as pd
import os
import time
import logging
from config.config import AREA_NUMBER, TIME_PERIOD, HH_API_URL, DATA_PATH


class HHVacanciesParseWithAPI:
    def __init__(self, area_number, period=None):
        self.area_number = AREA_NUMBER
        self._url = HH_API_URL
        if period is None:
            self.period = 30
        else:
            self.period = TIME_PERIOD
        self.logger = logging.getLogger(__name__)

    def save_vacancies_data_into_dataframe(self, vacancy_name, vacancies_list):
        vacancy_additional_details = requests.get(vacancies_list[0]['items'][0]['url']).json().keys()
        df = pd.DataFrame(columns=list(vacancy_additional_details))
        ind = 0
        for i in range(len(vacancies_list)):
            for j in range(len(vacancies_list[i]['items'])):
                additional_vacancies_data = requests.get(vacancies_list[i]['items'][j]['url']).json()
                time.sleep(1)
                df.loc[ind] = additional_vacancies_data
                self.logger.info(f'Add info for {ind+1} vacancies into dataframe!')
                ind += 1
        csv_name = f"{vacancy_name.replace(' ', '_')}_{self.area_number}.csv"
        df.to_csv(os.path.join(DATA_PATH, csv_name), index=False)
        self.logger.info(f'Save vacancies in file: {csv_name}')

    def collect_vacancies_data_into_list(self, job_name):
        try:
            vacancies_data_list = []
            common_get_request_params = {'text': job_name, 'area': self.area_number, 'period': self.period}
            vacancies_data = requests.get(self._url, params=common_get_request_params).json()
            vacancies_data_number_of_pages = vacancies_data['pages']
            for one_page in range(int(vacancies_data_number_of_pages)):
                get_request_params = {'text': job_name, 'area': self.area_number,
                                      'period': self.period, 'page': one_page}
                vacancies_data_from_one_page = requests.get(self._url, params=get_request_params).json()
                vacancies_data_list.append(vacancies_data_from_one_page)
                self.logger.info(f'Count of parsed vacancies pages: {one_page + 1}')
                time.sleep(1)
            self.save_vacancies_data_into_dataframe(job_name, vacancies_data_list)
        except Exception:
            self.logger.error(f'Exception occurred: ', exc_info=True)
