<div align="center">

<img src="https://github.com/user-attachments/assets/7385ffa2-7d74-469d-accf-9a912fc00d97" alt="High Performance Tool Icon" width="120" height="120" />

# High Performance Tool

### A Simple Windows Power Plan Utility

![Platform](https://img.shields.io/badge/Platform-Windows-0078D4?style=flat-square&logo=opentofu&logoColor=white)
![Language](https://img.shields.io/badge/Language-Python-B08D35?style=flat-square&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-2E8B57?style=flat-square&logo=python&logoColor=white)
![Windows Power Management](https://img.shields.io/badge/Power_Management-powercfg-5C6BC0?style=flat-square&logo=square&logoColor=white)
![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=flat-square&logo=github&logoColor=white)

**Switch between Windows power plans with just one click.**

A lightweight desktop utility for quickly switching between the High Performance and Balanced power plans through a simple graphical interface.

</div>

---

## 📖 About

High Performance Tool is a Windows desktop application designed to make power plan switching more convenient.

Instead of navigating through Windows settings, users can switch between two power plans directly from the application:

- **High Performance** — activates the High Performance power plan.
- **Balanced** — restores the Balanced power plan.

The application uses Python, Tkinter, and Windows' built-in `powercfg` utility to perform these actions.

## ✨ Features

- ⚡ **One-Click Switching** — change power plans through simple buttons.
- 🚀 **High Performance Mode** — activate the High Performance power plan.
- ⚖️ **Balanced Mode** — switch back to the Balanced power plan.
- 🪶 **Lightweight Interface** — a simple graphical application with minimal functionality.
- 🪟 **Native Windows Integration** — uses the built-in `powercfg` command and follows the Windows system font.
- 🖼️ **Display Scaling Support** — DPI-aware, sharp on high-resolution screens, with a single `SCALE` setting to resize the whole interface.
- 🎯 **Centered Window** — opens in the center of the desktop work area, above the taskbar.

## 🖥️ Application Preview

<img src="https://github.com/user-attachments/assets/c6ef3ff0-af0a-42ed-8574-1e922d6011f7" alt="High Performance Tool application interface" width="420" />

## 📂 Project Structure

```text
High-Performance-Tool/
├── HPTool.py
├── banner.png
├── icon.ico
├── requirements.txt
├── .gitignore
└── README.md
```

| File | Description |
|---|---|
| `HPTool.py` | Main Python script containing the application window and power plan switching functionality. |
| `banner.png` | Banner image displayed at the top of the application window. |
| `icon.ico` | Application window icon. |
| `requirements.txt` | List of third-party Python dependencies. |
| `.gitignore` | Specifies files and directories that Git should ignore, such as Python cache files and virtual environments. |
| `README.md` | Project documentation, including installation instructions and usage information. |

## 🚀 Getting Started

### Windows Executable

1. Visit the [GitHub Releases](https://github.com/faishalkc/High-Performance-Tool/releases) page.
2. Download the Windows release package.
3. Extract the downloaded archive.
4. Double-click **`HPTool.exe`** to launch the application.

### Running from Source

**Requirements:**
- Microsoft Windows
- Python 3 with Tkinter available
- Pillow (dependencies listed in `requirements.txt`)

Clone the repository:

```bash
git clone https://github.com/faishalkc/High-Performance-Tool.git
cd High-Performance-Tool
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python HPTool.py
```

Keep `banner.png` and `icon.ico` in the same directory as `HPTool.py`. The application locates these files relative to the script, so it can be launched from any working directory.

## 🎮 How to Use

1. Launch High Performance Tool.
2. Click **Enable High Performance Mode** to activate the High Performance power plan.
3. Click **Disable High Performance Mode** to return to the Balanced power plan.
4. Close the application when finished.

## 🛠️ Technologies

- **Python** — application logic.
- **Tkinter** — graphical user interface.
- **Pillow** — banner image loading and scaling.
- **ctypes** — Windows API access for DPI awareness and desktop work area.
- **Windows `powercfg`** — power plan management.

## ⚠️ Notes

- **Windows only:** The application uses Windows-specific functionality and is not intended for macOS or Linux.
- **Power plan availability:** The requested power plan must be available on the system.
- **Performance:** High Performance mode does not guarantee better performance in every workload and may increase power consumption.
- **Command feedback:** The current version does not display success or error notifications after a power plan change.

## 📄 License

This project is licensed under the [MIT License](LICENSE.md).

You are free to use, modify, and distribute this software in accordance with the terms of the license.
