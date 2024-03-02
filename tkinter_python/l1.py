from tkinter import*
win = Tk()
win.title("window") # dat ten cho cua so
win.geometry('300x300') # dat chieu dai rong cua cua so
win['bg'] = 'green' # thay doi mau background (co the thay bang ma mau)
win.attributes('-topmost', True) #giu nguyen cua so khong bi mat di
name = Label(win, text="Tieu de")
name.place(x=30, y=30) # vi tri cua tieu de
win.mainloop() # hien cua so khong co thi khong hien