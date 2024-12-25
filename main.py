import sys
import serial
import struct
import time
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_main import Ui_MainWindow
from client_faker.client_faker import FakerClient


class ImpedanceMeterApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # FakerClient

        self.faker = FakerClient()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Изначально серийный порт не инициализирован
        self.ser = None

        # Состояние подключения
        self.connection_status = False

        # Подключение кнопок к методам
        self.ui.connection_button.clicked.connect(self.connect_to_port)
        # self.ui.mode_button.clicked.connect(self.set_mode)
        self.ui.get_name_button.clicked.connect(self.get_device_name)
        self.ui.enable_avp_button.clicked.connect(self.enable_avp)
        self.ui.set_frequency_button.clicked.connect(lambda: self.set_frequency(1000))
        self.ui.get_info_button.clicked.connect(self.get_full_info)

    def connect_to_port(self):
        # self.connection_status = False
        selected_port = self.ui.combo_com_port.currentText()
        # if not self.connection_status:
        #     self.ui.connection_button.setText("Connect")
        #     self.connection_status = True
        # else:
        #     self.ui.connection_button.setText("Disconect")
        #     self.connection_status = False
        print(selected_port, self.faker.connection)
        # # self.port = "COM3"  # Замените на ваш порт
        self.baudrate = 9600
        try:
            # Будет
            # self.ser = serial.Serial(selected_port, self.baudrate, timeout=1)
            # Пока фейк

            if not self.faker.connection:
                # serial
                self.faker.connection = True
                self.ser = serial.Serial(selected_port, self.baudrate, timeout=1)
                # soft
                self.connection_status = True
                QMessageBox.information(self, "Success", f"Connected to {selected_port}")
                self.ui.connection_button.setText("Disconect")
            else:
                # serial
                self.faker.connection = False
                if self.ser is not None and self.ser.is_open:
                    try:
                        self.ser.close()  # Закрытие последовательного порта
                    except Exception as e:
                        print(f"Error closing serial port: {e}")
                # soft
                self.connection_status = False
                QMessageBox.information(self, "Success", f"Disconnect to {selected_port}")
                self.ui.connection_button.setText("Connect")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Couldn't connect to {selected_port}: {str(e)}")

    def send_command(self, command, *args):
        if self.ser is None or not self.ser.is_open:
            QMessageBox.warning(self, "Warning", "Serial port is not connected.")
            return
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
            QMessageBox.critical(self, "Error", "Response is too short")
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
        self.ui.response_text.setPlainText(result)

    def display_response(self, response):
        try:
            self.ui.response_text.setPlainText(response.hex())
        except Exception:
            self.ui.response_text.setPlainText("Error displaying response")

    def closeEvent(self, event):
        if self.ser is not None and self.ser.is_open:
            try:
                self.ser.close()  # Закрытие последовательного порта
            except Exception as e:
                print(f"Error closing serial port: {e}")
        event.accept()  # Принять событие закрытия


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImpedanceMeterApp()
    window.show()
    sys.exit(app.exec())
