from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile
import pandas as pd

api = KaggleApi()
api.authenticate()

api.dataset_download_files('samratkumardey/bangladesh-covid19-daily-dataset')
zf = ZipFile('bangladesh-covid19-daily-dataset.zip')
zf.extractall()
zf.close()

data = pd.read_csv('COVID-19 BD Dataset-25 april.csv')
print(data)
