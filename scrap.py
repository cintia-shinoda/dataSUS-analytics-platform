from time import sleep
import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
import json

url1 = "https://imunizacao-es.saude.gov.br/_search?scroll=1m"
url2 = "https://imunizacao-es.saude.gov.br/_search/scroll"

headers = {
  'Authorization': 'Basic aW11bml6YWNhb19wdWJsaWM6cWx0bzV0JjdyX0ArI1Rsc3RpZ2k=',
  'Content-Type': 'application/json'
}

# df_vacina = pd.json_normalize(vacina['hits']['hits'])

def paginate(scroll_id, page_number):
  try:
    print('Fetching page %s' % (page_number))
    vacina = None

    if page_number == 0:
      payload = json.dumps({
        "size": 10000
      })
      vacina = requests.request("POST", url1, headers=headers, data=payload).json()
    else:
      payload = json.dumps({
        "scroll": "1m",
        "scroll_id": scroll_id
      })
      vacina = requests.request("POST", url2, headers=headers, data=payload).json()

    next_scroll_id = vacina['_scroll_id']
    hits = vacina['hits']['hits']
    if len(hits) != 0:
      sleep(3)
      paginate(next_scroll_id, page_number + 1)
    else:
      print('All pages fetched')
  except:
    print("An occurred, trying again in 3s")
    sleep(3)
    paginate(scroll_id, page_number)

paginate(None, 0)