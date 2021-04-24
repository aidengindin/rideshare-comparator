import mysql.connector
import datetime as dt
import time

<<<<<<< Updated upstream

def database_function(scrLat, srcLon, destLat, destLon): #, results_list): 
    #put password in file - read it
    mydb = mysql.connector.connect(
        host= "localhost",
        user = "root",
        passwd = "Rashnar18",
        database = "rideshare-comparator"
        )
    mc = mydb.cursor()
    costHigher = True
    #rideList = 
    
    """
     Template code to insert data into tables
     q1 = mc.execute("INSERT INTO request (srcLat, srcLon, destLat, destLon, date, time) VALUES(%s,%s,%s,%s,%s,%s)", (srcLat, srcLon, destLat, destLon, date, time)
     q2 = mc.execute("INSERT INTO ride (name, price, seats, shared, pickup, arrival) VALUES(%s,%s,%s,%s,%s,%s)", (name, price, seats, shared, pickup, arrival)
     q3 = mc.execute("INSERT INTO generates(reqid, rid) VALUES(%s, %s)",(lastreqid, lastrid))    
    """

    # Inserting the request, rides, and generates
    """ 
    mc.execute("INSERT INTO request(srcLat, srcLon, destLat, destLon, date, time) VALUES(%s,%s,%s,%s,%s,%s)", (100.231, 243.21, 200.451, 354.213, '2021-4-12', '18:25:00'))
    lastreqid = mc.lastrowid
    
    FOR LOOP-as many entries in results_list
        
        adding up the prices
        mc.execute("INSERT INTO ride(name, price, seats, shared, pickup, arrival) VALUES(%s,%s,%s,%s,%s,%s)", ('pool', 32.31, 3, 0, '20:59:59', '23:59:59'))
        lastrid = mc.lastrowid
        mc.execute("INSERT INTO generates(reqid, rid) VALUES(%s, %s)",(lastreqid, lastrid))
    """
    
    #mydb.commit()

    #Current date and time for request made
    date = dt.date.today()
    t = time.localtime()
    now = time.strftime("%H:%M:%S", t)
    
    mc.execute("INSERT INTO request(srcLat, srcLon, destLat, destLon, date, time) VALUES(%s,%s,%s,%s,%s,%s)", (scrLat, srcLon, destLat, destLon, date, t))

    

    #Clearing the specified table - for testing purposes
    #mc.execute("DELETE FROM request")
    #mc.execute("DELETE FROM ride")
    #mc.execute("DELETE FROM generates")

    """
    mc.execute("SELECT * FROM request")
    for x in mc:
        print(x)
    """

    # AVG the rides Get the list of rides with similar distance traveled, (maybe time), return list --> get average, run an if statement
        # calc distance from lat and lon for every entry
    
    return costHigher

database_function(100.231,243.21, 200.451, 354.213)
=======
mydb = mysql.connector.connect(
    host= "localhost",
    user = "root",
    passwd = "Rashnar18",
    database = "rideshare-comparator"
    )
mc = mydb.cursor()

def isHigher(scrLat, srcLon, destLat, destLon, distance, results): #, distance, results): 
    costHigher = True
  
    #Current date and time for request made
    date = dt.date.today()
    t = time.localtime()
    now = time.strftime("%H:%M:%S", t)
    totalPrice = 0
    count = 0

    histAvg = calcAVG(distance)
    
    mc.execute("INSERT INTO request(srcLat, srcLon, destLat, destLon, date, time, distance) VALUES(%s,%s,%s,%s,%s,%s,%s)", (scrLat, srcLon, destLat, destLon, date, t, distance))
    lastreqid = mc.lastrowid
    
    for result in results:
        name = result["name"]
        price = result["price"]
        seats = result["seats"]
        shared = result["shared"]
        pickup = result["pickup"]
        arrival = result["arrival"]
        mc.execute("INSERT INTO ride(name, price, seats, shared, pickup, arrival) VALUES(%s,%s,%s,%s,%s,%s)", (name, price, seats, shared, pickup, arrival))
        lastrid = mc.lastrowid
        mc.execute("INSERT INTO generates(reqid, rid) VALUES(%s, %s)",(lastreqid, lastrid))
        totalPrice += price
        count += 1
    
    print(totalPrice/count)
    mydb.commit()  
    # AVG the rides Get the list of rides with similar distance traveled, (maybe time), return list --> get average, run an if statement
    currAvg = totalPrice/count
    print(histAvg)
 
    
    return costHigher

def clearTables():
    #Clearing the specified table - for testing purposes
    mc.execute("DELETE FROM generates")
    mc.execute("DELETE FROM request")
    mc.execute("DELETE FROM ride")
    mc.execute("ALTER TABLE request AUTO_INCREMENT = 0")
    mc.execute("ALTER TABLE ride AUTO_INCREMENT = 0")
    mydb.commit()

def checkTables():
    mc.execute("SELECT * FROM request")
    for x in mc:
        print(x)
    mc.execute("SELECT * FROM ride")
    for x in mc:
        print(x)
    mc.execute("SELECT * FROM generates")
    for x in mc:
        print(x)

def check():
    mc.execute("SELECT * FROM request JOIN generates ON request.reqid = generates.reqid JOIN ride ON ride.rid = generates.rid WHERE request.distance > (d-1) AND request.distance < (d+1)")
    for x in mc:
        print(x)


def calcAVG(distance):
    d = distance
    mc.execute("SELECT AVG(price) AS ap FROM ride JOIN generates ON ride.rid = generates.rid JOIN request ON request.reqid = generates.reqid")
    avg = mc.fetchone()[0]
    return avg

    
dicList = [{'name': "UberXL", 'price': 32.12, 'seats': 3, 'shared': 0, 'pickup': '20:59:59', 'arrival': '23:59:59'},
           {'name': "UberX", 'price': 21.51, 'seats': 3, 'shared': 1, 'pickup': '15:59:59', 'arrival': '21:59:59'},
           {"name": "Uber Pool", "price": 54.68, "seats": 2, "shared": 0, "pickup": '16:59:59', "arrival": '22:59:59'},
           {"name": "Uber Comfort", "price": 56.25, "seats": 1, "shared": 0, "pickup": '18:59:59', "arrival": '23:59:59'}]

isHigher(100.231,243.21, 200.451, 354.213,15.23,dicList)
#clearTables()
#checkTables()
#check()

>>>>>>> Stashed changes
