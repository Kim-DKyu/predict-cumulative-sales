from urllib import response
import requests
import json
from pymongo import MongoClient

API_KEY = '9af8f13836ae7a6a12f5cb144590bb30'

movie_detail = None
for i in range(20221001,20221030,5):
    API_URL = f'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={API_KEY}&targetDt={i}'
    row_data = requests.get(API_URL)
    movie_detail = json.loads(row_data.text)

    HOST = 'cluster1.0feolir.mongodb.net'
    USER = 'kdg'
    PASSWORD = '1234'
    DATABASE_NAME = 'AIB15'
    COLLECTION_NAME = 'Movie_detail'
    MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

    client = MongoClient({MONGO_URI})
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    collection.insert_one(movie_detail)

# for i in collection.find():
#     print(i['boxOfficeResult']['dailyBoxOfficeList'][0])