from flask import Flask, request, redirect,jsonify,render_template
from datetime import datetime
import json
import random
from flask_cors import CORS

alerts = []
currentalerts = {}

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
        if request.form['pw'] == 'wj301':
            Class = '1'
            result['text'] = request.form['text']
            result['date'] = current_date_yyyymmdd()
            alerts.append(result)
            currentalerts[Class] = result['text']
            return render_template('writealert.html')
        elif request.form['pw'] == 'wj302':
            Class = '2'
            result['text'] = request.form['text']
            result['date'] = current_date_yyyymmdd()
            alerts.append(result)
            currentalerts[Class] = result['text']
            return render_template('writealert.html')
        elif request.form['pw'] == 'wj303':
            Class = '3'
            result['text'] = request.form['text']
            result['date'] = current_date_yyyymmdd()
            alerts.append(result)
            currentalerts[Class] = result['text']
            return render_template('writealert.html')
        elif request.form['pw'] == 'wj304':
            Class = '4'
            result['text'] = request.form['text']
            result['date'] = current_date_yyyymmdd()
            alerts.append(result)
            currentalerts[Class] = result['text']
            return render_template('writealert.html')
        elif request.form['pw'] == 'wj305':
            Class = '5'
            result['text'] = request.form['text']
            result['date'] = current_date_yyyymmdd()
            alerts.append(result)
            currentalerts[Class] = result['text']
            return render_template('writealert.html')
        elif request.form['pw'] == 'wj306':
            Class = '6'
            result['text'] = request.form['text']
            result['date'] = current_date_yyyymmdd()
            alerts.append(result)
            currentalerts[Class] = result['text']
            return render_template('writealert.html')
        elif request.form['pw'] == 'wj307':
            Class = '7'
            result['text'] = request.form['text']
            result['date'] = current_date_yyyymmdd()
            alerts.append(result)
            currentalerts[Class] = result['text']
            return render_template('writealert.html')
        else:
            return '비밀번호 오류'

        
        

app.run(debug=True)