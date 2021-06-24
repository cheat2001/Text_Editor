from tkinter import *
from tkinter import filedialog
root=Tk()
root.geometry("1200x640")
root.title("Kak Text Editor")
#create Function New File
def new_file():
    txt.delete("1.0", END)
    root.title("New File - Text Editor")
    status.config(text="New File        ")
#create function open file
def open_file():
    txt.delete("1.0", END)
    #Grab FileName
    text_file=filedialog.askopenfilename(filetypes=(("All Files", "*.*"),("Text Files", "*.txt")))
    #Update Filename
    name=text_file
    status.config(text=f'{name}')
    name=name.replace("D:/", " ")
    root.title(f'{name}-Text Editor')
    #open the file
    text_file=open(text_file, 'r')
    stuff=text_file.read()
    #add file to text editor
    txt.insert(END, stuff)
    text_file.close()
#create function Save file
def saveas_file():
    text_file=filedialog.asksaveasfilename(filetypes=(("All Files", "*.*"),("Text Files", "*.txt")))
    if txt:
       #update status bar
        name=text_file
        status.config(text=f'Saved {name}')
        name = name.replace("D:/", " ")
        root.title(f'{name}-Text Editor')
        #open the file
        text_file=open(text_file, 'w')
        text_file.write(txt.get(1.0, END))
        #close FILE
        text_file.close()
#create frame
frm=Frame(root)
frm.pack(pady=5)
#create scrollbar
scr=Scrollbar(frm)
scr.pack(side=RIGHT, fill=Y)
#create text
txt=Text(frm, width=97, height=25,font=("Helvetica", 16), yscrollcommand=scr.set, bg="powderblue")
txt.pack()

#config our scroll
scr.config(command=txt.yview)
#create menu
mn=Menu(root)
root.config(menu=mn)
#Add  File menu
file=Menu(mn, tearoff=0)
mn.add_cascade(label="File", menu=file)
file.add_command(label="New", command=new_file)
file.add_command(label="Open", command=open_file)
file.add_command(label="Save", command=saveas_file)
file.add_command(label="Save as", command=saveas_file)
file.add_separator()
file.add_command(label="Exit", command=root.quit)
#Add Edit Menu
edit=Menu(mn, tearoff=0)
mn.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Undo")
edit.add_command(label="Redo")

#Add search Menu
search=Menu(mn, tearoff=0)
mn.add_cascade(label="Search", menu=search)
search.add_command(label="Find")
search.add_command(label="Find in file")
search.add_command(label="Find next")
search.add_command(label="Find previous")
search.add_command(label="Replace")
#Add Window Menu
window=Menu(mn, tearoff=0)
mn.add_cascade(label="Window", menu=window)
window.add_command(label="Close All", command=root.quit)
#Add help Menu
help=Menu(mn, tearoff=0)
mn.add_cascade(label="Help", menu=help)
help.add_command(label="More About")
#Add Status bar in the bottom
status=Label(text="@copyright by cheat       ", anchor=E)
status.pack(fill=X, side=BOTTOM, ipady=5)
root.mainloop()
