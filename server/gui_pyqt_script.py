import sys
import serial
import struct
import time
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QMessageBox


class ImpedanceMeterApp(QWidget):
    def __init__(self):
        super().__init__()

        # Настройки последовательного порта
        self.port = 'COM3'  # Замените на ваш порт
        self.baudrate = 9600
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
        except Exception:
            print(f"Couldnt connect {self.port}")

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Impedance Meter Control")

        # Создание кнопок
        self.get_name_button = QPushButton("Get Device Name", self)
        self.get_name_button.clicked.connect(self.get_device_name)

        self.enable_avp_button = QPushButton("Enable AVP", self)
        self.enable_avp_button.clicked.connect(self.enable_avp)

        self.set_frequency_button = QPushButton("Set Frequency (1000 Hz)", self)
        self.set_frequency_button.clicked.connect(lambda: self.set_frequency(1000))

        self.get_info_button = QPushButton("Get Full Info", self)
        self.get_info_button.clicked.connect(self.get_full_info)

        # Текстовое поле для отображения ответа
        self.response_text = QTextEdit(self)
        self.response_text.setReadOnly(True)

        # Установка компоновки
        layout = QVBoxLayout()
        layout.addWidget(self.get_name_button)
        layout.addWidget(self.enable_avp_button)
        layout.addWidget(self.set_frequency_button)
        layout.addWidget(self.get_info_button)
        layout.addWidget(self.response_text)

        self.setLayout(layout)

    def send_command(self, command, *args):
        try:
            cmd = bytearray([0xAA, command])
            for arg in args:
                cmd.extend(arg)
            self.ser.write(cmd)
            time.sleep(0.1)
            response = self.ser.read(100)
            return response
        except Exception as e:
            return e

    def get_device_name(self):
        response = self.send_command(64)
        self.display_response(response)

    def enable_avp(self):
        response = self.send_command(65)
        self.display_response(response)

    def set_frequency(self, frequency):
        frequency_bytes = struct.pack('>I', frequency)
        response = self.send_command(67, frequency_bytes[0:1], frequency_bytes[1:2], frequency_bytes[2:3], frequency_bytes[3:4])
        self.display_response(response)

    def get_full_info(self):
        response = self.send_command(72, b'\x00')
        self.parse_response(response)

    def parse_response(self, response):
        if len(response) < 20:
            QMessageBox.critical(self, "Error", "Response is too short")
            return

        flags = response[2]
        mode = response[3]
        slow = response[4]
        diap = response[5]
        Uсм1 = struct.unpack('>H', response[6:8])[0] / 10.0
        Uсм0 = struct.unpack('>H', response[8:10])[0] / 10.0
        frequency = struct.unpack('>I', response[10:14])[0]
        Z = struct.unpack('>f', response[14:18])[0]
        phase_angle = struct.unpack('>f', response[18:22])[0]

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
        self.response_text.setPlainText(result)

    def display_response(self, response):
        try:
            self.response_text.setPlainText(response.hex())
        except Exception:
            self.response_text.setPlainText("jopa")

    def closeEvent(self, event):
        try:
            self.ser.close()  # Закрытие последовательного порта
        except Exception as e:
            print(e)
        event.accept()  # Принять событие закрытия


app = QApplication(sys.argv)
window = ImpedanceMeterApp()
window.resize(400, 300)  # Установка размера окна
window.show()
sys.exit(app.exec())
