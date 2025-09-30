from flask import Flask
import pyodbc
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # Get connection string from environment (set via Key Vault)
        conn_str = os.environ.get('DBConnectionString')
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT @@VERSION")
        version = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return f"Connected to SQL Server: {version}"
    except Exception as e:
        return f"Error connecting to database: {str(e)}"

@app.route('/health')
def health():
    return "App is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)