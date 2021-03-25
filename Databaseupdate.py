import mysql.connector

def main():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Smartgarden",
      database="SmartGarden"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO BME280 (time, Temperature, Pressure, Altitude, Humidity) VALUES (%s, %s, %s, %s, %s)"
    val = [
      ('3.30pm', 15, 10, 20, 51),
      ('4pm', 10, 12, 45, 80),
      ('4.30pm', -2, 50, 50, 40),
      ('5pm', 14, 40, 70, 80),
      ('5.30pm', 19, 78, 70, 90),
    ]
    
    mycursor.executemany(sql, val)
        
    mydb.commit()

main()