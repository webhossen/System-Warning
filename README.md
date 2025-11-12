# ⚡ Prank App – System Warning Demo

A fun and visually dynamic **Python Tkinter application** that simulates a system warning screen with flashing borders, progress effects, speech, and sound.  
Created by **Md Anayet Hossen** as a learning and demonstration project for **Tkinter UI, threading, and audio handling** in Python.

---

## 🚀 Features

- Fullscreen GUI with animated flashing border  
- Color-changing warning icon (rainbow cycle)  
- Real-time progress simulation with emoji  
- Voice announcements using `pyttsx3`  
- Beep sound effects using `winsound`  
- Multithreaded design for smooth animation  
- Safe exit shortcut (`Ctrl + 0`)

---

## 🧠 Learning Goals

This project demonstrates:
- Tkinter GUI layout & styling  
- Python multithreading  
- Sound handling in Windows  
- Text-to-speech integration  
- Event binding and UI control  

---

## 🛠️ Requirements

Install dependencies before running:

```bash
pip install pyttsx3
```

*(`winsound` is built-in on Windows)*

---

## ▶️ How to Run

1. Download or clone this repository  
2. Open a terminal in the project directory  
3. Run the script:

```bash
python "System-Warning.py"
```

4. To safely exit the demo, press:
   ```
   Ctrl + 0
   ```

---

## 🗜️ Convert Python Script to Windows `.exe`

Nice — converting a Python script into a Windows `.exe` is straightforward.  
The most common tool is **PyInstaller**.  
Below are concise, copy-pasteable commands for both **Command Prompt (cmd)** and **PowerShell**, plus helpful tips and common gotchas.

---

### ⚡ Quick Steps (Recommended)

1. Open **cmd** or **PowerShell**.  
2. *(Optional but recommended)* Create & activate a virtual environment.  
3. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
4. Build the `.exe` with PyInstaller.  
5. Find your executable inside the `dist\` folder.

---

### 🧩 Example — Basic Console Program

Assume your script is `System-Warning.py`.

#### Command Prompt:

```cmd
python -m pip install --upgrade pip
python -m pip install pyinstaller
python -m PyInstaller --onefile "System-Warning.py"
```

#### PowerShell:

```powershell
python -m pip install --upgrade pip
python -m pip install pyinstaller
python -m PyInstaller --onefile "System-Warning.py"
```

After this, the executable will be at:
```
dist\fast app.exe
```

---

### ⚙️ Common Useful PyInstaller Options

| Option | Description |
|---------|-------------|
| `--onefile` | Bundle into a single `.exe` (recommended for distribution) |
| `--windowed` / `--noconsole` | For GUI apps (no console window) |
| `--icon=app.ico` | Attach an icon (use `.ico` format) |
| `--add-data "src;dest"` | Include data files (use `;` on Windows) |
| `--hidden-import modulename` | Fix missing imports |
| `--clean` | Remove temporary build files before building |
| `--noconfirm` | Overwrite previous builds without asking |

Example with icon:
```cmd
python -m PyInstaller --onefile --windowed --icon="C:\path\to\app.ico" "System-Warning.py"
```

PowerShell note for `--add-data` quoting:
```powershell
python -m PyInstaller --onefile --add-data 'C:\path\to\data\myfile.dat;data' "System-Warning.py"
```

---

### 💡 For Apps Using Tkinter, PyQt, pandas, numpy, etc.

PyInstaller usually detects these automatically.  
If not, add manual hints:

```cmd
python -m PyInstaller --onefile --hidden-import=some_module "System-Warning.py"
```

For data files, use:
```cmd
python -m PyInstaller --onefile --add-data "assets;assets" "System-Warning.py"
```

---

### 🧰 Creating & Using a Virtual Environment (Recommended)

**Command Prompt:**
```cmd
python -m venv venv
venv\Scripts\activate
pip install pyinstaller
python -m PyInstaller --onefile "System-Warning.py"
```

**PowerShell:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install pyinstaller
python -m PyInstaller --onefile "System-Warning.py"
```

If activation is blocked:
```powershell
Set-ExecutionPolicy RemoteSigned
```
*(Run as Administrator and understand the implications before changing execution policy.)*

---

### 📦 Where to Find the Built `.exe`

After running PyInstaller:

- ✅ `dist\fast app.exe` — final executable  
- 🧩 `build\...` — build intermediates  
- ⚙️ `fast app.spec` — configuration file (editable for advanced builds)

To clean up:
```cmd
rmdir /s /q build dist
del fast app.spec
```

---

### 🧪 Testing and Distribution

- Test the `.exe` on a machine **without Python installed**  
- Some antivirus software may flag unsigned executables  
- Code sign your exe if you plan broad distribution  
- Single-file `.exe`s are larger because they bundle the Python runtime

---

### 🧯 Troubleshooting

- If your exe crashes, rebuild **without** `--windowed` to see the error:
  ```cmd
  python -m PyInstaller --onefile "System-Warning.py"
  ```
- Run from CMD to read any error messages.  
- Check missing resources (`--add-data`) or hidden imports.

---

### 🔄 Alternatives

Other tools exist (like `cx_Freeze`, `py2exe`),  
but **PyInstaller** remains the most popular and simplest for most needs.

---

## ⚠️ Disclaimer

> This app is **for educational and entertainment purposes only**.  
> It does **not actually hack, copy, or access any real data**.  
> Please use responsibly and do not distribute it to mislead others.

---

## 👨‍💻 Author

**Md Anayet Hossen**  
💼 Diploma Student in Computer Science  
---

⭐ *If you found this project helpful, please give it a star!*
