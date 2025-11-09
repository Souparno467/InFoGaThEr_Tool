import tkinter as tk
from tkinter import messagebox
import re
import socket

class IPAddressValidator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("IP Address Validator")
        self.geometry("450x300")
        self.configure(bg="#1E1E1E")

        self.label = tk.Label(self, text="Enter Website Link:", bg="#1E1E1E", fg="#FFFFFF", font=("Arial", 12, "bold"))
        self.label.pack(pady=10)

        self.input_entry = tk.Entry(self, width=35, font=("Arial", 12))
        self.input_entry.pack(pady=5)

        # FIND IP Button with Large Emoji
        self.find_button = tk.Button(
            self, text=" FIND IP 🔍 ", command=self.process_input, bg="#FF5733", fg="#FFFFFF",
            font=("Arial", 14, "bold"), cursor="hand2", bd=0, padx=10, pady=5
        )
        self.find_button.pack(pady=15)

        # Result Box
        self.result_box = tk.Label(
            self, text="", bg="#333333", fg="#00FF00", font=("Arial", 11, "bold"),
            width=45, height=5, wraplength=400, justify="left", relief="solid", bd=1, padx=10, pady=5
        )
        self.result_box.pack(pady=10)

    def process_input(self):
        user_input = self.input_entry.get()
        self.result_box.config(text="Processing... 🔄", fg="#FFDD00")

        if self.is_valid_ip(user_input):
            self.result_box.config(text=f"'{user_input}' is a valid IP address.", fg="#00FF00")
        else:
            try:
                ip_address = socket.gethostbyname(user_input)
                self.result_box.config(
                    text=f"The IP address of '{user_input}' is: {ip_address}",
                    fg="#00FF00"
                )
            except socket.gaierror:
                self.result_box.config(
                    text=f"Unable to resolve '{user_input}'.",
                    fg="#FF5733"
                )

    @staticmethod
    def is_valid_ip(ip):
        pattern = (
            r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\\."
            r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\\."
            r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\\."
            r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"
        )
        return re.match(pattern, ip) is not None

if __name__ == "__main__":
    app = IPAddressValidator()
    app.mainloop()
