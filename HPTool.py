import ctypes
import ctypes.wintypes
import os
import subprocess
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk


class PowerPlan:
    ENABLE_ARGS = ["powercfg", "/s", "SCHEME_MIN"]
    DISABLE_ARGS = ["powercfg", "/setactive",
                    "381b4222-f694-41f0-9685-ff5bb260df2e"]

    @staticmethod
    def _run(args):
        subprocess.run(args, creationflags=subprocess.CREATE_NO_WINDOW)

    @classmethod
    def enable_high_performance(cls):
        cls._run(cls.ENABLE_ARGS)

    @classmethod
    def disable_high_performance(cls):
        cls._run(cls.DISABLE_ARGS)


class HPToolWindow:
    SCALE = 1.0

    BASE_PAD = 40
    BASE_PAD_INNER = 16
    BASE_PAD_BUTTON_GAP = 10
    BASE_MIN_WIDTH = 400
    BASE_BUTTON_IPADY = 6
    BASE_BANNER_WIDTH = 400
    BASE_BANNER_HEIGHT = 80

    TITLE = "High Performance Tool"
    ENABLE_TEXT = "Enable High Performance Mode"
    DISABLE_TEXT = "Disable High Performance Mode"
    CREDIT_TEXT = "Created by FaishalKC"

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ICON_PATH = os.path.join(BASE_DIR, "icon.ico")
    BANNER_PATH = os.path.join(BASE_DIR, "banner.png")

    SPI_GETWORKAREA = 48

    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

        self._setup_window()
        self._setup_fonts()
        self._build_banner()
        self._build_buttons()
        self._build_credit()
        self._center()

        self.root.deiconify()

    def run(self):
        self.root.mainloop()

    def _s(self, value):
        return int(round(value * self.SCALE))

    def _setup_window(self):
        self.root.resizable(False, False)
        self.root.iconbitmap(self.ICON_PATH)
        self.root.title(self.TITLE)

    def _setup_fonts(self):
        system_font = tkFont.nametofont("TkDefaultFont").actual()
        family = system_font["family"]
        size = system_font["size"]
        self.font = tkFont.Font(family=family, size=self._s(size))
        self.small_font = tkFont.Font(family=family,
                                      size=self._s(max(size - 1, 1)))

    def _build_banner(self):
        image = Image.open(self.BANNER_PATH).resize(
            (self._s(self.BASE_BANNER_WIDTH),
             self._s(self.BASE_BANNER_HEIGHT)),
            Image.LANCZOS)
        self.banner = ImageTk.PhotoImage(image)
        self.banner_label = tk.Label(self.root, image=self.banner)
        self.banner_label.pack(padx=self._s(self.BASE_PAD),
                               pady=(self._s(self.BASE_PAD),
                                     self._s(self.BASE_PAD_INNER)))

    def _build_buttons(self):
        self.enable_button = self._make_button(
            self.ENABLE_TEXT, PowerPlan.enable_high_performance)
        self.enable_button.pack(padx=self._s(self.BASE_PAD),
                                fill="x",
                                ipady=self._s(self.BASE_BUTTON_IPADY))

        self.disable_button = self._make_button(
            self.DISABLE_TEXT, PowerPlan.disable_high_performance)
        self.disable_button.pack(padx=self._s(self.BASE_PAD),
                                 pady=(self._s(self.BASE_PAD_BUTTON_GAP), 0),
                                 fill="x",
                                 ipady=self._s(self.BASE_BUTTON_IPADY))

    def _make_button(self, text, command):
        return tk.Button(self.root, text=text, font=self.font,
                         relief="solid", command=command)

    def _build_credit(self):
        self.credit_label = tk.Label(self.root, text=self.CREDIT_TEXT,
                                     font=self.small_font)
        self.credit_label.pack(pady=(self._s(self.BASE_PAD_INNER),
                                     self._s(self.BASE_PAD_INNER)))

    def _get_work_area(self):
        rect = ctypes.wintypes.RECT()
        ctypes.windll.user32.SystemParametersInfoW(
            self.SPI_GETWORKAREA, 0, ctypes.byref(rect), 0)
        return rect

    def _center(self):
        self.root.update_idletasks()
        w = max(self.root.winfo_reqwidth(), self._s(self.BASE_MIN_WIDTH))
        h = self.root.winfo_reqheight()

        area = self._get_work_area()
        x = area.left + (area.right - area.left - w) // 2
        y = area.top + (area.bottom - area.top - h) // 2
        self.root.geometry(f"{w}x{h}+{x}+{y}")


def main():
    ctypes.windll.user32.SetProcessDPIAware()
    HPToolWindow().run()


if __name__ == "__main__":
    main()
