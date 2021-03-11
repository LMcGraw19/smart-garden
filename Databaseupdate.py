import mysql.connector

def main():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Smartgarden",
      database="SmartGarden"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO Air_Temperature (time, temp, humidity) VALUES (%s, %s, %s)"
    val = [
      ('3.30pm', -15, 10),
      ('4pm', 10, 12),
      ('4.30pm', -12, 50),
      ('5pm', 14, 40),
      ('5.30pm', 19, 100),
    ]
    
    mycursor.executemany(sql, val)
        
    mydb.commit()

main()