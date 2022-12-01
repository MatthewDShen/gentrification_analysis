import pandas as pd
import os




pd.read_csv(os.getcwd()[:-6] + 'analysis/cleaned_features/census_2011.csv', encoding='utf-8')