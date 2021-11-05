from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import filedialog

# Main Window
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x600')


# # Texts
# lbl = Label(window, text="Hello")
# lbl.grid(column=11, row=26)

# # Inputting
# txt = Entry(window,width=10)
# txt.grid(column=0, row=1)

# # Functions
# def clicked():
#     res = "Welcome to " + txt.get()
#     lbl.configure(text= res)
# def rclick() :
#     lbl1 = Label(window, text="Radio Clicked")
#     lbl1.grid(column=0, row=7)

# # Buttons
# btn = Button(window, text="Click Me", command=clicked)
# btn.grid(column=0, row=2)

# # ComboBox
# combo = Combobox(window, state='readonly')
# combo['values']= ("Aditya", "Ashutosh", "Anjali", "Ayushika", "Krishna", "Vikas")
# combo.current(0) #set the selected item
# combo.grid(column=0, row=3)

# # CheckBox
# chk_state = BooleanVar()
# chk_state.set(False)
# chk = Checkbutton(window, text='Choose', var=chk_state)
# chk.grid(column=0, row=4)

# # Radio Buttons
# rad1 = Radiobutton(window, text='First', value=1)
# rad2 = Radiobutton(window,text='Second', value=2, command=rclick)
# rad3 = Radiobutton(window,text='Third', value=3)
# rad1.grid(column=0, row=6)
# rad2.grid(column=1, row=6)
# rad3.grid(column=2, row=6)

# # Scrolled Text
# txt1 = scrolledtext.ScrolledText(window, width=40, height=10)
# txt1.grid(column=0, row=8)
# txt1.insert(INSERT, 'Aditya Kumar\n ssddf\nsdd\nss')
# txt1.delete(2.0, END)

#-------MessageBox Starts
# Info
def mesb() :
    messagebox.showinfo('God', 'Come home fastly!')
btnn = Button(window, text='Mom', command=mesb)
btnn.grid(column=0, row=-1, pady=12)

# Warning & error messages 
"""messagebox.showwarning('Boards', 'Complete Your Syllabus')
messagebox.showerror('Python', 'Debug this code')"""

# AskQuestions Dialogs
"""res = messagebox.askquestion('Message title','Message content')
res = messagebox.askyesno('Message title','Message content')
res = messagebox.askyesnocancel('Message title','Message content')
res = messagebox.askokcancel('Message title','Message content')
res = messagebox.askretrycancel('Message title','Message content')"""
#------------MessageBox Ends Here

# # SpinBox
# spin = Spinbox(window, from_=1, to=10, width=10)
# spin.grid(column=0, row=10)

# #-----------------This Part is not Understood by me
# # For Progressbar Color
# style = ttk.Style()
# style.theme_use('default')
# style.configure("white.Horizontal.TProgressbar", background='red')
# # Progressbar
# bar = Progressbar(window, length=200, style='white.Horizontal.TProgressbar')
# bar['value'] = 70
# bar.grid(column=0, row=12)
# #-------------------------------------------------

# # FileDialog
# # file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
# # dir = filedialog.askdirectory()
# # file1 = filedialog.askopenfilename(initialdir= path.D(__file__)) # Error 

# # MenuBar
# menu = Menu(window)
# new_item = Menu(menu, tearoff=0)
# new_item.add_command(label='New')
# new_item.add_separator()
# new_item.add_command(label="Edit")
# menu.add_cascade(label='File', menu=new_item)
# window.config(menu=menu)


# Tab Control Starts--------------Not Working----------------
"""tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')
lbl1 = Label(tab1, text= 'label1')
lbl1.grid(column=0, row=0)
lbl2 = Label(tab2, text= 'label2')
lbl2.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')"""
window.mainloop()