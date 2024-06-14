import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess

class Maze_Game:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.title("Maze Game Raioniee")

        # Define states
        self.states = ["MENU", "GAME", "ABOUT"]
        self.current_state = "MENU"
        print("Current State:", self.current_state)

        # Define the transition table
        self.transitions = {
            "MENU": {"start_game": "GAME", "show_about": "ABOUT"},
            "GAME": {"back_to_menu": "MENU"},
            "ABOUT": {"back_to_menu": "MENU"}
        }

        # Define state methods
        self.state_methods = {
            "MENU": self.show_MENU,
            "GAME": self.start_game,
            "ABOUT": self.show_about
        }

        # Bg
        img1 = Image.open(r".\\images\\bg.jpeg")
        img1 = img1.resize((600, 400))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        self.bg_label = ttk.Label(self.root, image=self.photoimg1)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Frames
        self.main_frame = tk.Frame(self.bg_label, bg="white")
        self.tentang_frame = tk.Frame(self.bg_label, bg="white")

        # Label game
        self.label = tk.Label(self.bg_label, text="Raioniee Maze Game", bg="#FF90BC", fg="white", font=("Helvetica", 20))
        self.label.place(x=150, y=130)

        # State display label
        self.state_label = tk.Label(self.root, text=f"State: {self.current_state}", bg="pink", fg="white", font=("Helvetica", 12))
        self.state_label.place(x=10, y=370)

        # Initially show menu state
        self.state_methods[self.current_state]()

    def transition(self, event):
        try:
            self.current_state = self.transitions[self.current_state][event]
            self.state_label.config(text=f"State: {self.current_state}")  # Update the state label
            self.state_methods[self.current_state]()
        except KeyError:
            print(f"No transition for event '{event}' from state '{self.current_state}'")

    def show_MENU(self):
        self.main_frame.pack_forget()
        self.tentang_frame.pack_forget()

        try:
            self.tentang_label.place_forget()
        except AttributeError:
            pass

        # Display menu elements here
        b1 = tk.Button(self.bg_label, text="Main", fg="pink", bg="white", command=lambda: self.transition("start_game"))
        b1.place(x=280, y=200)

        b2 = tk.Button(self.bg_label, text="Tentang", fg="pink", bg="white", command=lambda: self.transition("show_about"))
        b2.place(x=270, y=250)

    def start_game(self):
        self.current_state = "GAME"  # Set the current state to GAME
        self.state_label.config(text=f"State: {self.current_state}")  # Update the state label
        self.root.withdraw()
        subprocess.Popen(['python', './maze_game.py']).wait()
        self.root.deiconify()
        self.transition("back_to_menu")

    def show_about(self):
        self.current_state = "ABOUT"  # Set the current state to ABOUT
        self.state_label.config(text=f"State: {self.current_state}")  # Update the state label
        self.main_frame.pack_forget()
        print("Current State:", self.current_state)

        # Display tentang 
        img2 = Image.open(r".\\images\\purple.jpeg")
        img2 = img2.resize((600, 400))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        self.tentang_label = ttk.Label(self.root, image=self.photoimg2)
        self.tentang_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Tampilan sy
        self.label = tk.Label(self.tentang_label, text="Raioniee Maze Game", bg="#FF90BC", fg="white", font=("Helvetica", 20))
        self.label.place(x=150, y=130)
        self.label = tk.Label(self.tentang_label, text="Dibuat oleh:\nAdinda Salsabila (2215006135)\ndan\n Rafael Pascal Jeremiah (2215061007)", font=("Helvetica", 10), fg="#FF90BC", bg="white")
        self.label.place(x=150, y=200)

        # Back to menu button
        self.back_button = tk.Button(self.tentang_label, text="Back", fg="pink", bg="white", command=lambda: self.transition("back_to_menu"))
        self.back_button.place(x=270, y=300)

if __name__ == "__main__":
    root = tk.Tk()
    obj = Maze_Game(root)
    root.mainloop()
