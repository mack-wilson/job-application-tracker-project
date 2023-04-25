# app.py

import tkinter as tk
from ui import JobAppTrackerUI
import data_handler

def main():
    root = tk.Tk()
    data_handler_instance = data_handler
    app = JobAppTrackerUI(root, data_handler_instance)
    root.mainloop()
    
if __name__ == "__main__":
    main()
