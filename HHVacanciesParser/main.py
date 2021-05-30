from src.hh_parser import *
import logging
from config.config import AREA_NUMBER, JOB_TITLE, TIME_PERIOD

if __name__ == '__main__':
    # 
    logger = logging.getLogger(__name__)
    # Parse vacancies from hh.ru
    try:    
        vacancies_parser_obj = HHVacanciesParseWithAPI(AREA_NUMBER, TIME_PERIOD)
        if len(JOB_TITLE) >= 1:
            for one_job_name in JOB_TITLE:
                vacancies_parser_obj.collect_vacancies_data_into_list(one_job_name)
                logger.info(f'Processed {one_job_name} vacancy!')
        else:
            logger.info('Nothing vacancies names to parse!')
    except Exception:
        logger.error(f'Exception occurred: ', exc_info=True)
