import pymysql
class db:
    def __init__(self): 
        self.con = pymysql.connect(host='localhost', database='store', user='root',password='senha')
        self.cursor = self.con.cursor()

    def createshema(self):
        sql_query = """CREATE TABLE customer (
        customerNumber INT PRIMARY KEY AUTO_INCREMENT,
        start_ts TIMESTAMP DEFAULT NOW(),
        customerName varchar(20) NOT NULL
        ) AUTO_INCREMENT=1;
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
        query ='CREATE TRIGGER before_customer_delete BEFORE DELETE ON customer FOR EACH ROW BEGIN INSERT INTO CustomerArchives(customerNumber, customerName, start_ts) VALUES(OLD.customerNumber, OLD.customerName, old.start_ts); UPDATE sales SET customerNumber = "9999" Where customerNumber= OLD.customerNumber; END'
        self.cursor.execute(query)
        self.con.close()