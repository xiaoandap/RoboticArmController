import serial
def qianyi():
    ser = serial.Serial()
    ser.port='com4'
    ser.baudrate=9600
    ser.bytesize=8
    ser.stopbits=1
    ser.parity="N"
    ser.open()
    ser.write(bytearray([0x55]))
    ser.write(bytearray([0x55]))
    ser.write(bytearray([0x08]))
    ser.write(bytearray([0x03]))
    ser.write(bytearray([0x01]))
    ser.write(bytearray([0xE8]))
    ser.write(bytearray([0x03]))
    ser.write(bytearray([0x02]))
    ser.write(bytearray([0xD0]))
    ser.write(bytearray([0x07]))
    if(ser.isOpen()):
        print("succeed！")
    else:
        print("failed")
qianyi():