from guizero import App, Text, TextBox, PushButton, ListBox, Box

# Task operations
def add_task():
    task = task_input.value.strip()
    if task:
        task_listbox.append(task)  # Directly add to ListBox
        task_input.clear()

def delete_task():
    if task_listbox.value:
        task_listbox.remove(task_listbox.value)

def clear_tasks():
    task_listbox.clear()

def mark_task_completed():
    if task_listbox.value:
        selected = task_listbox.value
        completed = f"{selected} (Completed)"
        index = task_listbox.items.index(selected)
        task_listbox.items[index] = completed  # Update directly

# App setup
app = App("Task Manager", width=350, height=400)

# Title
Text(app, text="Task Manager", size=18, color="blue", align="top")

# Task Input Area
task_input = TextBox(app, width=30, align="top", text="Enter a task...")  # Simpler placeholder alternative
task_input.when_clicked = lambda: task_input.clear() if task_input.value == "Enter a task..." else None

# Buttons for Task Actions
PushButton(app, text="Add Task", command=add_task, align="top")
PushButton(app, text="Mark Completed", command=mark_task_completed, align="top")
PushButton(app, text="Delete Task", command=delete_task, align="top")
PushButton(app, text="Clear All Tasks", command=clear_tasks, align="top")

# Task List
task_listbox = ListBox(app, width=40, height=15, align="top")

# Run the app
app.display()