from flask import Flask, render_template, request
import pickle
import pandas as pd


app = Flask(__name__)
ridge_model = pickle.load(open('C:\\Users\\HB\\Section3\\Section3_Project\\model.pkl','rb'))

@app.route('/index/',defaults={'num':0})
@app.route('/index/<num>')
def index_num(num):
    return 'Welcome to Index %i' % int(num)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/write_action', methods=['POST'])
def index_1():
    genre = request.form.get('genre')
    director = request.form.get('director')
    actor1 = request.form.get('actor1')
    actor2 = request.form.get('actor2')
    watchGrade = request.form.get('watchGrade')

    X_test = pd.DataFrame([[genre,director,actor1,actor2,watchGrade]], 
                columns = ['genreNm','dir_peopleNm', 'act_peopleNm1','act_peopleNm2','watchGradeNm'])
    X_test_ohe = ridge_model[1].transform(X_test)
    y_test_pred = ridge_model[0].predict(X_test_ohe)
    res = format(y_test_pred[0],'f')
    res = res.split('.')[0]
    return  f'예측한 누적 매출액은 {res}원 입니다.'

if __name__ == "__main__":
    app.run(debug=True)