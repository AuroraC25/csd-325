# Name: Aurora Crippen
# GitHub Repository: https://github.com/AuroraC25/csd-325.git
# Date: August 12, 2026
# Course: CSD 325-T301_2267_1 Advanced Python
# Assignment: Module 10.2 Assignment
# Description: Tkinter Scrolling To Do List


import tkinter as tk
import tkinter.messagebox as msg


class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        #Create an empty list to store tasks if no tasks are provided
        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        #Create the canvas and frames used to display and scroll through tasks
        self.tasks_canvas = tk.Canvas(self)

        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        #Create a vertical scrollbar for the task list
        self.scrollbar = tk.Scrollbar(
            self.tasks_canvas,
            orient="vertical",
            command=self.tasks_canvas.yview
        )

        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        # ***Changed the window title to my last name for the assignment***
        self.title("Crippen-ToDo")
        self.geometry("300x400")

        # ***Added a File menu with an Exit option to close the program***
        menu_bar = tk.Menu(self)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.destroy)

        menu_bar.add_cascade(label="File", menu=file_menu)

        self.config(menu=menu_bar)

        #Create the text box where the user enters new tasks
        self.task_create = tk.Text(
            self.text_frame,
            height=3,
            bg="white",
            fg="black"
        )

        #Position the task canvas, scrollbar, and text entry area
        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window(
            (0, 0),
            window=self.tasks_frame,
            anchor="n"
        )

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        #Display instructions and use right-click to delete a task
        # ***Changed instruction color to navy with white text***
        todo1 = tk.Label(
            self.tasks_frame,
            text="--- Add Items Here --- **Right Click to Delete**",
            bg="navy",
            fg="white",
            pady=10
        )
        todo1.bind("<Button-3>", self.remove_task)

        self.tasks.append(todo1)

        #Display each task in the task list
        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        #Bind keyboard, window, and mouse actions to their functions
        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        # ***Changed task colors to alternate between navy and red***
        self.colour_schemes = [
            {"bg": "navy", "fg": "white"},
            {"bg": "red3", "fg": "white"}
        ]

    #Add a new task when the user enters text and presses Enter
    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()

        #Do not add a task if the text box is empty
        if len(task_text) > 0:
            new_task = tk.Label(
                self.tasks_frame,
                text=task_text,
                pady=10
            )

            self.set_task_colour(len(self.tasks), new_task)

            # ***Changed deletion from left-click to right-click***
            new_task.bind("<Button-3>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)

        #Clear the text box after attempting to add a task
        self.task_create.delete(1.0, tk.END)

    #Ask for confirmation before deleting the selected task
    def remove_task(self, event):
        task = event.widget

        if msg.askyesno(
            "Really Delete?",
            "Delete " + task.cget("text") + "?"
        ):
            self.tasks.remove(event.widget)
            event.widget.destroy()
            self.recolour_tasks()

    #Reapply alternating colors after a task is deleted
    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    #Select the appropriate color based on the task's position
    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)

        my_scheme_choice = self.colour_schemes[task_style_choice]

        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])

    #Update the scrollable area when the task frame changes size
    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(
            scrollregion=self.tasks_canvas.bbox("all")
        )

    #Keep the task labels the same width as the canvas
    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(
            self.canvas_frame,
            width=canvas_width
        )

    #Allow the mouse wheel to scroll through the task list
    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(
                int(-1 * (event.delta / 120)),
                "units"
            )
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1

            self.tasks_canvas.yview_scroll(move, "units")

# Create and run the To-Do application
if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()