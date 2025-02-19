# Telepromptu

A simple, keyboard-controlled teleprompter application built with Python and PyQt6.

## Features
- Smooth text scrolling with adjustable speed
- Keyboard shortcuts for all controls
- Font size and family selection
- Text alignment options
- Dark theme for better readability
- Progress tracking

## Keyboard Controls
- Space: Play/Pause
- Left/Right Arrows: Adjust speed
- Up/Down Arrows: Manual scroll
- Page Up/Down: Adjust font size
- R: Reset to top
- Home/End: Jump to top/bottom

## Installation

### System Requirements
- Python 3.8 or higher
- On Linux: `sudo apt-get install python3-pyqt6` (or equivalent for your distribution)
- On Windows: No additional system requirements
- On macOS: No additional system requirements

### Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/telepromptu.git
cd telepromptu
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

## Running the Application
```bash
python main.py
```

## Troubleshooting
If you encounter any PyQt6 installation issues on Linux, make sure you have the appropriate system-level Qt dependencies installed.