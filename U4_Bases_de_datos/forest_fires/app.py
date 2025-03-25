from flask import Flask, render_template, request
import psycopg2
import create_table
import consts as c

app = Flask(__name__)

create_table.create_and_import(c.DB_PARAMS, c.CSV_PATH_1, c.TABLE_NAME_1)

@app.route('/')
def index():
    conn = psycopg2.connect(**c.DB_PARAMS)
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM {c.TABLE_NAME_1};")
    records = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    
    cursor.close()
    conn.close()
    return render_template('index.html', records=records, columns=columns)

@app.route('/query', methods=['GET', 'POST'])
def query():
    records = None
    columns = None
    if request.method == 'POST':
        query = request.form['query']
        try:
            conn = psycopg2.connect(**c.DB_PARAMS)
            cursor = conn.cursor()
            
            cursor.execute(query)
            records = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            
            cursor.close()
            conn.close()
        except Exception as e:
            records = None
            print(f"Error: {e}")
    
    return render_template('query.html', records=records, columns=columns)

if __name__ == '__main__':
    app.run(debug=True)
