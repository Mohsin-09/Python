import os
import pickle
from tkinter import Tk, Frame, Label, Button, Toplevel, StringVar, OptionMenu, Listbox, MULTIPLE, Menu, N, S, E, W
from tkinter import messagebox
from tkinter import ttk
from datetime import date, timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to get student names from the folder
def get_student_names(directory):
    return [f.split('.')[0] for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# Function to load attendance data
def load_attendance_data():
    if os.path.exists('attendance_data.pkl'):
        with open('attendance_data.pkl', 'rb') as file:
            return pickle.load(file)
    return {}

# Function to save attendance data
def save_attendance_data():
    with open('attendance_data.pkl', 'wb') as file:
        pickle.dump(attendance_data, file)

# Function to update attendance
def update_attendance():
    global attendance_data
    today = str(date.today())
    present_students = [student_listbox.get(i) for i in student_listbox.curselection()]
    attendance_data[today] = present_students
    absent_students = list(set(student_names) - set(present_students))
    save_attendance_data()
    messagebox.showinfo("Attendance Updated", f"Present Students: {present_students}\nAbsent Students: {absent_students}")

# Function to filter dates
def filter_dates(num_days):
    today = date.today()
    return [str(today - timedelta(days=i)) for i in range(num_days)]

# Function to show attendance analytics
def show_analytics():
    def plot_attendance(name, num_days=None):
        if num_days:
            dates = filter_dates(num_days)
        else:
            dates = list(attendance_data.keys())
        dates.sort()
        attendance = [1 if name in attendance_data.get(date, []) else 0 for date in dates]

        fig, ax = plt.subplots()
        ax.plot(dates, attendance, marker='o')
        ax.set_title(f'Attendance Analytics for {name}')
        ax.set_xlabel('Date')
        ax.set_ylabel('Attendance')
        ax.set_yticks([0, 1])
        ax.set_yticklabels(['Absent', 'Present'])
        
        if len(dates) > 0:
            ax.set_xticks([dates[0], dates[-1]])
            ax.set_xticklabels([dates[0], dates[-1]])

        for widget in analytics_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=analytics_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def create_plot(name):
        plot_attendance(name)
    
    def create_plot_last_7_days(name):
        plot_attendance(name, num_days=7)

    def create_plot_last_14_days(name):
        plot_attendance(name, num_days=14)

    def create_plot_last_30_days(name):
        plot_attendance(name, num_days=30)

    analytics_window = Toplevel(root)
    analytics_window.title("Attendance Analytics")
    
    analytics_frame = Frame(analytics_window)
    analytics_frame.pack(pady=10, padx=10)

    name_var = StringVar(analytics_window)
    name_var.set(student_names[0])  # Set default value

    dropdown = ttk.OptionMenu(analytics_window, name_var, student_names[0], *student_names, command=create_plot)
    dropdown.pack(pady=5)

    menu_bar = Menu(analytics_window)
    analytics_window.config(menu=menu_bar)

    time_frame_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Time Frame", menu=time_frame_menu)
    time_frame_menu.add_command(label="Last 7 Days", command=lambda: create_plot_last_7_days(name_var.get()))
    time_frame_menu.add_command(label="Last 14 Days", command=lambda: create_plot_last_14_days(name_var.get()))
    time_frame_menu.add_command(label="Last 30 Days", command=lambda: create_plot_last_30_days(name_var.get()))

# Main interface
root = Tk()
root.title("Face Attendance System")

# Set style
style = ttk.Style(root)
style.theme_use('clam')  # You can try 'clam', 'alt', 'default', or 'classic'
style.configure('TButton', font=('Arial', 12), padding=10)
style.configure('TLabel', font=('Arial', 14), padding=10)
style.configure('TListbox', font=('Arial', 12), padding=10)

students_directory = r"C:\Users\A1 Computer\Desktop\faceAttendanceSystem\students"
student_names = get_student_names(students_directory)

# Load attendance data
attendance_data = load_attendance_data()

date_label = ttk.Label(root, text=f"Date: {date.today().isoformat()}")
date_label.pack(pady=10)

attendance_frame = ttk.Frame(root)
attendance_frame.pack(pady=10, padx=10)

student_listbox = Listbox(attendance_frame, selectmode=MULTIPLE, font=('Arial', 12), width=30, height=15)
for student in student_names:
    student_listbox.insert('end', student)
student_listbox.pack(side='left', fill='y')

scrollbar = ttk.Scrollbar(attendance_frame, orient='vertical', command=student_listbox.yview)
scrollbar.pack(side='right', fill='y')
student_listbox.config(yscrollcommand=scrollbar.set)

update_button = ttk.Button(root, text="Update Attendance", command=update_attendance)
update_button.pack(pady=5)

analytics_button = ttk.Button(root, text="Attendance Analytics", command=show_analytics)
analytics_button.pack(pady=5)

root.mainloop()
