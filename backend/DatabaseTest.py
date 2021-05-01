import mysql.connector
import datetime as dt
import time

# Connecting to the mySQL Server 
mydb = mysql.connector.connect(
    host= "localhost",
    user = "root",
    passwd = "Rashnar18",
    database = "rideshare-comparator"
    )
mc = mydb.cursor()

# Main method that returns 
def isHigher(scrLat, srcLon, destLat, destLon, distance, results):
    costHigher = False
  
    #Current date and time for request made
    date = dt.date.today()
    t = time.localtime()
    now = time.strftime("%H:%M:%S", t)

    # Setting of variables to calculate the average and cost
    totalPrice = 0
    count = 0
    histAvg = calcAVG(distance)
    
    # Inserting into the request table and getting the id of the request to use later on
    mc.execute("INSERT INTO request(srcLat, srcLon, destLat, destLon, date, time, distance) VALUES(%s,%s,%s,%s,%s,%s,%s)", (scrLat, srcLon, destLat, destLon, date, now, distance))
    lastreqid = mc.lastrowid

    # Looping through the dictionary to generate the rides
    for result in results:
        name = result["name"]
        price = result["price"]
        seats = result["seats"]
        shared = result["shared"]
        pString = result["pickup"]
        pickup = dt.datetime.strptime(pString, "%Y-%m-%dT%H:%M:%S").time()
        aString = result["arrival"]
        arrival = dt.datetime.strptime(aString, "%Y-%m-%dT%H:%M:%S").time()
        mc.execute("INSERT INTO ride(name, price, seats, shared, pickup, arrival) VALUES(%s,%s,%s,%s,%s,%s)", (name, price, seats, shared, pickup, arrival))
        lastrid = mc.lastrowid
        mc.execute("INSERT INTO generates(reqid, rid) VALUES(%s, %s)",(lastreqid, lastrid))
        totalPrice += price
        count += 1
    mydb.commit()
    # If there is no data in the database yet, return False
    if(histAvg == 1):
        return costHigher

    # Calculation of average 
    currAvg = float(totalPrice/count)
    percInc = 100*((currAvg - histAvg)/(currAvg))
    # If the price is 50% higher than the historical data, return true, otherwise return false
    if(percInc > 50):
        costHigher = True
    return costHigher

#Clearing the tables - for testing purposes
def clearTables():
    mc.execute("DELETE FROM generates")
    mc.execute("DELETE FROM request")
    mc.execute("DELETE FROM ride")
    mc.execute("ALTER TABLE request AUTO_INCREMENT = 0")
    mc.execute("ALTER TABLE ride AUTO_INCREMENT = 0")
    mydb.commit()

# Set of SELECT ALL queries to check each table and print them out / for development testing
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
# Another testing method, which SELECTs ALL from the combination of the tables
def check():
    mc.execute("SELECT * FROM request JOIN generates ON request.reqid = generates.reqid JOIN ride ON ride.rid = generates.rid")
    for x in mc:
        print(x)

# Calculates the average cost of rides within 
def calcAVG(distance):
    # Creating upper and lower bounds
    upper = distance + 2
    lower = distance - 2
    # Inserting data into table in order to reference them later
    mc.execute("INSERT INTO distances(upper, lower) VALUES(%s,%s)",(upper, lower))
    # Query, calculating the average price of rides in which the distance is within +- 2 miles
    mc.execute("SELECT AVG(price) FROM ride JOIN generates ON ride.rid = generates.rid JOIN request ON request.reqid = generates.reqid, distances WHERE request.distance BETWEEN distances.lower AND distances.upper")
    # Manipulating the query result into a float and deleting the upper and lower bound from the table
    var = mc.fetchall()[0]
    entry = str(var)
    avg1 = entry.replace("(","")
    avg2 = avg1.replace(")","")
    avg = avg2.replace(",","")
    mc.execute("DELETE FROM distances")
    if(avg == "None"):
        return 1
    else:
        return float(avg)

# Function used to test the query, with data that should return False 
def testFalse():
    clearTables()
    dicList = [{'name': "UberXL", 'price': 32.12, 'seats': 3, 'shared': 0, 'pickup': '2007-03-04T21:08:12', 'arrival': '2007-03-04T21:08:12'},
           {'name': "UberX", 'price': 21.51, 'seats': 3, 'shared': 1, 'pickup': '2007-03-04T15:28:16', 'arrival': '2007-03-04T21:08:12'},
           {"name": "Uber Pool", "price": 54.68, "seats": 2, "shared": 0, "pickup": '2007-03-04T01:08:12', "arrival": '2007-03-04T21:08:12'},
           {"name": "Uber Comfort", "price": 56.25, "seats": 1, "shared": 0, "pickup": '2007-03-04T21:08:12', "arrival": '2007-03-04T21:08:12'}]
    dicList2 = [{'name': "UberXL", 'price': 42.12, 'seats': 3, 'shared': 0, 'pickup': '2007-03-04T21:08:12', 'arrival': '2007-03-04T21:08:12'},
           {'name': "UberX", 'price': 31.51, 'seats': 3, 'shared': 1, 'pickup': '2007-03-04T15:28:16', 'arrival': '2007-03-04T21:08:12'},
           {"name": "Uber Pool", "price": 54.68, "seats": 2, "shared": 0, "pickup": '2007-03-04T01:08:12', "arrival": '2007-03-04T21:08:12'},
           {"name": "Uber Comfort", "price": 56.25, "seats": 1, "shared": 0, "pickup": '2007-03-04T21:08:12', "arrival": '2007-03-04T21:08:12'}]
    isHigher(100.231,243.21, 200.451, 354.213,15.23,dicList)
    print("OUTCOME: "),
    print(isHigher(100.231,243.21, 200.451, 354.213,15.23,dicList2))
    checkTables()
    clearTables()

# Function used to test the query, with data that should return True
def testTrue():
    clearTables()
    dicList = [{'name': "UberXL", 'price': 32.12, 'seats': 3, 'shared': 0, 'pickup': '2007-03-04T21:08:12', 'arrival': '2007-03-04T21:08:12'},
           {'name': "UberX", 'price': 21.51, 'seats': 3, 'shared': 1, 'pickup': '2007-03-04T15:28:16', 'arrival': '2007-03-04T21:08:12'},
           {"name": "Uber Pool", "price": 54.68, "seats": 2, "shared": 0, "pickup": '2007-03-04T01:08:12', "arrival": '2007-03-04T21:08:12'},
           {"name": "Uber Comfort", "price": 56.25, "seats": 1, "shared": 0, "pickup": '2007-03-04T21:08:12', "arrival": '2007-03-04T21:08:12'}]
    dicList2 = [{'name': "UberXL", 'price': 82.12, 'seats': 3, 'shared': 0, 'pickup': '2007-03-04T21:08:12', 'arrival': '2007-03-04T21:08:12'},
           {'name': "UberX", 'price': 51.51, 'seats': 3, 'shared': 1, 'pickup': '2007-03-04T15:28:16', 'arrival': '2007-03-04T21:08:12'},
           {"name": "Uber Pool", "price": 74.68, "seats": 2, "shared": 0, "pickup": '2007-03-04T01:08:12', "arrival": '2007-03-04T21:08:12'},
           {"name": "Uber Comfort", "price": 156.25, "seats": 1, "shared": 0, "pickup": '2007-03-04T21:08:12', "arrival": '2007-03-04T21:08:12'}]
    isHigher(100.231,243.21, 200.451, 354.213,15.23,dicList)
    print("OUTCOME: "),
    print(isHigher(100.231,243.21, 200.451, 354.213,16.23,dicList2))
    checkTables()
    clearTables()
