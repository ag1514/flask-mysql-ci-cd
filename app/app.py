from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        connection = mysql.connector.connect(
            host='db',
            user='root',
            password='rootpassword',
            database='flaskdb'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        return jsonify(message=f"Connected to database: {record}")
    except Exception as e:
        return jsonify(error=str(e))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
