import time
import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
import json
from time import sleep
import traceback

url1 = "https://imunizacao-es.saude.gov.br/_search?scroll=1m"
url2 = "https://imunizacao-es.saude.gov.br/_search/scroll"

headers = {
    'Authorization': 'Basic aW11bml6YWNhb19wdWJsaWM6cWx0bzV0JjdyX0ArI1Rsc3RpZ2k=',
    'Content-Type': 'application/json'
}

df_vacina = pd.DataFrame()

chunk_size = 10000

page_number = 0
scroll_id = None

while True:
  start = time.time()
  try:
    print('Fetching page %s' % (page_number))
    vacina = None
    if page_number == 0:
      payload = json.dumps({
          "size": chunk_size
      })
      vacina = requests.request(
          "POST", url1, headers=headers, data=payload).json()
    else:
      payload = json.dumps({
          "scroll": "30m",
          "scroll_id": scroll_id
      })
      vacina = requests.request(
          "POST", url2, headers=headers, data=payload).json()

    scroll_id = vacina['_scroll_id']
    hits = vacina['hits']['hits']
    df_vacina = pd.json_normalize(hits)
    if len(hits) != 0:
      # sleep(3)
      page_number += 1
      # for index, row in df_vacina.iterrows():
      #   uf = row['_source.estabelecimento_uf']
      #   df_vacina.loc[[index]].to_csv(f'datasets/{uf}.csv', mode='a', header=False, index=False, index_label='_id')
    else:
      print('All pages fetched')
      break
  except Exception:
    traceback.print_exc()
    print("An error occurred, trying again in 3s")
    # sleep(3)
    
  end = time.time()
  print(end - start, "seconds")