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
    mycursor.execute("CREATE TABLE Air_Temperature (id INT AUTO_INCREMENT PRIMARY KEY, time VARCHAR(255), temp INT, humidity INT)")
    mycursor.execute("CREATE TABLE Soil_Temperture (id INT AUTO_INCREMENT PRIMARY KEY, time VARCHAR(255), temp INT, moisture INT)")
    mycursor.execute("CREATE TABLE Light_Indensity (id INT AUTO_INCREMENT PRIMARY KEY, time VARCHAR(255), reading VARCHAR(255))")
    mycursor.execute("CREATE TABLE Wind_Speed_and_direction (id INT AUTO_INCREMENT PRIMARY KEY, time VARCHAR(255), speed VARCHAR(255), direction VARCHAR(255))")
    mycursor.execute("CREATE TABLE Rainfall (id INT AUTO_INCREMENT PRIMARY KEY, time VARCHAR(255), reading VARCHAR(255))")

    #Variables are set up with data to go into tables
    sql = "INSERT INTO Air_Temperature (time, temp, humidity) VALUES (%s, %s, %s)"
    val = [
      ('1pm', -15, 10),
      ('1.30pm', -10, 12),
      ('2pm', -12, 50),
      ('2.30pm', -14, 40),
      ('3pm', -19, 78),
    ]

    sql2 = "INSERT INTO Soil_Temperture (time, temp, moisture) VALUES (%s, %s, %s)"
    val2 = [
      ('1pm', -15, 10),
      ('1.30pm', -10, 12),
      ('2pm', -12, 50),
      ('2.30pm', -14, 40),
      ('3pm', -19, 78),
    ]

    sql3 = "INSERT INTO Light_Indensity (time, reading) VALUES (%s, %s)"
    val3 = [
      ('1pm', 'cloudy'),
      ('1.30pm', 'still cloudy'),
      ('2pm', "it's Edinburgh'"),
      ('2.30pm', 'Summer time'),
      ('3pm', 'and back to winter'),
    ]

    sql4 = "INSERT INTO Wind_Speed_and_direction (time, speed, direction) VALUES (%s, %s, %s)"
    val4 = [
      ('1pm', '25mph', 'West'),
      ('1.30pm', '150mph', 'North'),
      ('2pm', '10mph', 'East'),
      ('2.30pm', '5mph', 'South'),
      ('3pm', '189mph', 'West'),
    ]

    sql5 = "INSERT INTO Rainfall (time, reading) VALUES (%s, %s)"
    val5 = [
      ('1pm', '10mm'),
      ('1.30pm', '5mm'),
      ('2pm', '15mm'),
      ('2.30pm', '9mm'),
      ('3pm', '78mm'),
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
    