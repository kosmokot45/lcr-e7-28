import tkinter as tk
from tkinter import messagebox, PhotoImage
import serial
import struct
import time


class ImpedanceMeterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Impedance Meter Control E7-28")
        self.master.iconphoto(False, PhotoImage(file="static/vsu_gerb.png"))

        # Настройки последовательного порта
        self.port = "COM3"  # Замените на ваш порт
        self.baudrate = 9600
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
        except Exception:
            print(f"Couldnt connect {self.port}")
        # Создание интерфейса
        self.create_widgets()

    def create_widgets(self):
        # Кнопка для получения имени прибора
        self.get_name_button = tk.Button(self.master, text="Get Device Name", command=self.get_device_name)
        self.get_name_button.pack(pady=10)

        # Кнопка для включения АВП
        self.enable_avp_button = tk.Button(self.master, text="Enable AVP", command=self.enable_avp)
        self.enable_avp_button.pack(pady=10)

        # Кнопка для установки частоты
        self.set_frequency_button = tk.Button(
            self.master, text="Set Frequency (1000 Hz)", command=lambda: self.set_frequency(1000)
        )
        self.set_frequency_button.pack(pady=10)

        # Кнопка для получения полной информации
        self.get_info_button = tk.Button(self.master, text="Get Full Info", command=self.get_full_info)
        self.get_info_button.pack(pady=10)

        # Текстовое поле для отображения ответа
        self.response_text = tk.Text(self.master, height=10, width=50)
        self.response_text.pack(pady=10)

    def send_command(self, command, *args):
        cmd = bytearray([0xAA, command])
        for arg in args:
            cmd.extend(arg)
        self.ser.write(cmd)
        time.sleep(0.1)
        response = self.ser.read(100)
        return response

    def get_device_name(self):
        response = self.send_command(64)
        print(self.send_command(64))
        self.display_response(response)

    def enable_avp(self):
        response = self.send_command(65)
        self.display_response(response)

    def set_frequency(self, frequency):
        frequency_bytes = struct.pack(">I", frequency)
        response = self.send_command(
            67, frequency_bytes[0:1], frequency_bytes[1:2], frequency_bytes[2:3], frequency_bytes[3:4]
        )
        self.display_response(response)

    def get_full_info(self):
        response = self.send_command(72, b"\x00")
        self.parse_response(response)

    def parse_response(self, response):
        if len(response) < 20:
            messagebox.showerror("Error", "Response is too short")
            return

        flags = response[2]
        mode = response[3]
        slow = response[4]
        diap = response[5]
        Uсм1 = struct.unpack(">H", response[6:8])[0] / 10.0
        Uсм0 = struct.unpack(">H", response[8:10])[0] / 10.0
        frequency = struct.unpack(">I", response[10:14])[0]
        Z = struct.unpack(">f", response[14:18])[0]
        phase_angle = struct.unpack(">f", response[18:22])[0]

        result = (
            f"Flags: {bin(flags)}\n"
            f"Mode: {mode}\n"
            f"Slow: {slow}\n"
            f"Diap: {diap}\n"
            f"Uсм1: {Uсм1}\n"
            f"Uсм0: {Uсм0}\n"
            f"Frequency: {frequency}\n"
            f"Impedance (Z): {Z}\n"
            f"Phase Angle (Radians): {phase_angle}\n"
            f"Phase Angle (Degrees): {phase_angle * 57.2957795}\n"
        )
        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(tk.END, result)

    def display_response(self, response):
        # Отображение ответа в текстовом поле
        self.response_text.delete(1.0, tk.END)  # Очистка текстового поля
        self.response_text.insert(tk.END, response.hex())  # Отображение ответа в шестнадцатеричном формате

    def close(self):
        try:
            self.ser.close()  # Закрытие последовательного порта
        except Exception as e:
            print(e)
        self.master.destroy()  # Закрытие окна приложения


root = tk.Tk()
root.geometry("500x500+1000+500")
root.minsize(500, 500)  # минимальные размеры: ширина - 200, высота - 150
root.maxsize(1000, 1000)  # максимальные размеры: ширина - 400, высота - 300
app = ImpedanceMeterApp(root)

# Обработка закрытия окна
root.protocol("WM_DELETE_WINDOW", app.close)
root.mainloop()
