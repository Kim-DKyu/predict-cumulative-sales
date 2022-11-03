from pymongo import MongoClient
import os
import sqlite3

DB_FILENAME = 'Movie_api.db'
DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)

HOST = 'cluster1.0feolir.mongodb.net'
USER = 'kdg'
PASSWORD = '1234'
DATABASE_NAME = 'AIB15'
COLLECTION_NAME = 'Movie_detail'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

client = MongoClient({MONGO_URI})
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

conn = sqlite3.connect(DB_FILEPATH)
cur = conn.cursor()

for i in collection.find():
    for j in range(0,10,1):
        sql = f"""
            INSERT INTO Movie_api (
                id, movieNm, movieCd, salesAmt, salesShare, salesInten, 
                salesChange, salesAcc, audiCnt, audiInten,
                audiChange, audiAcc, scrnCnt, showCnt
            )
            VALUES (
                {"'"+str(i['_id'])+str(j)+"'"},
                \"{i['boxOfficeResult']['dailyBoxOfficeList'][j]['movieNm']}\",
                {i['boxOfficeResult']['dailyBoxOfficeList'][j]['movieCd']},
                {i['boxOfficeResult']['dailyBoxOfficeList'][j]['salesAmt']},
                {i['boxOfficeResult']['dailyBoxOfficeList'][j]['salesShare']},
                {i['boxOfficeResult']['dailyBoxOfficeList'][j]['salesInten']},
                {i['boxOfficeResult']['dailyBoxOfficeList'][j]['salesChange']},
                {i['boxOfficeResult']['dailyBoxOfficeList'][j]['salesAcc']},
                {i['boxOfficeResult']['dailyBoxOfficeList'][j]['audiCnt']},
                {i['boxOfficeResult']['dailyBoxOfficeList'][j]['audiInten']},
                {i['boxOfficeResult']['dailyBoxOfficeList'][j]['audiChange']},
                {i['boxOfficeResult']['dailyBoxOfficeList'][j]['audiAcc']},
                {i['boxOfficeResult']['dailyBoxOfficeList'][j]['scrnCnt']},
                {i['boxOfficeResult']['dailyBoxOfficeList'][j]['showCnt']}
            ) 
        """
        cur.execute(sql)

conn.commit()
cur.close()
