from src.hh_parser import *
from src.transform_data import *
import logging
from config.config import AREA_NUMBER, JOB_TITLE, TIME_PERIOD, ANALYZE_COLUMNS_NAMES, DS_DATA_FILE

if __name__ == '__main__':
    # 
    logger = logging.getLogger(__name__)
    # Parse vacancies from hh.ru
    try:    
        # vacancies_parser_obj = HHVacanciesParseWithAPI(AREA_NUMBER, TIME_PERIOD)
        # if len(JOB_TITLE) >= 1:
        #     for one_job_name in JOB_TITLE:
        #         vacancies_parser_obj.collect_vacancies_data_into_list(one_job_name)
        #         logger.info(f'Processed {one_job_name} vacancy!')
        # else:
        #     logger.info('Nothing vacancies names to parse!')
        transform_data_obj = TransformDataset(DS_DATA_FILE)
        modify_frame = transform_data_obj.transform_data()
        print(modify_frame.head())
    except Exception:
        logger.error(f'Exception occurred: ', exc_info=True)
