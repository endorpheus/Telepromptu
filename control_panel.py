from PyQt6.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QPushButton, 
                            QSlider, QLabel, QSpinBox, QComboBox, QProgressBar)
from PyQt6.QtCore import Qt, pyqtSignal

class ControlPanel(QWidget):
    # Define signals
    speed_changed = pyqtSignal(int)
    font_size_changed = pyqtSignal(int)
    font_family_changed = pyqtSignal(str)
    alignment_changed = pyqtSignal(Qt.AlignmentFlag)
    play_clicked = pyqtSignal()
    load_clicked = pyqtSignal()
    reset_clicked = pyqtSignal()
    
    def __init__(self, initial_speed=10, initial_font_size=64):
        super().__init__()
        self.setup_ui(initial_speed, initial_font_size)
        # Set initial play button state
        self.update_play_button_state(False, self.style())
    
    def setup_ui(self, initial_speed, initial_font_size):
        # Main layout will be vertical to stack control rows
        main_layout = QVBoxLayout(self)
        
        # First row: Basic controls
        basic_controls = QHBoxLayout()
        
        # Play button
        self.play_button = QPushButton()
        self.play_button.setMinimumWidth(40)
        self.play_button.setToolTip("Play/Pause (Space)")
        self.play_button.clicked.connect(self.play_clicked.emit)
        
        # Reset button
        self.reset_button = QPushButton()
        self.reset_button.setIcon(self.style().standardIcon(
            self.style().StandardPixmap.SP_MediaSkipBackward
        ))
        self.reset_button.setToolTip("Reset to Beginning (R)")
        self.reset_button.setMinimumWidth(40)
        self.reset_button.clicked.connect(self.reset_clicked.emit)
        
        # Load button
        self.load_button = QPushButton("Load Text")
        self.load_button.clicked.connect(self.load_clicked.emit)
        
        # Speed controls
        speed_label = QLabel("Speed:")
        self.speed_slider = QSlider(Qt.Orientation.Horizontal)
        self.speed_slider.setRange(10, 100)
        self.speed_slider.setValue(initial_speed)
        self.speed_slider.setToolTip("Adjust Speed (Left/Right Arrow)")
        self.speed_slider.valueChanged.connect(self.speed_changed.emit)
        
        # Add basic controls to first row
        basic_controls.addWidget(self.play_button)
        basic_controls.addWidget(self.reset_button)
        basic_controls.addWidget(self.load_button)
        basic_controls.addWidget(speed_label)
        basic_controls.addWidget(self.speed_slider)
        
        # Second row: Text formatting controls
        format_controls = QHBoxLayout()
        
        # Font controls
        font_label = QLabel("Font:")
        self.font_combo = QComboBox()
        self.font_combo.addItems(["Arial", "Helvetica", "Times New Roman", "Courier New"])
        self.font_combo.currentTextChanged.connect(self.font_family_changed.emit)
        
        font_size_label = QLabel("Size:")
        self.font_size_spin = QSpinBox()
        self.font_size_spin.setRange(12, 72)
        self.font_size_spin.setValue(initial_font_size)
        self.font_size_spin.setToolTip("Adjust Font Size (Page Up/Down)")
        self.font_size_spin.valueChanged.connect(self.font_size_changed.emit)
        
        # Alignment controls
        align_label = QLabel("Align:")
        self.align_left = QPushButton("Left")
        self.align_center = QPushButton("Center")
        self.align_right = QPushButton("Right")
        
        self.align_left.clicked.connect(
            lambda: self.alignment_changed.emit(Qt.AlignmentFlag.AlignLeft))
        self.align_center.clicked.connect(
            lambda: self.alignment_changed.emit(Qt.AlignmentFlag.AlignCenter))
        self.align_right.clicked.connect(
            lambda: self.alignment_changed.emit(Qt.AlignmentFlag.AlignRight))
        
        # Add formatting controls to second row
        format_controls.addWidget(font_label)
        format_controls.addWidget(self.font_combo)
        format_controls.addWidget(font_size_label)
        format_controls.addWidget(self.font_size_spin)
        format_controls.addSpacing(20)
        format_controls.addWidget(align_label)
        format_controls.addWidget(self.align_left)
        format_controls.addWidget(self.align_center)
        format_controls.addWidget(self.align_right)
        format_controls.addStretch()
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setFormat("%p% - Line %v of %m")
        
        # Add all rows to main layout
        main_layout.addLayout(basic_controls)
        main_layout.addLayout(format_controls)
        main_layout.addWidget(self.progress_bar)
    
    def update_play_button_state(self, is_playing, style):
        icon = style.standardIcon(
            style.StandardPixmap.SP_MediaPause if is_playing 
            else style.StandardPixmap.SP_MediaPlay
        )
        self.play_button.setIcon(icon)
    
    def update_progress(self, current_line, total_lines):
        self.progress_bar.setMaximum(total_lines)
        self.progress_bar.setValue(current_line)