
from flask import Flask
from flask_mysqldb import MySQL
mysql = MySQL()
app = Flask(__name__)
# My SQL Instance configurations 
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rockyouon1'
app.config['MYSQL_DB'] = 'studentbook'
app.config['MYSQL_HOST'] = '35.195.10.161'
mysql.init_app(app)
# The first route to access the webservice from http://external-ip:5000/ 
#@pp.route("/add") this will create a new endpoints that can be accessed using http://external-ip$
@app.route("/")

def hello(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM students''')
    cur.execute('''INSERT INTO students(studentName, email) values("Im a NEW Student", "xxxSNIPARZxxx@mydit.ie")''')
	cur.execute('''UPDATE students SET studentName='Jackie' WHERE studentName='first Student';''')
	cur.execute('''DELETE FROM students WHERE studentName LIKE '%second%';''')# execute an SQL statment
    rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    return str(rv)      #Return the data in a string format
if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000') #Run the flask app at port 5000
