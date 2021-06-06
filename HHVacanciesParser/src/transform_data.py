import pandas as pd
import numpy as np
import ast
import logging
from config.config import ANALYZE_COLUMNS_NAMES, DATE_COLUMNS


class TransformDataset:
    def __init__(self, filename):
        self.filename = filename
        self.logger = logging.getLogger(__name__)

    def transform_data(self):
        data = pd.read_csv(self.filename, dayfirst=True,
                           parse_dates=DATE_COLUMNS, usecols=ANALYZE_COLUMNS_NAMES)
        data['employer'] = data['employer'].apply(lambda x: ast.literal_eval(x)['name'])
        data['area'] = data['area'].apply(lambda x: ast.literal_eval(x)['name'])
        data['experience'] = data['experience'].apply(lambda x: ast.literal_eval(x)['name'])
        data['schedule'] = data['schedule'].apply(lambda x: ast.literal_eval(x)['name'])
        data['key_skills'] = data['key_skills'].apply(
            lambda x: [v for v_dict in ast.literal_eval(x) for _, v in v_dict.items()])
        data['description'] = data['description'].apply(
            lambda x: x if x is not None and len(x) > 50 else None)
        cut_data = data.replace(to_replace='None', value=np.nan).\
            dropna(subset=['description']).reset_index(drop=True)
        return cut_data
