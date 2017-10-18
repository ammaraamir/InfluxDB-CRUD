# InfluxDB-CRUD

The purpose of this repository is to provide a flask app integrated with InfluxDB which performs CRUD operations on time series data. 
You can do the following operations using this application:

  - Create
  - Insert
  - Select
  - Update
  - Delete

# Requirements
  - Python 2.7
  - Flask
  - Influxdb
  - Influxdb-Python

### Installation

To run this application:

Install the dependencies and  start the service.
Download or Clone this repository.
```sh
$ wget "https://gitlab.com/data-intelligence-hub/InfluxDB.git"
$ cd InfluxDB
$ python basic_app.py
```
It should produce the following output...
```sh
$ Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
If everything goes well. You will see a screen with multiple options.

- You can create a db.
- You can name a db to use. (This is MUST)
- You can run select query on db you are using.
- You can insert data in db.
- You can update the data in db.
- You can delete the db.
