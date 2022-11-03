import sqlite3
import os
from pymongo import MongoClient
from urllib import response
import requests
import json

DB_FILENAME = 'Movie_api.db'
DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)
conn = sqlite3.connect(DB_FILEPATH)
cur = conn.cursor()

#영화코드 중복제거 후 추출
t = cur.execute('select DISTINCT movieCd from Movie_api ma')

dist = []
for i in t:
    dist.append(i[0])

#영화코드 별 영화상세 정보 db추가
API_KEY = '9af8f13836ae7a6a12f5cb144590bb30'

Movie_detail_director= None

for i in dist:
    API_URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={API_KEY}&movieCd={i}'
    row_data = requests.get(API_URL)
    Movie_detail_director = json.loads(row_data.text)

    HOST = 'cluster1.0feolir.mongodb.net'
    USER = 'kdg'
    PASSWORD = '1234'
    DATABASE_NAME = 'AIB15'
    COLLECTION_NAME = 'Movie_detail_director'
    MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

    client = MongoClient({MONGO_URI})
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    collection.insert_one(Movie_detail_director)