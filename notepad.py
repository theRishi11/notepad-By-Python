from tkinter import*
top = Tk()
top.geometry("600x500")
top.title("Notepad by Rishi")

def newFile():
    editor.delete(1.0,END)

def closeCWSNotepad():
    top.quit()

menubar = Menu(top)

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command=newFile)
filemenu.add_command(label="New Window")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save As")
filemenu.add_separator()
filemenu.add_command(label="Page Setup")
filemenu.add_command(label="Print\tctrl + p")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=closeCWSNotepad)

editmenu = Menu(menubar,tearoff=0)
editmenu.add_command(label="Undo")
editmenu.add_command(label="Cut     Ctrl+X")
editmenu.add_command(label="Copy     Ctrl+C")
editmenu.add_command(label="Paste   Ctrl+V")
editmenu.add_command(label="Delete    DEL")
editmenu.add_separator()
editmenu.add_command(label="Find   Ctrl+F")
editmenu.add_command(label="Find Next\tctrl+F3")
editmenu.add_command(label="Find Previous\tShift+F3")
editmenu.add_command(label="Repalce\t Ctrl+H")
editmenu.add_command(label="Go to\t Ctrl+G")
editmenu.add_separator()
editmenu.add_command(label="Select All\t Ctrl+A")
editmenu.add_command(label="Time/Date\tF5")
editmenu.add_separator()

formatMenu = Menu(menubar,tearoff=0)
formatMenu.add_command(label="WordWrap")
formatMenu.add_command(label="Font")

viewMenu = Menu(menubar,tearoff=0)

zoomMenu = Menu(viewMenu,tearoff=0)
zoomMenu.add_command(label="Zoom In")
zoomMenu.add_command(label="Zoom Out")

viewMenu.add_cascade(label="Zoom",menu=zoomMenu)
zoomMenu.add_command(label="Status Bar")

menubar.add_cascade(label="File",menu=filemenu)
menubar.add_cascade(label="Edit",menu=editmenu)
menubar.add_cascade(label="Format",menu=formatMenu)
menubar.add_cascade(label="View",menu=viewMenu)

editor = Text(top,width=600)
editor.pack()

footerText = StringVar()
footerText.set("Ln 1,col 1 \t|\t100%\tWindow (CRLF) \t \t| \tUTF-8")
footer = Label(top,textvariable=footerText,bd=1,relief=SUNKEN,anchor=W)
footer.pack(side=BOTTOM,fill=X)
top.config(menu=menubar)
top.mainloop()