
from flask import Flask, jsonify, request, render_template, url_for, Response
import pymysql
import xlwt
import io


class db:
    def __init__(self):
        self.con = pymysql.connect(
            host='localhost', database='store', user='root', password='senha')
        self.cursor = self.con.cursor()

    def createshema(self):
        sql_query = """CREATE TABLE customer (
        customerNumber int unsigned PRIMARY KEY,
        start_ts TIMESTAMP DEFAULT NOW(),
        customerName varchar(20) NOT NULL
        )ENGINE=InnoDB AUTO_INCREMENT=7975 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
        create table product (
        productNumber int primary key AUTO_INCREMENT,
        productName varchar (20) not null,
        productMaker varchar (20),
        productDescription varchar (50) not null
        ) AUTO_INCREMENT=1;

        create table sales (
        salesNumber int primary key not null AUTO_INCREMENT,
        validFrom TIMESTAMP DEFAULT NOW(),
        productNumber int not null,
        customerNumber int not null
        )AUTO_INCREMENT=1;

        ALTER TABLE sales ADD CONSTRAINT fk_productNumber FOREIGN KEY ( productNumber ) REFERENCES product ( productNumber );
        ALTER TABLE sales ADD CONSTRAINT fk_customerNumber FOREIGN KEY ( customerNumber ) REFERENCES customer ( customerNumber ) ;

        CREATE TABLE CustomerArchives (
            id INT PRIMARY KEY AUTO_INCREMENT,
            customerNumber INT,
            customerName varchar (20),
            start_ts date,
            deletedAt TIMESTAMP DEFAULT NOW()
        )AUTO_INCREMENT=1;
        """

        self.cursor.execute(sql_query)
        self.con.close()

    def createtrigger(self):
        query = 'CREATE TRIGGER before_customer_delete BEFORE DELETE ON customer FOR EACH ROW BEGIN INSERT INTO CustomerArchives(customerNumber, customerName, start_ts) VALUES(OLD.customerNumber, OLD.customerName, old.start_ts); UPDATE sales SET customerNumber = "9999" Where customerNumber= OLD.customerNumber; END'
        self.cursor.execute(query)
        self.con.close()


    def download_report(self):
        query = "SELECT customerNumber, start_ts, customerName FROM customer"
        self.cursor.execute(query)
        result = self.cursor.fetchall()

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

            sh.write(idx+1, 0, row[0])
            sh.write(idx+1, 1, row[1])
            sh.write(idx+1, 2, row[2])
            idx += 1

        workbook.save(output)
        output.seek(0)
        return Response(output, mimetype="application/ms-excel", headers={"Content-Disposition": "attachment;filename=customer_report.xls"})
