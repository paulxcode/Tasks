import tkinter as tk

tasks = []

def view_tasks():
    for i, task in enumerate(tasks):
        task_var = tk.StringVar()
        task_var.set(task)
        task_label = tk.Label(task_frame, textvariable=task_var, cursor='hand2', font=("Arial", 14), bg="lightblue")
        task_label.grid(row=i,column=1)
        task_label.bind("<Button-1>", lambda e, task_index=i: delete_task(task_index))
        task_check = tk.Checkbutton(task_frame, variable=task_var, command=lambda: change_color(task_var, task_label))
        task_check.grid(row=i,column=0)



def add_task():
    task = task_entry.get()
    tasks.append(task)
    task_entry.delete(0, "end")
    view_tasks()

def delete_task(task_index):
    task_label = task_frame.grid_slaves(row=task_index)
    task_label[0].destroy()
    del tasks[task_index]
    view_tasks()

def change_color(task_var, task_label):
    if task_var.get() == '1':
        task_label.config(bg='green')
    else:
        task_label.config(bg='lightblue')

root = tk.Tk()
root.geometry("800x600")
root.title("Task List")

task_frame = tk.Frame(root)
task_frame.pack()

task_label = tk.Label(root, text="Enter task:")
task_label.pack()

task_entry = tk.Entry(root)
task_entry.pack()

add_button = tk.Button(root, text="Add", command=add_task)
add_button.pack()

view_tasks()
root.mainloop()

