from flask import Flask, render_template, request, redirect
from influxdb import InfluxDBClient
name = ""
json_body = [
    {
        "measurement": "cpu_load_short",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time": "2009-11-10T23:00:00Z",
        "fields": {
            "value": 0.64
        }
    }
]


import pyrebase
config = {
"apiKey": "AIzaSyDpdMk_GRtvNDExaZnH4NTMXlIpSXE8BEM",
"authDomain": "firstapp-5c5f7.firebaseapp.com",
"databaseURL": "https://firstapp-5c5f7.firebaseio.com",
"projectId": "firstapp-5c5f7",
"storageBucket": "firstapp-5c5f7.appspot.com",
"messagingSenderId": "885228640632",
             }

### TESTING ###
firebase = pyrebase.initialize_app(config)
db = firebase.database()
lat = db.child("Latitude").get().val()
lon = db.child("Longitude").get().val()
drID = db.child("Droneid").get().val()
detTime = db.child("Detectiontimestamp").get().val()
mode = db.child("DetectionMode").get().val()
anomType = db.child("Anomalydetect").get().val()
area = db.child("Opertionarea").get().val()


print(lat)
print(lon)
print(drID)
print(detTime)
print(mode)
print(anomType)
print(area)
### TESTING ###

client = InfluxDBClient('localhost', 8086, 'root', 'root', 'mydb')

### TESTING ###
client.write(['drone id="'+drID+'",lat='+lat+',lon='+lon+',type="'+anomType+'",mode="'+mode+'",area="'+area+'",time="'+detTime+'"'],{'db':'aiinspect'},204,'line')
print("Data Inserted for Drone")
### TESTING ###

#client.create_database('example_my')

#client.write_points(json_body)

email_addresses = []
app = Flask(__name__)

@app.route('/')
def hello_world():
    author = "Ammar Bin Aamir"
    name = "Shakoor!!!"
    return render_template('index.html', author=author, name=name)

@app.route('/create', methods = ['POST'])
def create():
	name = request.form['dbname']
	client.create_database(name)
	print("Database Created")
	return render_template('index.html')

@app.route('/usedb', methods = ['POST'])
def usedb():
	name = request.form['usedb']
	client.switch_database(name)
	print("Using db: " + name)
	return redirect('/')

@app.route('/select', methods = ['POST'])
def select():
	query = request.form['selectQuery']
	result = client.query(query)
	return "Result: {0}".format(result)

@app.route('/insert', methods = ['POST'])
def insert():
	insQuery = request.form['insertQuery']
	name1 = request.form['usedb']
	#client.write_points(insQuery)
	print(name1)
	client.write([insQuery],{'db':name1},204,'line')
	print("Data inserted")
	return redirect('/')

@app.route('/update', methods = ['POST'])
def update():
	lat = db.child("Latitude").get().val()
	lon = db.child("Longitude").get().val()
	drID = db.child("Droneid").get().val()
	detTime = db.child("Detectiontimestamp").get().val()
	mode = db.child("DetectionMode").get().val()
	anomType = db.child("Anomalydetect").get().val()
	area = db.child("Opertionarea").get().val()
	client.write(['drone id="'+drID+'",lat='+lat+',lon='+lon+',type="'+anomType+'",mode="'+mode+'",area="'+area+'",time="'+detTime+'"'],			{'db':'aiinspect'},204,'line')
	print("Data Updated")
	return redirect('/')
	#return render_template('update.html')

@app.route('/delete', methods = ['POST'])
def delete():
	delName = request.form['deleteQuery']
	client.drop_database(delName)
	print("Database Deleted")
	return redirect('/')

@app.route('/emails.html')
def emails():
    return render_template('emails.html', email_addresses=email_addresses)

if __name__ == "__main__":
    app.run()
