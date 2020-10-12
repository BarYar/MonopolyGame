#with open ("../Files/Cities/Haifa.txt", "r") as text:
    #lines=text.read().split()
    #print(lines)
import tkinter as tk
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
ratio=
window = tk.Tk()
# welcome = tk.Label(bg="black")
# welcome.place(relx=0, rely=0, relheight=0.17, relwidth=0.17)
playerdetails1 = tk.Label(bg="black")
playerdetails1.place(relx=0, rely=0.87, relheight=0.13, relwidth=1)
playerdetails2 = tk.Label(bg="black")
playerdetails2.place(relx=0, rely=0, relheight=0.13, relwidth=1)
playerdetails3 = tk.Label(bg="black")
playerdetails3.place(relx=0, rely=0, relheight=1, relwidth=0.13)
playerdetails4 = tk.Label(bg="black")
playerdetails4.place(relx=0.87, rely=0, relheight=1, relwidth=0.13)
# b = tk.Label(bg="white")
# b.place(relx=0.5, rely=0.88, relheight=0.11, relwidth=0.05)
#window.geometry(f'{screensize[0]}x{screensize[1]}')
window.attributes("-fullscreen", True)
window.mainloop()