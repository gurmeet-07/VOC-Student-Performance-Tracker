import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os


# TODO List Class for handling tasks
class ToDoList:
    def __init__(self, file_name="tasks.json"):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, title, description, category):
        task = {"title": title, "description": description, "category": category, "completed": False}
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            self.save_tasks()

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            self.save_tasks()


# GUI Application
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal To-Do List")
        self.todo_list = ToDoList()

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.complete_button = tk.Button(root, text="Mark Complete", command=self.mark_complete)
        self.complete_button.pack(side=tk.LEFT, padx=5)

        # Load initial tasks
        self.load_tasks()

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)  # Clear the listbox
        for idx, task in enumerate(self.todo_list.tasks):
            status = "✔" if task['completed'] else "❌"
            display_text = f"{task['title']} [{task['category']}] - {status}"
            self.task_listbox.insert(tk.END, display_text)

    def add_task(self):
        title = simpledialog.askstring("Task Title", "Enter the task title:")
        description = simpledialog.askstring("Task Description", "Enter the task description:")
        category = simpledialog.askstring("Task Category", "Enter task category (e.g., Work, Personal, Urgent):")

        if title and category:
            self.todo_list.add_task(title, description, category)
            self.load_tasks()  # Refresh task list
        else:
            messagebox.showwarning("Invalid Input", "Task title and category are required!")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_idx = selected_task_index[0]
            self.todo_list.delete_task(task_idx)
            self.load_tasks()  # Refresh task list
        else:
            messagebox.showwarning("No Selection", "Please select a task to delete!")

    def mark_complete(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_idx = selected_task_index[0]
            self.todo_list.mark_task_completed(task_idx)
            self.load_tasks()  # Refresh task list
        else:
            messagebox.showwarning("No Selection", "Please select a task to mark as complete!")


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
