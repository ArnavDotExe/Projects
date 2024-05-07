import tkinter as tk
from tkinter import filedialog, messagebox

class Notepad:
    def __init__(self, root):
        self.__root = root
        self.__root.title("Untitled - Notepad")
        self.__thisTextArea = tk.Text(self.__root, undo=True)
        self.__thisTextArea.pack(expand=True, fill='both')
        self.__thisTextArea.config(wrap='word')
        self.__thisTextArea.focus_set()
        self.__file = None
        self.__root.mainloop()

    def __openFile(self):
        self.__file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if self.__file == "":
            self.__file = None
        else:
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0, tk.END)
            with open(self.__file, "r") as file:
                self.__thisTextArea.insert(tk.END, file.read())

    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0, tk.END)

    def __saveFile(self):
        if self.__file is None:
            self.__file = filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            if self.__file == "":
                self.__file = None
            else:
                with open(self.__file, "w") as file:
                    file.write(self.__thisTextArea.get(1.0, tk.END))
                self.__root.title(os.path.basename(self.__file) + " - Notepad")
        else:
            with open(self.__file, "w") as file:
                file.write(self.__thisTextArea.get(1.0, tk.END))

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def __quitApplication(self):
        self.__root.destroy()

    def __showAbout(self):
        messagebox.showinfo("Notepad", "A simple Notepad application")

if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
