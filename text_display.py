from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QWheelEvent, QTextCursor, QTextBlockFormat

class ScrollableTextEdit(QTextEdit):
    def __init__(self, font_size=64, font_family="Arial"):
        super().__init__()
        self.setup_display(font_size, font_family)
        self.wheel_scroll_speed = 2  # Pixels per wheel step
        self.initial_style = """
            QTextEdit {
                background-color: #000000;
                color: #ffffff;
                border: none;
                padding: 20px;
            }
        """
        self.setStyleSheet(self.initial_style)
        
    def setup_display(self, font_size, font_family):
        self.setReadOnly(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setFont(QFont(font_family, font_size))
        self.setPlaceholderText("Load a text file to begin...")
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        # Set default center alignment
        self.set_alignment(Qt.AlignmentFlag.AlignCenter)
    
    def get_line_count(self):
        return len(self.toPlainText().splitlines())
    
    def wheelEvent(self, event: QWheelEvent):
        delta = event.angleDelta().y()
        scrollbar = self.verticalScrollBar()
        new_value = scrollbar.value() - (delta / 120 * self.wheel_scroll_speed)
        new_value = max(0, min(new_value, scrollbar.maximum()))
        scrollbar.setValue(int(new_value))
        event.accept()
        
    def setText(self, text):
        super().setText(text)
        # Reapply current alignment to all text
        self.set_alignment(self.alignment())
        
    def set_alignment(self, alignment):
        # Create text block format with desired alignment
        text_block_format = QTextBlockFormat()
        text_block_format.setAlignment(alignment)
        
        # Create cursor and select all text
        cursor = self.textCursor()
        cursor.select(QTextCursor.SelectionType.Document)
        
        # Apply the formatting
        cursor.mergeBlockFormat(text_block_format)
        
        # Clear selection and update cursor
        cursor.clearSelection()
        self.setTextCursor(cursor)