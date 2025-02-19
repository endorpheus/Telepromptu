#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import QApplication
from teleprompter import TeleprompterWindow

def main():
    app = QApplication(sys.argv)
    window = TeleprompterWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()