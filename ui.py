# ui.py
import tkinter as tk
from tkinter import ttk


class JobAppTrackerUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Job Application Tracker")

        self.create_home_page()

    def create_home_page(self):
        self.home_frame = ttk.Frame(self.master)
        self.home_frame.pack(fill=tk.BOTH, expand=True)

        welcome_label = ttk.Label(self.home_frame, text="Welcome to the Job Application Tracker!")
        welcome_label.pack(pady=10)

        new_app_button = ttk.Button(self.home_frame, text="Submit a New Job Application", command=self.new_application_page)
        new_app_button.pack(pady=5)

        view_apps_button = ttk.Button(self.home_frame, text="View/Edit Existing Job Applications", command=self.db_page)
        view_apps_button.pack(pady=5)

    def new_application_page(self):
        self.home_frame.pack_forget()
        self.new_app_frame = ttk.Frame(self.master)
        self.new_app_frame.pack(fill=tk.BOTH, expand=True)

        # Add input fields, labels, and buttons for new application data here

        back_button = ttk.Button(self.new_app_frame, text="Back to Home", command=self.back_to_home)
        back_button.pack(side=tk.BOTTOM, pady=10)

    def db_page(self):
        self.home_frame.pack_forget()
        self.db_frame = ttk.Frame(self.master)
        self.db_frame.pack(fill=tk.BOTH, expand=True)

        # Add UI elements for displaying and editing job applications here

        back_button = ttk.Button(self.db_frame, text="Back to Home", command=self.back_to_home)
        back_button.pack(side=tk.BOTTOM, pady=10)

    def back_to_home(self):
        if hasattr(self, 'new_app_frame'):
            self.new_app_frame.pack_forget()
        if hasattr(self, 'db_frame'):
            self.db_frame.pack_forget()

        self.home_frame.pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = JobAppTrackerUI(root)
    root.mainloop()
