import os
# Number of region examples: 113-all Russia, 1-Moscow, 2-St.Petersburg, 3-Ekaterinburg, 88-Kazan
AREA_NUMBER = 113
JOB_TITLE = ['Data Scientist']
# Maximum period - 30 days!
TIME_PERIOD = 30
HH_API_URL = 'https://api.hh.ru/vacancies'
CONFIGURATION_FILE_NAME: str = 'logging_configuration.json'
LOGGER_CONFIGURATION_PATH = r'%s' % os.path.abspath(os.path.join(os.getcwd(),
                                                                 CONFIGURATION_FILE_NAME)).replace('\\', '/')
# Data paths
DATA_PATH = r'%s' % os.path.abspath(os.path.join(os.getcwd(), 'data')).replace('\\', '/')
DS_DATA_FILE = r'%s' % os.path.abspath(os.path.join(DATA_PATH, 'Data_Scientist_113.csv')).replace('\\', '/')
DA_DATA_FILE = r'%s' % os.path.abspath(os.path.join(DATA_PATH, 'Аналитик_данных_113.csv')).replace('\\', '/')
# Columns names
ANALYZE_COLUMNS_NAMES = ['employer', 'area', 'name', 'salary', 'experience',
                         'schedule', 'description', 'key_skills', 'published_at']
DATE_COLUMNS = ['published_at']
