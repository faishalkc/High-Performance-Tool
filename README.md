 <div align="center">

<img src="https://github.com/user-attachments/assets/7385ffa2-7d74-469d-accf-9a912fc00d97" alt="High Performance Tool Icon" width="120" height="120" />

# High Performance Tool

### A Simple Windows Power Plan Utility

[![Platform](https://img.shields.io/badge/Platform-Windows-0078D4?style=for-the-badge&logo=opentofu&logoColor=white)](https://www.microsoft.com/windows)
[![Language](https://img.shields.io/badge/Language-Python-B08D35?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/faishalkc/High-Performance-Tool)

[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-B08D35?style=flat-square&logo=python&logoColor=white)](https://docs.python.org/3/library/tkinter.html)
[![Windows Power Management](https://img.shields.io/badge/Power_Management-powercfg-5C6BC0?style=flat-square&logo=windows&logoColor=white)](https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/powercfg-command-line-options)

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
- 🪟 **Native Windows Integration** — uses the built-in `powercfg` command.

## 🖥️ Application Preview

<img src="https://github.com/user-attachments/assets/c6ef3ff0-af0a-42ed-8574-1e922d6011f7" alt="High Performance Tool application interface" width="420" />

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

Clone the repository:

```bash
git clone https://github.com/faishalkc/High-Performance-Tool.git
cd High-Performance-Tool
```

Run the application:

```bash
python HPTool.py
```

Keep `banner.png` and `icon.ico` in the same directory as `HPTool.py`, as the application loads these files using relative paths.

## 🎮 How to Use

1. Launch High Performance Tool.
2. Click **Enable High Performance Mode** to activate the High Performance power plan.
3. Click **Disable High Performance Mode** to return to the Balanced power plan.
4. Close the application when finished.

## 🛠️ Technologies

- **Python** — application logic.
- **Tkinter** — graphical user interface.
- **Windows `powercfg`** — power plan management.

## ⚠️ Notes

- **Windows only:** The application uses Windows-specific functionality and is not intended for macOS or Linux.
- **Power plan availability:** The requested power plan must be available on the system.
- **Performance:** High Performance mode does not guarantee better performance in every workload and may increase power consumption.
- **Command feedback:** The current version does not display success or error notifications after a power plan change.

## 📦 Releases

Download the latest Windows version from the [GitHub Releases](https://github.com/faishalkc/High-Performance-Tool/releases) page.

## 📄 License

No license information is currently specified in this repository. Unless a license is added, the default copyright rules apply.
