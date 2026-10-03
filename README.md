 <div align="center">

<img src="https://github.com/user-attachments/assets/7385ffa2-7d74-469d-accf-9a912fc00d97" alt="High Performance Tool Icon" width="120" height="120" />

# High Performance Tool

### A Simple Windows Power Plan Utility

[![Platform](https://img.shields.io/badge/Platform-Windows-0078D4?style=for-the-badge\&logo=windows\&logoColor=white)](https://www.microsoft.com/windows)
[![Language](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![GUI](https://img.shields.io/badge/GUI-Tkinter-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://docs.python.org/3/library/tkinter.html)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/faishalkc/High-Performance-Tool)

**Switch between Windows power plans with a simple graphical interface.**

A lightweight desktop utility for enabling High Performance Mode or returning to the Balanced power plan without manually navigating through Windows power settings.

</div>

---

## 📖 About

High Performance Tool is a simple Windows application developed to make switching power plans more convenient.

Windows provides different power plans that influence how the system manages power consumption and performance. However, accessing these settings can require navigating through several system menus.

This utility provides a straightforward alternative through a small graphical interface with two buttons:

* **Enable High Performance Mode** — activates the Windows High Performance power plan.
* **Disable High Performance Mode** — switches back to the Balanced power plan.

The application uses Python and Tkinter for its graphical interface and the built-in Windows `powercfg` command-line utility to change the active power plan.

Originally created as a simple personal utility, High Performance Tool focuses on one task: making power plan switching quick and accessible.

## ✨ Features

* ⚡ **One-Click Power Plan Switching** — activate High Performance Mode directly from the application.
* 🔄 **Restore Balanced Mode** — switch back to the Balanced power plan whenever needed.
* 🖥️ **Simple Graphical Interface** — perform both actions without manually entering commands.
* 🪶 **Lightweight Application** — a small Python program with a straightforward interface.
* 🛠️ **Native Windows Integration** — uses the Windows `powercfg` utility instead of implementing a separate power management system.
* 🎯 **Focused Functionality** — designed specifically for switching between two power plans.

## 🖥️ Application Preview

<img src="https://github.com/user-attachments/assets/c6ef3ff0-af0a-42ed-8574-1e922d6011f7" alt="High Performance Tool application interface" width="420" />

## ⚙️ How It Works

High Performance Tool relies on the `powercfg` command provided by Windows.

When a button is clicked, the application executes the corresponding command to change the active power plan.

| Action                        | Command                                                        | Purpose                                                    |
| :---------------------------- | :------------------------------------------------------------- | :--------------------------------------------------------- |
| Enable High Performance Mode  | `powercfg /s SCHEME_MIN`                                       | Activates the High Performance power scheme alias.         |
| Disable High Performance Mode | `powercfg.exe /setactive 381b4222-f694-41f0-9685-ff5bb260df2e` | Activates the Balanced power plan using its standard GUID. |

The application does not implement its own CPU or GPU optimization algorithm. Instead, it changes the active Windows power plan, allowing Windows to apply the settings associated with that plan.

**Note:** Actual performance and power consumption depend on the hardware, Windows configuration, available power plans, and workload. Selecting High Performance Mode does not guarantee higher performance in every situation.

## 📋 Requirements

Before running the application, ensure that your system meets the following requirements:

* **Operating System:** Microsoft Windows.
* **Python:** Python 3 with Tkinter available, if running from source.
* **System Utility:** The Windows `powercfg` command.
* **Project Assets:** The application icon and banner image must be available at the paths expected by the script.

The application uses Tkinter, which is commonly included with standard Python installations for Windows.

## 🚀 Getting Started

### 1. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/faishalkc/High-Performance-Tool.git
```

### 2. Enter the Project Directory

```bash
cd High-Performance-Tool
```

### 3. Check the Project Files

Ensure the Python script and its required visual assets are present:

```text
High-Performance-Tool/
├── HPTool.py
├── banner.png
├── icon.ico
└── README.md
```

The Python script references `banner.png` and `icon.ico` using relative paths. Keep these files in the expected location when launching the application.

### 4. Run the Application

```bash
python HPTool.py
```

If your system uses the Python launcher, you can also try:

```bash
py HPTool.py
```

The application window should open with two buttons for switching power plans.

## 🎮 How to Use

| Button                            | Action                                     |
| :-------------------------------- | :----------------------------------------- |
| **Enable High Performance Mode**  | Activates the High Performance power plan. |
| **Disable High Performance Mode** | Returns to the Balanced power plan.        |

1. Launch High Performance Tool.
2. Click **Enable High Performance Mode** when you want to activate the High Performance power plan.
3. Click **Disable High Performance Mode** when you want to return to the Balanced power plan.
4. Close the application when you are finished.

The application does not currently display the active power plan or provide a confirmation message after a button is clicked.

## 📂 Project Structure

```text
High-Performance-Tool/
├── HPTool.py     # Application logic and Tkinter interface
├── banner.png    # Application banner
├── icon.ico      # Window icon
└── README.md     # Project documentation
```

## 🛠️ Technologies

| Technology                                                                                                          | Purpose                                    |
| :------------------------------------------------------------------------------------------------------------------ | :----------------------------------------- |
| **Python**                                                                                                          | Application logic and command execution.   |
| **Tkinter**                                                                                                         | Desktop graphical user interface.          |
| **powercfg (Windows)**                                                                                              | Native utility for managing power schemes. |

## ⚠️ Notes and Limitations

* **Windows only:** The application depends on Windows-specific commands and is not intended for macOS or Linux.
* **Available power plans:** The requested power scheme must be available and supported by the Windows installation.
* **Performance expectations:** High Performance Mode changes the active power plan; it does not guarantee a measurable improvement in every application.
* **Power consumption:** A performance-oriented power plan may increase energy consumption or heat generation, depending on the system and workload.
* **Command feedback:** The current implementation does not display detailed success or error messages when a command fails.
* **Python execution:** Running from source requires a compatible Python installation and the project's visual assets.

## 🔮 Possible Future Improvements

The following are potential enhancements, not features currently implemented:

* Display the currently active power plan.
* Show success and error notifications after switching plans.
* Detect whether the High Performance power plan is available.
* Add support for additional power plans when available.
* Package the application into a standalone Windows executable.

## 📄 License

No license information is specified in this README. Please refer to the repository files for any applicable licensing terms.

---

<div align="center">

**High Performance Tool**

*A small utility for a simple task.*

Made by [faishalkc](https://github.com/faishalkc)

</div>
