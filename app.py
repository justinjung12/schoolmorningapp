from flask import Flask, request, redirect,jsonify,render_template
from datetime import datetime
import json
import random
from flask_cors import CORS

alerts = []
currentalerts = {}
test = ''
names = []
app = Flask(__name__)
CORS(app)
def current_date_yyyymmdd():
    # 현재 날짜를 가져옴
    current_date = datetime.now()
    # 'yyyymmdd' 형태로 포맷팅하여 문자열로 변환
    formatted_date = current_date.strftime('%Y%m%d')
    return str(formatted_date)




@app.route('/')
def main():
    print(currentalerts)
    return render_template('schoolapp.html')

@app.route('/currentalert',methods=['GET', 'POST'])
def currentalert():
    try:
        return currentalerts[request.form['class']]
    except:
        return '아직 알림이 없네요'
    
@app.route('/writealert',methods=['GET', 'POST'])
def writealert():
    global currentalerts
    if request.method == 'GET':
        return render_template('writealert.html')
    if request.method == 'POST':
        result = {}
        if request.form['pw'] == 'wj311':
            Class = '1'
            result['text'] = request.form['text']
            result['date'] = current_date_yyyymmdd()
            alerts.append(result)
            currentalerts[Class] = result['text']
            return render_template('writealert.html')
        elif request.form['pw'] == 'wj322':
            Class = '2'
            result['text'] = request.form['text']
            result['date'] = current_date_yyyymmdd()
            alerts.append(result)
            currentalerts[Class] = result['text']
            return render_template('writealert.html')
        elif request.form['pw'] == 'wj333':
            Class = '3'
            result['text'] = request.form['text']
            result['date'] = current_date_yyyymmdd()
            alerts.append(result)
            currentalerts[Class] = result['text']
            return render_template('writealert.html')
        elif request.form['pw'] == 'wj344':
            Class = '4'
            result['text'] = request.form['text']
            result['date'] = current_date_yyyymmdd()
            alerts.append(result)
            currentalerts[Class] = result['text']
            return render_template('writealert.html')
        elif request.form['pw'] == 'wj355':
            Class = '5'
            result['text'] = request.form['text']
            result['date'] = current_date_yyyymmdd()
            alerts.append(result)
            currentalerts[Class] = result['text']
            return render_template('writealert.html')
        elif request.form['pw'] == 'wj366':
            Class = '6'
            result['text'] = request.form['text']
            result['date'] = current_date_yyyymmdd()
            alerts.append(result)
            currentalerts[Class] = result['text']
            return render_template('writealert.html')
        elif request.form['pw'] == 'wj377':
            Class = '7'
            result['text'] = request.form['text']
            result['date'] = current_date_yyyymmdd()
            alerts.append(result)
            currentalerts[Class] = result['text']
            return render_template('writealert.html')
        else:
            return '비밀번호 오류'
@app.route('/writetest',methods=['GET', 'POST'])
def writetest():
    global test
    global currentalerts
    if request.method == 'GET':
        return render_template('writetest.html')
    if request.method == 'POST':
        test = request.form['test']
        return render_template('writetest.html')

@app.route('/test',methods=['GET', 'POST'])
def showtest():
    return test

@app.route('/name',methods=['GET', 'POST'])
def name():
    global names
    date = current_date_yyyymmdd()
    names.append([request.form['name'],date])
    print(names)
    return 'success'

@app.route('/showname',methods=['GET', 'POST'])
def showname():
    if request.method == 'GET':
        return render_template('showname.html')
    if request.method == 'POST':
        res = []
        if request.form['name'] != 'all':
            for i in names: 
                if i[0] == request.form['name']: 
                    res.append(i) 
            return str(res)
        else:
            return str(names)

