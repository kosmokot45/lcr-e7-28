import pprint
import serial
import struct
import time


port = "COM3"
baudrate = 9600
read_buff_size = 100

# open serial port
ser = serial.Serial(port, baudrate, timeout=1)


def send_command(command, *args):
    cmd = bytearray([0xAA, command])
    for arg in args:
        cmd.extend(arg)
    ser.write(cmd)
    time.sleep(0.1)
    response = ser.read(read_buff_size)
    return response


def parse_response(response):
    if len(response) < 20:
        print("Response is too short")
        return

    # Разбор данных
    flags = response[2]
    mode = response[3]
    slow = response[4]
    diap = response[5]
    Uсм1 = struct.unpack(">H", response[6:8])[0]  # 2 байта в int16
    Uсм0 = struct.unpack(">H", response[8:10])[0]  # 2 байта в int16
    frequency = struct.unpack(">I", response[10:14])[0]  # 4 байта в int32
    Z = struct.unpack(">f", response[14:18])[0]  # 4 байта в float
    phase_angle = struct.unpack(">f", response[18:22])[0]  # 4 байта в float

    # Вывод результатов
    print("Flags:", bin(flags))
    print("Mode:", mode)
    print("Slow:", slow)
    print("Diap:", diap)
    print("Uсм1:", Uсм1 / 10.0)  # Преобразование в действительное значение
    print("Uсм0:", Uсм0 / 10.0)  # Преобразование в действительное значение
    print("Frequency:", frequency)
    print("Impedance (Z):", Z)
    print("Phase Angle (Radians):", phase_angle)
    print("Phase Angle (Degrees):", phase_angle * 57.2957795)  # Преобразование в градусы


try:
    # lcr name
    response = send_command(64)
    print("Response:", response)

    # turn on avp
    response = send_command(65)
    print("Response:", response)

    # set freq
    freq = int(1000)
    freq_bytes = struct.pack(">I", freq)  # pack to 4 bytes
    response = send_command(67, freq_bytes[0:1], freq_bytes[1:2], freq_bytes[2:3], freq_bytes[3:4])
    print("Response:", response)

    # set offset
    offset = int(50)
    offset_bytes = struct.pack(">H", offset)  # pack to 2 bytes
    response = send_command(67, offset_bytes[0:1], offset_bytes[1:2], offset_bytes[2:3])
    print("Response:", response)

    # info
    response = send_command(72, "b'\x00")
    print("Response:", response)

    # reset
    response = send_command(71)
    print("Response:", response)

finally:
    # close serial port
    ser.close()
