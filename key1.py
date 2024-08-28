import tkinter as tk

class UppercaseKeyboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Uppercase Keyboard")
        self.create_widgets()

    def create_widgets(self):
        # Create a text widget where the input will be displayed
        self.text_display = tk.Text(self.root, height=5, width=50, font=("Arial", 16))
        self.text_display.grid(row=0, column=0, columnspan=10)

        # Define the keyboard layout
        keys = [
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
            'z', 'x', 'c', 'v', 'b', 'n', 'm',
            'SPACE', 'ENTER', 'BACKSPACE',
        ]

        # Create buttons for each key
        row, col = 1, 0
        for key in keys:
            if key == 'SPACE':
                button = tk.Button(self.root, text='SPACE', width=20, height=2, command=lambda k=key: self.on_key_press(k))
                button.grid(row=row, column=col, columnspan=4)
                col += 4
            elif key == 'ENTER':
                button = tk.Button(self.root, text='ENTER', width=10, height=2, command=lambda k=key: self.on_key_press(k))
                button.grid(row=row, column=col, columnspan=2)
                col += 2
            elif key == 'BACKSPACE':
                button = tk.Button(self.root, text='BACKSPACE', width=10, height=2, command=lambda k=key: self.on_key_press(k))
                button.grid(row=row, column=col, columnspan=2)
                col = 0
                row += 1
            else:
                button = tk.Button(self.root, text=key.upper(), width=5, height=2, command=lambda k=key: self.on_key_press(k))
                button.grid(row=row, column=col)
                col += 1
                if col > 9:
                    col = 0
                    row += 1

    def on_key_press(self, key):
        if key == 'SPACE':
            self.text_display.insert(tk.END, ' ')
        elif key == 'ENTER':
            self.text_display.insert(tk.END, '\n')
        elif key == 'BACKSPACE':
            current_text = self.text_display.get("1.0", tk.END)[:-2]  # Remove last character
            self.text_display.delete("1.0", tk.END)  # Clear the text area
            self.text_display.insert(tk.END, current_text)  # Insert updated text
        else:
            self.text_display.insert(tk.END, key.upper())  # Convert to uppercase and insert

if __name__ == "__main__":
    root = tk.Tk()
    app = UppercaseKeyboard(root)
    root.mainloop()
