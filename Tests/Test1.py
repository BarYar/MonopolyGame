import tkinter as tk
height = 1200
start_screen = tk.Tk()
start_screen.geometry(f"{str(int(height / 4))}x{str(int(height / 4))}")
#start_screen.iconbitmap(self.getIcon())  # Set the icon for the windoww
start_screen.title("Monopoly")
tk.Label(start_screen, text="Welcome to the Monopoly Game\nChoose this game players quantity.",
         font=("Times", "15", "bold"), bg="white").place(x=0, y=0)
start_screen.configure(bg="white")
for i in range(3):  # Adding the quantity buttons
    tk.Button(start_screen, text=str(i + 2), font=(None, 16, 'bold'), bg="DarkSeaGreen1"). \
        place(x=(i * 0.0625+0.035) * height, y=0.11 * height, height=0.03 * height, width=0.05 * height)
start_screen.mainloop()