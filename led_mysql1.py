import mysql.connector
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

while end == 0:

    mydb = mysql.connector.connect (
        host="localhost",
        user="root",
        passwd="",
        database=""
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT status FROM raspi WHERE gpio_id = 11")

    result = cursor.fetchall()

    for row in result:

        if row[0] == 0:
                #print("aus")
                GPIO.output(11,0)
        elif row[0] == 1:
                #print("ein")
                GPIO.output(11,1)
        elif row[0] == 2:
                #print("fertig")
                end = 1
        else:
                print("fehler")
                time.sleep(2)

GPIO.cleanup()