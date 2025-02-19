from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QFileDialog, QApplication
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QKeyEvent
from text_display import ScrollableTextEdit
from control_panel import ControlPanel
from theme import Theme

class TeleprompterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_variables()
        self.init_ui()
        self.setup_shortcuts()
        self.apply_theme()
        # Maximize window
        self.showMaximized()

    def init_variables(self):
        self.is_playing = False
        self.base_scroll_speed = 50
        self.scroll_amount = 1
        self.scroll_timer = QTimer()
        self.scroll_timer.timeout.connect(self.scroll_text)
        self.manual_scroll_step = 20

    def init_ui(self):
        self.setWindowTitle("Telepromptu")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        self.text_display = ScrollableTextEdit()
        self.control_panel = ControlPanel()
        self.connect_signals()
        
        layout.addWidget(self.control_panel)
        layout.addWidget(self.text_display)

    def connect_signals(self):
        self.control_panel.play_clicked.connect(self.toggle_play)
        self.control_panel.load_clicked.connect(self.load_text)
        self.control_panel.speed_changed.connect(self.update_speed)
        self.control_panel.font_size_changed.connect(self.update_font_size)
        self.control_panel.font_family_changed.connect(self.update_font_family)
        self.control_panel.alignment_changed.connect(self.update_alignment)
        self.control_panel.reset_clicked.connect(self.reset_text)

    def setup_shortcuts(self):
        self.shortcuts = {
            Qt.Key.Key_Space: self.toggle_play,
            Qt.Key.Key_Left: lambda: self.adjust_speed(-5),
            Qt.Key.Key_Right: lambda: self.adjust_speed(5),
            Qt.Key.Key_Up: self.scroll_up,
            Qt.Key.Key_Down: self.scroll_down,
            Qt.Key.Key_PageUp: lambda: self.adjust_font_size(2),
            Qt.Key.Key_PageDown: lambda: self.adjust_font_size(-2),
            Qt.Key.Key_R: self.reset_text,
            Qt.Key.Key_Home: self.scroll_to_top,
            Qt.Key.Key_End: self.scroll_to_bottom
        }

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() in self.shortcuts:
            self.shortcuts[event.key()]()
        else:
            super().keyPressEvent(event)

    def toggle_play(self):
        self.is_playing = not self.is_playing
        self.control_panel.update_play_button_state(self.is_playing, self.style())
        
        if self.is_playing:
            scrollbar = self.text_display.verticalScrollBar()
            if scrollbar.value() >= scrollbar.maximum():
                self.is_playing = False
                self.control_panel.update_play_button_state(False, self.style())
                return
            self.scroll_timer.start(self.base_scroll_speed)
        else:
            self.scroll_timer.stop()

    def scroll_text(self):
        scrollbar = self.text_display.verticalScrollBar()
        if scrollbar.value() >= scrollbar.maximum():
            self.is_playing = False
            self.control_panel.update_play_button_state(False, self.style())
            self.scroll_timer.stop()
        else:
            scrollbar.setValue(scrollbar.value() + self.scroll_amount)
            self.update_progress()

    def scroll_up(self):
        scrollbar = self.text_display.verticalScrollBar()
        new_value = max(0, scrollbar.value() - self.manual_scroll_step)
        scrollbar.setValue(new_value)
        self.update_progress()

    def scroll_down(self):
        scrollbar = self.text_display.verticalScrollBar()
        new_value = min(scrollbar.maximum(), scrollbar.value() + self.manual_scroll_step)
        scrollbar.setValue(new_value)
        self.update_progress()

    def reset_text(self):
        self.is_playing = False
        self.control_panel.update_play_button_state(False, self.style())
        self.scroll_timer.stop()
        self.scroll_to_top()
        self.update_progress()
        self.control_panel.play_button.setFocus()

    def update_speed(self, value):
        self.base_scroll_speed = int(110 - value)
        if self.is_playing:
            self.scroll_timer.setInterval(self.base_scroll_speed)

    def adjust_speed(self, delta):
        current_speed = self.control_panel.speed_slider.value()
        new_speed = max(10, min(100, current_speed + delta))
        self.control_panel.speed_slider.setValue(new_speed)

    def update_font_size(self, size):
        self.text_display.setFont(QFont(self.text_display.font().family(), size))

    def adjust_font_size(self, delta):
        current_size = self.control_panel.font_size_spin.value()
        new_size = max(12, min(72, current_size + delta))
        self.control_panel.font_size_spin.setValue(new_size)

    def update_font_family(self, family):
        self.text_display.setFont(QFont(family, self.text_display.font().pointSize()))

    def update_alignment(self, alignment):
        self.text_display.set_alignment(alignment)

    def scroll_to_top(self):
        self.text_display.verticalScrollBar().setValue(0)

    def scroll_to_bottom(self):
        self.text_display.verticalScrollBar().setValue(
            self.text_display.verticalScrollBar().maximum()
        )

    def update_progress(self):
        scrollbar = self.text_display.verticalScrollBar()
        if scrollbar.maximum() > 0:
            progress = int((scrollbar.value() / scrollbar.maximum()) * 100)
            total_lines = self.text_display.get_line_count()
            current_line = int((total_lines * progress) / 100)
            self.control_panel.update_progress(current_line, total_lines)

    def load_text(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open Text File",
            "",
            "Text Files (*.txt);;All Files (*)"
        )
        if file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read()
                self.text_display.setText(text)
                self.is_playing = False
                self.control_panel.update_play_button_state(False, self.style())
                self.scroll_timer.stop()
                self.scroll_to_top()
                self.update_progress()
                self.control_panel.play_button.setFocus()

    def apply_theme(self):
        QApplication.instance().setPalette(Theme.get_dark_palette())
        self.setStyleSheet(Theme.get_stylesheet())