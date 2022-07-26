
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from db import db

app = Flask(__name__)

mysql = MySQL(app)



@app.route('/customer', methods=["GET", "POST"])
def customer ():
    con = db().con
    cursor = con.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM customer")
        customer = [
            dict(customerNumber=row[0], start_ts=row[1], name=row[2])
            for row in cursor.fetchall()
        ]
        if customer is not None:
            return jsonify(customer)
    
    if request.method == 'POST':
        new_customer = request.form["customerName"]
        new_date = request.form["start_ts"]
        sql = """INSERT INTO customer(customerName, start_ts) values (%s, %s)"""
        cursor = cursor.execute (sql, (new_customer, new_date))
        con.commit()
        return f"Customer created successfully"


@app.route("/customer/<int:customerNumber>", methods=["GET"])
def get_customer(customerNumber):
    con = db().con
    cursor = con.cursor()
    customer = None
    cursor.execute("SELECT * FROM customer WHERE customerNumber = %s", (customerNumber,))
    rows = cursor.fetchall()
    for r in rows:
            customer = r
            if customer is not None:
                return jsonify(customer), 200
            else:
                return ("No customer"), 404
    
@app.route("/customer/<int:customerNumber>", methods=["PUT"])
def edit_customer(customerName):
    con = db().con
    cursor = con.cursor()
    customer = None
    post_data= request.get_json()
    customer.insert({
            'customerNumber': post_data['customerNumber'],
            'customerName':post_data['customerName']
        })
    con.commit()
    return "Sucess"

@app.route("/customer/<int:customerNumber>", methods=["DELETE"])
def delete_customer(customerNumber):
    con = db().con
    cursor = con.cursor()
    cursor.execute(f"Delete FROM customer WHERE customerNumber = {customerNumber}")
    con.commit()
    return "The customer with the id: {} has been deleted." .format(customerNumber),200

@app.route("/customer/config", methods=["GET"])
def trigger_customer():
    db().createtrigger()
    return "Trigger created"


           


if __name__ == "__main__":
    app.run(debug=True)
