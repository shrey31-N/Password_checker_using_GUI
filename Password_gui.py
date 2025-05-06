import tkinter as tk
import Password_checker_function  # custom module

# === Theme Settings ===
BG_COLOR = "#0f0f0f"
FG_COLOR = "#00ffcc"
ENTRY_BG = "#1e1e1e"
BTN_BG = "#003f5c"
BTN_FG = "#00ffcc"
FONT = ("Times New Roman", 12)
TITLE_FONT = ("Algerian", 14, "bold")

# === Window Setup ===
root = tk.Tk()
root.title("Password Checker")
root.configure(bg=BG_COLOR)
root.geometry("500x450")
root.resizable(False, False)

# === Track Password Visibility ===
is_password_visible = False

def on_check():
    pwd = entry.get()
    result = Password_checker_function.password_checker(pwd)

    if result == "Strong":
        result_label.config(text="✅ Password is Strong", fg="#00ff00")
    else:
        result_label.config(
            text="❌ Weak Password\nUse min 7 chars, A-Z, a-z, 0-9 & special char",fg="#ff4c4c")

def toggle_password():
    global is_password_visible
    if is_password_visible:
        entry.config(show="*")
        toggle_btn.config(text="👁 Show")
        is_password_visible = False
    else:
        entry.config(show="")
        toggle_btn.config(text="🙈 Hide")
        is_password_visible = True

# === Create a Centered Frame ===
main_frame = tk.Frame(root, bg=BG_COLOR)
main_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame

# === Title ===
title = tk.Label(main_frame, text="🔐 Password Checker", fg=FG_COLOR, bg=BG_COLOR, font=TITLE_FONT)
title.pack(pady=10)

# === Entry and Toggle in a Row ===
entry_frame = tk.Frame(main_frame, bg=BG_COLOR)
entry_frame.pack(pady=5)

entry = tk.Entry(entry_frame, width=25, show="*", font=FONT, bg=ENTRY_BG, fg=FG_COLOR,
                 insertbackground=FG_COLOR, relief=tk.FLAT)
entry.grid(row=0, column=0, padx=5)

toggle_btn = tk.Button(entry_frame, text="👁 Show", command=toggle_password,
                       font=("Arial", 10), bg=BTN_BG, fg=BTN_FG, relief=tk.FLAT)
toggle_btn.grid(row=0, column=1)

# === Check Button ===
check_btn = tk.Button(main_frame, text="Check Password", command=on_check, bg=BTN_BG, fg=BTN_FG,
                      font=FONT, activebackground="#005f73", relief=tk.FLAT)
check_btn.pack(pady=15)

# === Result Label ===
result_label = tk.Label(main_frame, text="", fg=FG_COLOR, bg=BG_COLOR, font=FONT)
result_label.pack(pady=5)

# === Run App ===
root.mainloop()
