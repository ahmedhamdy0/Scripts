import serial
ser = serial.Serial('/dev/ttyACM0' , 9600 )

while True :
    x = input("Enter Input : ").encode()
    ser.write(x)
