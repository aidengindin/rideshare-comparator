import mysql.connector

file = open('databaseKey.txt', 'r')
lines = file.readlines()

# Connecting to the mySQL Server
mydb = mysql.connector.connect(
    host=str(lines[0]),
    user="root",
    passwd=str(lines[1]),
    database="rideshare-comparator"
)
mc = mydb.cursor()

file.close()

d = open('data.txt', 'w')


d.write("REQUEST TABLE DATA\n")
d.write("ID | Src Lat | Src Lon | Dst Lat | Dst Lon |   Date   | Time | Distance\n")
mc.execute("SELECT * FROM request")

for x in mc:
    for i in range(0, len(x)):
        d.write(str(x[i]) + " | ")

    d.write("\n")
        

d.write("\n")

d.write("RIDE TABLE DATA\n")
d.write("ID | Name | Price | Sts | Shrd | StartTime | EndTime\n")
mc.execute("SELECT * FROM ride")

for x in mc:
    for i in range(0, len(x)):
        d.write(str(x[i]) + " | ")

    d.write("\n")


d.write("\n")

d.write("GENERATES TABLE DATA\n")
d.write("req | rid\n")
mc.execute("SELECT * FROM generates")

for x in mc:
    for i in range(0, len(x)):
        d.write(str(x[i]) + " | ")

    d.write("\n")



d.close()
