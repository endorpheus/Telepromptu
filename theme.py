from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

class Theme:
    @staticmethod
    def get_dark_palette():
        palette = QPalette()
        
        # Main colors
        palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
        
        # Text colors
        palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
        
        # Button colors
        palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
        
        # Highlight colors
        palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
        
        return palette
    
    @staticmethod
    def get_stylesheet():
        return """
            /* Main Window */
            QMainWindow {
                background-color: #353535;
            }
            
            /* Basic Controls */
            QPushButton {
                background-color: #2a82da;
                color: white;
                border: none;
                padding: 5px 15px;
                border-radius: 3px;
                min-width: 60px;
            }
            
            QPushButton:hover {
                background-color: #3294ea;
            }
            
            QPushButton:checked {
                background-color: #1e5b99;
            }
            
            QPushButton:focus {
                border: 1px solid #ffffff;
            }
            
            /* Sliders */
            QSlider::groove:horizontal {
                border: 1px solid #999999;
                height: 8px;
                background: #4a4a4a;
                margin: 2px 0;
                border-radius: 4px;
            }
            
            QSlider::handle:horizontal {
                background: #2a82da;
                border: 1px solid #5c5c5c;
                width: 18px;
                margin: -2px 0;
                border-radius: 9px;
            }
            
            QSlider::handle:horizontal:hover {
                background: #3294ea;
            }
            
            /* Combo Box */
            QComboBox {
                background-color: #2a82da;
                color: white;
                border: none;
                border-radius: 3px;
                padding: 5px 10px;
                min-width: 100px;
            }
            
            QComboBox::drop-down {
                border: none;
            }
            
            QComboBox::down-arrow {
                image: none;
                border: none;
            }
            
            QComboBox QAbstractItemView {
                background-color: #353535;
                color: white;
                selection-background-color: #2a82da;
            }
            
            /* Spin Box */
            QSpinBox {
                background-color: #2a82da;
                color: white;
                border: none;
                border-radius: 3px;
                padding: 5px;
                min-width: 60px;
            }
            
            QSpinBox::up-button, QSpinBox::down-button {
                background-color: #1e5b99;
                border: none;
                border-radius: 2px;
                margin: 1px;
            }
            
            QSpinBox::up-button:hover, QSpinBox::down-button:hover {
                background-color: #3294ea;
            }
            
            /* Progress Bar */
            QProgressBar {
                border: 1px solid #999999;
                border-radius: 3px;
                text-align: center;
                padding: 1px;
                background-color: #4a4a4a;
                color: white;
            }
            
            QProgressBar::chunk {
                background-color: #2a82da;
                width: 1px;
            }
            
            /* Labels */
            QLabel {
                color: white;
            }
            
            /* Text Display */
            QTextEdit {
                background-color: #000000;
                color: #ffffff;
                border: none;
                padding: 20px;
                selection-background-color: #2a82da;
                selection-color: white;
            }
            
            /* Tooltips */
            QToolTip {
                background-color: #353535;
                color: white;
                border: 1px solid #2a82da;
                border-radius: 3px;
                padding: 5px;
            }
        """