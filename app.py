from flask import Flask, jsonify, request
from datetime import datetime
from flaskext.mysql import MySQL
import hashlib

app = Flask(__name__)



mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'fishee_v1_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 8889
mysql.init_app(app)

@app.route("/v1/sensor", methods = ['POST'])
def insert_sensor():
   conn = mysql.connect()
   _device_id  = request.form['device_id']
   _datetime = datetime.now()

   _mdb = "1911130001"
   _mdb_name = "admin"
   _mdd = datetime.now()

   _celcius = request.form['celcius']
   _ph = request.form['ph']
   _ketinggian = request.form['ketinggian']

   conn = mysql.connect()
   cur = conn.cursor()

   querySuhu = """INSERT INTO `sensor_suhu` (`device_id`, `datetime`, `celcius`, `mdb`, `mdb_name`, `mdd`) VALUES (%s,%s,%s,%s,%s,%s)"""
   queryPh = """INSERT INTO `sensor_ph` (`device_id`, `datetime`, `ph`, `mdb`, `mdb_name`, `mdd`) VALUES (%s,%s,%s,%s,%s,%s)"""
   queryKetinggian = """INSERT INTO `sensor_ketinggian` (`device_id`, `datetime`, `ketinggian`, `mdb`, `mdb_name`, `mdd`) VALUES (%s,%s,%s,%s,%s,%s)"""
   
   cur.execute(querySuhu, (_device_id, _datetime, _celcius, _mdb_name, _mdb_name, _mdd))
   cur.execute(queryPh, (_device_id, _datetime, _ph, _mdb_name, _mdb_name, _mdd))
   cur.execute(queryKetinggian, (_device_id, _datetime, _ketinggian, _mdb_name, _mdb_name, _mdd))

   conn.commit()
   return jsonify(message="Insert data berhasil", status=True)



@app.route("/v1/feed", methods = ['POST'])
def data_feed():
   conn = mysql.connect()
   _device_id  = request.form['device_id']

   _celcius = request.form['suhu']
   _ph = request.form['ph']

   _time_created	 = datetime.now()
   _debit_feed = request.form['debit_feed']
   _weather = request.form['weather']

   conn = mysql.connect()
   cur = conn.cursor()

   query = """INSERT INTO `data_feeder` (`device_id`, `suhu`, `ph`, `time_created`, `debit_feed`, `weather`) VALUES (%s,%s,%s,%s,%s,%s)"""
   
   cur.execute(query, (_device_id, _celcius, _ph, _time_created, _debit_feed, _weather))

   conn.commit()
   return jsonify(message="Insert data berhasil", status=True)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)