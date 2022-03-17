import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
import json

url = "https://imunizacao-es.saude.gov.br/_search"

payload = json.dumps({
  "size": 10000
})
headers = {
  'Authorization': 'Basic aW11bml6YWNhb19wdWJsaWM6cWx0bzV0JjdyX0ArI1Rsc3RpZ2k=',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# status da requisição
print(response)

# json para DF
vacina = response.json()
vacina['hits']['hits']
df_vacina = pd.json_normalize(vacina['hits']['hits'])
print(df_vacina)

# Página 1
# POST https://imunizacao-es.saude.gov.br/_search?scroll=1m
# { "size": 10000 }
# Página 2,3,4...
# POST https://imunizacao-es.saude.gov.br/_search/scroll
# { "scroll": "1m", "scroll_id": "scroll id da página anterior" }
