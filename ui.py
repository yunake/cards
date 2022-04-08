import sys

from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtCore import Signal, Slot, QSize
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6.QtWidgets import QPushButton, QTabWidget, QLabel
from PySide6.QtGui import QColorSpace, QPixmap, QImageReader


from __feature__ import snake_case
from __feature__ import true_property

from people import people

from evdev import InputDevice, ecodes, list_devices
from select import select

keys = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"
dev = InputDevice("/dev/input/by-id/usb-Sycreader_RFID_Technology_Co.__Ltd_SYC_ID_IC_USB_Reader_08FF20140315-event-kbd")


class MainWindow(QMainWindow):
    code_signal = Signal(str)

    def __init__(self):
        super().__init__()
        #self.window_title = "My App"
        #button = QPushButton("Press Me!")
        # button = QTabWidget()
        # for n, color in enumerate(["red", "green", "blue", "yellow"]):
        #     button.add_tab(QLabel(color), color)
        #button.set_fixed_size(QSize(700, 700))
        #self.fixed_size = QSize(200, 600)
        #self.set_central_widget(button)
        # TODO: update image when we read a card
        # TODO: resize image to fit the screen
        self._photo_label = QLabel()
        self.set_central_widget(self._photo_label)
        self.w = self.screen().available_geometry.width()
        self.h = self.screen().available_geometry.height()
        self.set_fixed_size(self.w, self.h)
        self.code_signal.connect(self.set_photo)

    def read_code(self):
        barcode = ""
        while True:
            r,w,x = select([dev], [], [])

            for event in dev.read():
                if event.type != 1 or event.value != 1:
                    continue
                if event.code == 28:
                    self.code_signal.emit(people[barcode]['photo'])
                    #self.set_photo(people[barcode]['photo'])
                    barcode = ""
                    break
                barcode += keys[event.code]

    def set_photo(self, filename):
        reader = QImageReader(filename)
        reader.set_auto_transform(True)
        self._photo = reader.read()
        if self._photo.color_space().is_valid():
            self._photo.convert_to_color_space(QColorSpace.SRgb)
        p = QPixmap.from_image(self._photo)
        print(p.size())
        self._photo_label.set_pixmap(p)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

import threading
t = threading.Thread(target=window.read_code)
t.start()
#window.set_photo(people['1733444945']['photo'])

sys.exit(app.exec())
