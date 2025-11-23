from tkinter import *
from tkinter import messagebox
from PIL import Image , ImageTk

root = Tk()
root.title("Denomination Calculator")
root.configure(bg="#f0f0f0")
root.geometry("650x500")

upload = Image.open("app_img.jpg")

upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg="#f0f0f0")
label.place(x=180, y=20)

label1 = Label(root, text="Hey User! Welcome To Denomination Counter Apllication ", font=("Arial", 20, "bold"), bg="#f0f0f0")

label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo("Denomination Calculator", "This Application helps you to calculate the total amount based on the number of notes you have.\n\nEnter the number of notes for each denomination and click 'Calculate Total' to see the total amount.\n\nDenominations included: 2000, 500, 200, 100, 50, 20, 10, 5, 2, 1. Enjoy using the app! Alert!, Do you want to continue?")
    
    if MsgBox == 'ok':
        topwin()
        
button1 = Button(root, text="Let's get started", bg="#4caf50", fg="white", command=msg)
button1.place(x =260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.geometry("9000x9000")
    top.configure(bg="#f0f0f0")
    
    label1 = Label(top, text="Enter total amount", bg="#f0f0f0")
    entry = Entry(top)
    lbl = Label(
        top,
        text = "Here are numbers of notes for each denomination",
        bg="#f0f0f0"
     )
    l1 = Label(top, text="2000", bg="#f0f0f0", )
    l2 = Label(top, text="500", bg="#f0f0f0")
    l3 = Label(top, text="200", bg="#f0f0f0")
    l4 = Label(top, text="100", bg="#f0f0f0")
    l5 = Label(top, text="50", bg="#f0f0f0")
    l6 = Label(top, text="20", bg="#f0f0f0")
    l7 = Label(top, text="10", bg="#f0f0f0")
    l8 = Label(top, text="5", bg="#f0f0f0")
    
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)
    t5 = Entry(top)
    t6 = Entry(top)
    t7 = Entry(top)
    
    def caculator():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100
            amount %= 100
            note50 = amount // 50
            amount %= 50
            note20 = amount // 20
            amount %= 20
            note10 = amount // 10
            amount %= 10
            note5 = amount // 5
            amount %= 5
            
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            
            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
            t4.insert(END, str(note50))
            t5.insert(END, str(note20))
            t6.insert(END, str(note10))
            t7.insert(END, str(note5))
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            
    btn = Button(top, text="Calculate ", bg="#4caf50", fg="white", command=caculator)
    
    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)
    
    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    l4.place(x=180, y=290)
    l5.place(x=180, y=320)
    l6.place(x=180, y=350)
    l7.place(x=180, y=380)
    
    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    t4.place(x=270, y=290)
    t5.place(x=270, y=320)
    t6.place(x=270, y=350)
    t7.place(x=270, y=380)
    
    top.mainloop()
    
root.mainloop()

   
    