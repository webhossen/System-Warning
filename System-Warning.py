import tkinter as tk
import threading
import time
import pyttsx3  # text-to-speech
import winsound  # For Windows sound support

# --- Basic Configuration ---
HEADER_TEXT = "⚠ YOUR SYSTEM WAS HACKED BY HOSSEN ⚠"
CENTER_LINE1 = "All your information is being copied."
EMOJI = "💾"
PROGRESS_DURATION = 20
FLASH_INTERVAL = 0.6
SIREN_INTERVAL = 3

# --- Icon Color Configuration ---
COLOR_CYCLE_SPEED = 0.2
RAINBOW_COLORS = [
    "#FF0000", "#FF7F00", "#FFFF00", "#7FFF00",
    "#0000FF", "#00FF7F", "#00FFFF"
]
ICON_FONT_SIZE = 220
# -------------------------------

class WarningApp:
    def __init__(self, root):
        self.root = root
        root.title("System Warning")
        root.configure(bg="black")
        root.attributes("-fullscreen", True)

        # Initialize text-to-speech
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 165)
            self.voice_enabled = True
        except Exception:
            self.voice_enabled = False

        # Create main canvas and elements
        self.canvas = tk.Canvas(root, bg="black", highlightthickness=0)
        self.canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.flashing = True

        self.header = tk.Label(root, text=HEADER_TEXT, bg="black", fg="#ff2d2d",
                               font=("Helvetica", 24, "bold"))
        self.header.pack(pady=(30, 10))

        self.center_frame = tk.Frame(root, bg="black")
        self.center_frame.pack(expand=True)

        self.line1 = tk.Label(self.center_frame, text=CENTER_LINE1, bg="black", fg="white",
                              font=("Helvetica", 26))
        self.line1.pack(pady=(0, 10))

        self.warning_icon_label = tk.Label(self.center_frame, text="⚠",
                                           bg="black", fg=RAINBOW_COLORS[0],
                                           font=("Helvetica", ICON_FONT_SIZE, "bold"))
        self.warning_icon_label.pack(pady=(20, 20))

        self.progress_label = tk.Label(self.center_frame, text="Data copied: 0% " + EMOJI,
                                       bg="black", fg="#ccff00", font=("Helvetica", 22))
        self.progress_label.pack(pady=(12, 0))

        self.footer = tk.Label(root, text="Hack By MD. Anayet Hossen", bg="black", fg="#7f7f7f",
                               font=("Helvetica", 12))
        self.footer.pack(side="bottom", pady=(0, 18))

        # Hidden exit option
        root.bind("<Escape>", lambda e: None)
        root.bind("<Control-0>", lambda e: self.exit())
        self._hidden_exit_button = tk.Button(root, text="Hidden Exit (Ctrl+0)", command=self.exit)

        # --- Background Threads ---
        threading.Thread(target=self._progress_thread, daemon=True).start()
        threading.Thread(target=self._flash_thread, daemon=True).start()
        threading.Thread(target=self._play_warning_sound, daemon=True).start()
        threading.Thread(target=self._voice_announce, daemon=True).start()
        threading.Thread(target=self._color_cycle_icon_thread, daemon=True).start()
        # ---------------------------

    # Progress simulation
    def _progress_thread(self):
        steps = PROGRESS_DURATION
        for i in range(steps + 1):
            if not self.flashing:
                break
            percent = int((i / steps) * 100)
            self.progress_label.config(text=f"Data copied: {percent}% {EMOJI}")
            time.sleep(1)
        self._on_finish()

    # Flashing red border
    def _flash_thread(self):
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        pad = 6
        on = False
        while self.flashing:
            on = not on
            self.canvas.delete("border")
            if on:
                self.canvas.create_rectangle(pad, pad, w - pad, h - pad,
                                             outline="#ff2d2d", width=10, tags="border")
            self.canvas.update()
            time.sleep(FLASH_INTERVAL)

    # Cycle warning icon colors
    def _color_cycle_icon_thread(self):
        color_index = 0
        while self.flashing:
            new_color = RAINBOW_COLORS[color_index % len(RAINBOW_COLORS)]
            self.warning_icon_label.config(fg=new_color)
            self.warning_icon_label.update()
            color_index += 1
            time.sleep(COLOR_CYCLE_SPEED)

    # Play repeating beep
    def _play_warning_sound(self):
        while self.flashing:
            winsound.Beep(800, 500)
            time.sleep(SIREN_INTERVAL)

    # Voice alert (initial)
    def _voice_announce(self):
        if not self.voice_enabled:
            return
        try:
            self.engine.say("Warning. YOUR SYSTEM WAS HACKED BY HOSSEIN.")
            self.engine.say("All your information is being copied.")
            self.engine.say("Copying your data now.")
            for _ in range(9):
                self.engine.say("Warning.")
            self.engine.runAndWait()
        except Exception:
            pass

    # Voice alert (final message)
    def _final_voice_announcement(self):
        if not self.voice_enabled:
            return
        try:
            current_rate = self.engine.getProperty('rate')
            self.engine.setProperty('rate', 160)
            self.engine.say("Your Data was Copied Successfully.")
            self.engine.say("Data copy complete, 100 percent.")
            self.engine.runAndWait()
            self.engine.setProperty('rate', current_rate)
        except Exception:
            pass

    # End animation and show completion message
    def _on_finish(self):
        self.flashing = False
        self.line1.config(text="Your Data was Copied Successfully", fg="#00ff00")
        self.progress_label.config(text="Data copy: 100% ✅", fg="#cfcfcf")
        self.warning_icon_label.pack_forget()
        self.root.update()
        winsound.Beep(1000, 600)
        time.sleep(0.3)
        if self.voice_enabled:
            threading.Thread(target=self._final_voice_announcement).start()
        time.sleep(6)
        self.exit()

    # Safely exit the app
    def exit(self):
        self.flashing = False
        if self.voice_enabled:
            try:
                self.engine.stop()
            except Exception:
                pass
        try:
            self.root.destroy()
        except Exception:
            pass


if __name__ == "__main__":
    root = tk.Tk()
    app = WarningApp(root)
    root.mainloop()
