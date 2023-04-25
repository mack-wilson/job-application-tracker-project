# ui.py
import data_handler

import tkinter as tk
from tkinter import ttk



class JobAppTrackerUI:
    def __init__(self, master, data_handler):
        self.master = master
        self.data_handler = data_handler
        self.master.title("Job Application Tracker")
        self.file_name = "job_applications.csv"
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

        self.new_app_data = {
            'job_title': tk.StringVar(),
            'company': tk.StringVar(),
            'source': tk.StringVar(),
            'job_link': tk.StringVar(),
            'salary_estimate': tk.StringVar()
        }

        self.create_input_field(self.new_app_frame, "Job Title", self.new_app_data['job_title'], 0)
        self.create_input_field(self.new_app_frame, "Company", self.new_app_data['company'], 1)
        self.create_input_field(self.new_app_frame, "Source", self.new_app_data['source'], 2)
        self.create_input_field(self.new_app_frame, "Job Link", self.new_app_data['job_link'], 3)
        self.create_input_field(self.new_app_frame, "Salary Estimate", self.new_app_data['salary_estimate'], 4)

        submit_button = ttk.Button(self.new_app_frame, text="Submit", command=self.submit_new_app)
        submit_button.grid(row=5, column=1, pady=10)

        back_button = ttk.Button(self.new_app_frame, text="Back to Home", command=self.back_to_home)
        back_button.grid(row=6, column=1, pady=10)

    def create_input_field(self, parent, label_text, text_var, row):
        label = ttk.Label(parent, text=label_text)
        label.grid(row=row, column=0, padx=10, pady=5, sticky=tk.W)
        entry = ttk.Entry(parent, textvariable=text_var, width=50)
        entry.grid(row=row, column=1, padx=10, pady=5)

    def db_page(self):
        self.home_frame.pack_forget()
        self.db_frame = ttk.Frame(self.master)
        self.db_frame.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(self.db_frame, columns=('Job Title', 'Company', 'Source', 'Job Link', 'Salary Estimate', 'Status'), show='headings')
        for col in self.tree['columns']:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.W)
        self.tree.pack(pady=5, padx=5, expand=True, fill=tk.BOTH)

        self.load_applications()

        update_button = ttk.Button(self.db_frame, text="Update Selected Application", command=self.update_application)
        update_button.pack(side=tk.LEFT, padx=5)

        delete_button = ttk.Button(self.db_frame, text="Delete Selected Application", command=self.delete_application)
        delete_button.pack(side=tk.RIGHT, padx=5)

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
