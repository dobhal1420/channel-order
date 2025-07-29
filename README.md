# PyQt5 Hello World App

This is a simple cross-platform desktop application built with PyQt5 that displays "Hello, World!".

## 📦 Requirements
- Python 3.8+
- pip

## 📥 Installation
1. Clone or unzip this project.
2. Navigate to the project directory.
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   On Windows:
   ```
   venv\Scripts\activate
   ```
   On macOS/Linux:
   ```
   source venv/bin/activate
   ```
5. Install dependencies
   ```
   pip install -r requirements.txt
   ```
6. Only if you installed new dependencies don't forget to add it to requirement.txt
   ```
   pip freeze > requirements.txt
   ```


## 🚀 Run the App
Navigate to the `src` folder and run:
   python app.py

## Run the tests
Navigate to the `src` folder and run:
   python -m unittest discover -s tests

## 🛠 Packaging with PyInstaller
Install PyInstaller:
   pip install pyinstaller

Create a standalone executable:
   pyinstaller --onefile --windowed src/app.py

The executable will be in the `dist` folder.

## 🖥 Compatibility
This app works on both Windows and macOS.
