from flask import Flask, jsonify 
import pandas as pd
from sqlalchemy import create_engine
from config import username, password

app = Flask(__name__)

engine = create_engine('postgresql://{}:{}@localhost:5432/California_Renewables'.format(username, password))

conn = engine.connect()
##sql = 'select a."ds", a.yhat as "Predicted Value", b."RENEW TOTAL" as "True Production", (a.yhat - b."RENEW TOTAL") as "Error"From "RenewablePredictions" aleft join "RenewableProduction" bon a."ds" = b."TIMESTAMP"order by a."ds"'
#responce_data = pd.read_sql(sql=sql,con=conn)



@app.route('/')
def home():
    return ('Welcome to my Renewable Predictions API! <br/>'
    'Available Routes: <br/>'
    'localhost:5000/Contact <br/>'
    'localhost:5000/API/Date/01-01-2017 <br/>'
    'localhost:5000/API/Date_Range/01-01-2017#01-31-2017 ')

@app.route('/Contact')
def contact():
    name = 'Graham Penrose'
    email = 'grahamelpenrose@gmail.com'
    return 'Please contact {} at {} with any questions/ comments'.format(name, email)

@app.route('/API/Date/<date_str>')
def get_date_data(date_str):
    responce_dict = {}
    sql = '''select a."ds", a.yhat as "Predicted Value", b."RENEW TOTAL" as "True Production", \
            (a.yhat - b."RENEW TOTAL") as "Error" From "RenewablePredictions" a left join "RenewableProduction" b \
            on a."ds" = b."TIMESTAMP" where to_char(a."ds", 'YYYY-mm-dd') = '{}'\
            order by a."ds"'''.format(date_str)
    responce_data = pd.read_sql(sql=sql,con=conn)
    for index, row in responce_data.iterrows():
        responce_dict['{}'.format(row[0])] = [{'Predicted Production':row[1],'True Production':row[2]}]
    return jsonify(responce_dict)

if __name__ == '__main__':
    app.run(debug=True)

