import mysql.connector
import datetime as dt


def database_function(scrLat, srcLon, destLat, destLon): #, results_list): 
    #put password in file - read it
    mydb = mysql.connector.connect(
        host="localhost",
        user = "root",
        passwd = "Rashnar18",
        database = "rideshare-comparator"
        )
    mc = mydb.cursor()
    
    
    # Template code to insert data into tables
    # q1 = mc.execute("INSERT INTO request (srcLat, srcLon, destLat, destLon, date, time) VALUES(%s,%s,%s,%s,%s,%s)", (srcLat, srcLon, destLat, destLon, date, time)
    # q2 = mc.execute("INSERT INTO ride (name, price, seats, shared, pickup, arrival) VALUES(%s,%s,%s,%s,%s,%s)", (name, price, seats, shared, pickup, arrival)
    # q3 = mc.execute("INSERT INTO generates(reqid, rid) VALUES(%s, %s)",(lastreqid, lastrid))    

    #mc.execute("INSERT INTO request(srcLat, srcLon, destLat, destLon, date, time) VALUES(%s,%s,%s,%s,%s,%s)", (100.231,243.21, 200.451, 354.213, '2021-4-12', '18:25:00'))
    #lastreqid = mc.lastrowid
    #mc.execute("INSERT INTO ride(name, price, seats, shared, pickup, arrival) VALUES(%s,%s,%s,%s,%s,%s)", ('pool', 32.31, 3, 0, '20:59:59', '23:59:59'))
    #lastrid = mc.lastrowid
    #mc.execute("INSERT INTO generates(reqid, rid) VALUES(%s, %s)",(lastreqid, lastrid))

    #mydb.commit()
    date = dt.date.today()
   # time = dt.now().time()
    mc.execute("INSERT INTO request(srcLat, srcLon, destLat, destLon, date, time) VALUES(%s,%s,%s,%s,%s,%s)", (100.231,243.21, 200.451, 354.213, '2021-4-12', '18:25:00'))


    #Clearing the specified table - for testing purposes
    #mc.execute("DELETE FROM request")
    #mc.execute("DELETE FROM ride")
    #mc.execute("DELETE FROM generates")

    mc.execute("SELECT * FROM request")
    for x in mc:
        print(x)

database_function(100.231,243.21, 200.451, 354.213)
