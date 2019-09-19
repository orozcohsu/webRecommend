import pyodbc

cnxn = pyodbc.connect("DSN=SpliceODBC64")

#Open a cursor
cursor = cnxn.cursor()

#Create weblog table
cursor.execute("CREATE TABLE WEBLOG(id int NOT NULL GENERATED ALWAYS AS IDENTITY (START WITH 1, INCREMENT BY 1), uuid varchar(2), item varchar(2), rating varchar(2), PRIMARY KEY (id))")
cnxn.commit();

#Create recommend table
cursor.execute("CREATE TABLE RECOMMEND(id int NOT NULL GENERATED ALWAYS AS IDENTITY (START WITH 1, INCREMENT BY 1), uuid varchar(2), item varchar(2), score decimal(5,2), PRIMARY KEY (id))")
cnxn.commit();
