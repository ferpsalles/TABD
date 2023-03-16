
from flask import Flask, render_template, url_for,  redirect
from flaskext.mysql import MySQL
import pymysql
import xlwt
import io
import cripto



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
    df=cripto.gerar_relatorio(conn)
    df.to_excel(r'C:\Users\fee_s\Desktop\store api\app\static\despesas_detal.xlsx')
    return redirect(url_for('static', filename='despesas_detal.xlsx'))

if __name__ == "__main__":
    app.run(debug=True)
