#%%
import requests
import json

url = "https://geo.abs.gov.au/arcgis/rest/services/Hosted/CED_2021_cen_sel_var/FeatureServer/0/query?f=json&maxRecordCountFactor=4&orderByFields=objectid&outFields=*&resultType=standard&returnGeometry=false&returnExceededLimitFeatures=true&where=1=1&defaultSR=102100"

r = requests.get(url)

with open("census.json", "w") as f:
    data = r.json()
    f.write(json.dumps(data, indent=4))