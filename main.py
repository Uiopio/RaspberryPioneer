
import serial

if __name__ == '__main__':
    ser = serial.Serial('/dev/serial0', 57600, timeout=1)
    ser.flush()

    while True:
        if ser.in_waiting > 0:
            line = ser.readline()
            for i in range(len(line)):
                print((line[i]))

