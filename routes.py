from flask import Flask,render_template
import mysql.connector
import json

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'database': 'medical',
  'raise_on_warnings': True,
}

link = mysql.connector.connect(**config)

mycursor = link.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
