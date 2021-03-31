import mysql.connector

def main():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Smartgarden",
      database="SmartGarden"
    )
    
    mycursor = mydb.cursor()

    #Table creation below
    mycursor.execute("CREATE TABLE BME280 (id INT AUTO_INCREMENT PRIMARY KEY, time VARCHAR(255), Temperature FLOAT, Pressure FLOAT, Altitude FLOAT, Humidity FLOAT)")
    mycursor.execute("CREATE TABLE DS18B20 (id INT AUTO_INCREMENT PRIMARY KEY, time VARCHAR(255), Temperature INT)")
    mycursor.execute("CREATE TABLE SEN0114 (id INT AUTO_INCREMENT PRIMARY KEY, time VARCHAR(255), Moisture INT)")
    mycursor.execute("CREATE TABLE SHT21 (id INT AUTO_INCREMENT PRIMARY KEY, time VARCHAR(255), Temperature INT, Humidity INT)")
    mycursor.execute("CREATE TABLE TSL2591 (id INT AUTO_INCREMENT PRIMARY KEY, time VARCHAR(255), Lumination FLOAT)")

    #Variables are set up with data to go into tables
    sql = "INSERT INTO BME280 (time, Temperature, Pressure, Altitude, Humidity) VALUES (%s, %s, %s, %s, %s)"
    val = [
      ('1pm', 15, 10, 20, 51),
      ('1.30pm', 10, 12, 45, 80),
      ('2pm', -2, 50, 50, 40),
      ('2.30pm', 14, 40, 70, 80),
      ('3pm', 19, 78, 70, 90),
    ]

    sql2 = "INSERT INTO DS18B20 (time, Temperature) VALUES (%s, %s)"
    val2 = [
      ('1pm', -15),
      ('1.30pm', -10),
      ('2pm', -12),
      ('2.30pm', -14),
      ('3pm', -19),
    ]

    sql3 = "INSERT INTO SEN0114 (time, Moisture) VALUES (%s, %s)"
    val3 = [
      ('1pm', 454),
      ('1.30pm', 200),
      ('2pm', 780),
      ('2.30pm', 500),
      ('3pm', 700),
    ]

    sql4 = "INSERT INTO SHT21 (time, Temperature, Humidity) VALUES (%s, %s, %s)"
    val4 = [
      ('1pm', 15, 75),
      ('1.30pm', 10, 80),
      ('2pm', 12, 45),
      ('2.30pm', 4, 72),
      ('3pm', 19, 30),
    ]

    sql5 = "INSERT INTO TSL2591 (time, Lumination) VALUES (%s, %s)"
    val5 = [
      ('1pm', .7),
      ('1.30pm', .6),
      ('2pm', .5),
      ('2.30pm', .8),
      ('3pm', .9),
    ]

    #variables that stored mysql commands and its assoicated data are execueted
    mycursor.executemany(sql, val)
    mycursor.executemany(sql2, val2)
    mycursor.executemany(sql3, val3)
    mycursor.executemany(sql4, val4)
    mycursor.executemany(sql5, val5)

    mydb.commit() #Statement commits changes to the mysql server

if __name__ == "__main__":
    main()
    