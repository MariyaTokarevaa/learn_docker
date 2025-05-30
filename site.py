from flask import Flask
import psycopg2

app=Flask(__name__)

@app.route('/')
def index():
    conn=psycopg2.connect(dbname='postgres', user='postgres', password='12345', host='dbps')
    cursor=conn.cursor()

    cursor.execute('SELECT * FROM women LIMIT 10')
    records=cursor.fetchall()
    cursor.close()
    conn.close()


    return '<h1>Hello from Flas_Docker</h1>' + f'{"<p>".join(map(str, records))}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)