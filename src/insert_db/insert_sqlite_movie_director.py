from pymongo import MongoClient
import os
import sqlite3

DB_FILENAME = 'Movie_api.db'
DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)

HOST = 'cluster1.0feolir.mongodb.net'
USER = 'kdg'
PASSWORD = '1234'
DATABASE_NAME = 'AIB15'
COLLECTION_NAME = 'Movie_detail_director'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

client = MongoClient({MONGO_URI})
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

conn = sqlite3.connect(DB_FILEPATH)
cur = conn.cursor()

for i in collection.find():
    if (len(i['movieInfoResult']['movieInfo']['actors']) < 2 or len(i['movieInfoResult']['movieInfo']['directors'])<1):
        continue
    elif (len(i['movieInfoResult']['movieInfo']['actors']) < 3):
        sql_1 = f"""
                INSERT INTO Movie_director_api (
                movieCd, movieNm, genreNm, dir_peopleNm, act_peopleNm1, 
                act_peopleNm2, watchGradeNm
            )
            VALUES (
                {i['movieInfoResult']['movieInfo']['movieCd']},
                \"{i['movieInfoResult']['movieInfo']['movieNm']}\",
                \"{i['movieInfoResult']['movieInfo']['genres'][0]['genreNm']}\",
                \"{i['movieInfoResult']['movieInfo']['directors'][0]['peopleNm']}\",
                \"{i['movieInfoResult']['movieInfo']['actors'][0]['peopleNm']}\",
                \"{i['movieInfoResult']['movieInfo']['actors'][1]['peopleNm']}\",
                \"{i['movieInfoResult']['movieInfo']['audits'][0]['watchGradeNm']}\"
            )
        """
        cur.execute(sql_1)
    else:
        sql_2 = f"""
                INSERT INTO Movie_director_api (
                movieCd, movieNm, genreNm, dir_peopleNm, act_peopleNm1, 
                act_peopleNm2, act_peopleNm3, watchGradeNm
            )
            VALUES (
                {i['movieInfoResult']['movieInfo']['movieCd']},
                \"{i['movieInfoResult']['movieInfo']['movieNm']}\",
                \"{i['movieInfoResult']['movieInfo']['genres'][0]['genreNm']}\",
                \"{i['movieInfoResult']['movieInfo']['directors'][0]['peopleNm']}\",
                \"{i['movieInfoResult']['movieInfo']['actors'][0]['peopleNm']}\",
                \"{i['movieInfoResult']['movieInfo']['actors'][1]['peopleNm']}\",
                \"{i['movieInfoResult']['movieInfo']['actors'][2]['peopleNm']}\",
                \"{i['movieInfoResult']['movieInfo']['audits'][0]['watchGradeNm']}\"
            )
        """
        cur.execute(sql_2)

conn.commit()
cur.close()
