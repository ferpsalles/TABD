
from flask import Flask, jsonify, request, render_template, url_for, Response
from flaskext.mysql import MySQL
import pymysql
import xlwt
import io


app = Flask(__name__, template_folder='template')

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'senha'
app.config['MYSQL_DATABASE_DB'] = 'store'
mysql.init_app(app)


@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/dowload/report/excel')
def download_report():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(
        "SELECT customerNumber, start_ts, customerName FROM customer")
    result = cursor.fetchall()

    ## output in Bytes
    output = io.BytesIO()

    # create a workbook object
    workbook = xlwt.Workbook()

    # add a sheet
    sh = workbook.add_sheet('sheet')

    ## write in headers
    sh.write(0, 0, 'Número do Cliente')
    sh.write(0, 1, 'Início')
    sh.write(0, 2, 'Nome')

    idx = 0

    # write in row values
    for row in result:

        sh.write(idx+1, 0, str(row['customerNumber']))
        sh.write(idx+1, 1, row['start_ts'])
        sh.write(idx+1, 2, row['customerName'])
        idx += 1

    workbook.save(output)
    output.seek(0)
    return Response(output, mimetype="application/ms-excel", headers={"Content-Disposition": "attachment;filename=customer_report.xls"})


if __name__ == "__main__":
    app.run(debug=True)
