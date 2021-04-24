import mysql.connector
import datetime as dt
import time

mydb = mysql.connector.connect(
    host= "localhost",
    user = "root",
    passwd = "Rashnar18",
    database = "rideshare-comparator"
    )
mc = mydb.cursor()

def isHigher(scrLat, srcLon, destLat, destLon, distance, results): #, distance, results): 
    costHigher = False
  
    #Current date and time for request made
    date = dt.date.today()
    t = time.localtime()
    now = time.strftime("%H:%M:%S", t)
    totalPrice = 0
    count = 0

    histAvg = calcAVG(distance)
    if(histAvg is 1):
        return costHigher
    
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
    mydb.commit()
    
    currAvg = float(totalPrice/count)
    percInc = 100*((histAvg - currAvg)/(histAvg))
    print(percInc)
    if(percInc > 50):
        costHigher = True
    
    return costHigher

def clearTables():
    #Clearing the tables - for testing purposes
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
    mc.execute("SELECT * FROM request JOIN generates ON request.reqid = generates.reqid JOIN ride ON ride.rid = generates.rid")
    for x in mc:
        print(x)


def calcAVG(distance):
    d = distance
    mc.execute("SET @d:= 'distance'")
    mc.execute("SELECT AVG(price) FROM ride JOIN generates ON ride.rid = generates.rid JOIN request ON request.reqid = generates.reqid")
    print(type(mc.fetchall()))
    if(not all(mc.fetchall())):
        entry = str(mc.fetchall()[0])
        avg1 = entry.replace("(","")
        avg2 = avg1.replace(")","")
        avg = avg2.replace(",","")
        return float(avg)
    else:
        print("HELLO")
        return 1

    
dicList = [{'name': "UberXL", 'price': 32.12, 'seats': 3, 'shared': 0, 'pickup': '20:59:59', 'arrival': '23:59:59'},
           {'name': "UberX", 'price': 21.51, 'seats': 3, 'shared': 1, 'pickup': '15:59:59', 'arrival': '21:59:59'},
           {"name": "Uber Pool", "price": 54.68, "seats": 2, "shared": 0, "pickup": '16:59:59', "arrival": '22:59:59'},
           {"name": "Uber Comfort", "price": 56.25, "seats": 1, "shared": 0, "pickup": '18:59:59', "arrival": '23:59:59'}]

print(isHigher(100.231,243.21, 200.451, 354.213,15.23,dicList))
#clearTables()
#checkTables()
#check()

