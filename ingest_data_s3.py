#
## Script python utilizado para efetuar upload do arquivo MICRODADOS_ENEM_2017.csv para um Bucket S3 do AWS
#

import boto3
import pandas as pd
import os
import io
import requests
import zipfile
import wget
import urllib3

urllib3.disable_warnings()

## Baixa o arquivo zip, descompacta e salva em pasta local no computador
URL = 'https://storage.googleapis.com/kaggle-data-sets/527761/967534/compressed/3.DADOS/MICRODADOS_ENADE_2017.txt.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20220616%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220616T200300Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=2e0615d1e3b98e640e71d5b48dae948a14e88f96e8124520a81abc1d71004f91c568a1630e5919782108a80d9e44dd1cf2db5861f53dc8d52c9e2c29b7439ad529935133b7397f07a2944c6abf71a3a30ab040a1f53d4c2032691366be64c5345c0a385a0384f848d83d56dca2ed6be0404d9510157fcfbef4bde2557a08b90e4ef9d4601253a472dc6eed88af34731c415b3c5183416e701dbdb6b327fbc22a59381f03fd116ba9bee1368d74169ec56142fe5f195165e40a47eefb6c44c342ae49c6ac498843414623dd66370c01598a9c50de786743d9b247ae4769efb0e74245d7a4ee127d9ccae288632c9176e5a8580da3ac011c6dd85eb527adad62c3'

response = requests.get(URL, verify = False, stream = True)

file = zipfile.ZipFile(io.BytesIO(response.content))
path = './data'
os.makedirs(path, exist_ok = True)
file.extractall(path)

os.rename('data/MICRODADOS_ENADE_2017.txt', 'data/MICRODADOS_ENADE_2017.csv') 

# Cria um client para interagir com o AWS S3
s3 = boto3.client('s3')

# Efetua download de um arquivo do AWS S3 para o disco local
# s3.download_file("datalake-jorge-igti-mba-engenharia-dados",
#                  "data/ITENS_PROVA_2020.csv",
#                  "data/ITENS_PROVA_2020.csv")

# csvFile = path + "/DADOS/MICRODADOS_ENEM_2020.csv";
# print (csvFile)

# Le o arquivo csv e mostra em formato de tabela (separador ;)
# df = pd.read_csv(csvFile, encoding='utf8', sep=";")
# print(df)

# Faz upload do arquivo MICRODADOS_ENEM_2020.csv para a pasta raw-data do AWS S3
s3.upload_file("data/MICRODADOS_ENADE_2017.csv",
              "datalake-jorge-igti-tf-producao-431738431676",
              "raw-zone/MICRODADOS_ENADE_2017.csv")
