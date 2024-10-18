import tkinter as tk
def on_key_press(event):
    print("recla precionada: ", event.char)
root = tk.Tk()
root.title("Lector rfid")
    
text_area = tk.Text(root, height = 10, width = 40)
text_area.pack()
text_area.bind("<KeyPress>", on_key_press)

root.attributes("-topmost", True)
root.mainloop()