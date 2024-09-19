from tkinter import *
from tkinter.font import Font


# Window config
root = Tk()
root.title("Todoist")
# root.iconbitmap("")
root.geometry("500x500")

# Font config
my_font = Font(
        family = "Brush script MT",
        size = 15,
        weight = "bold")


# create Frame
my_frame = Frame(root)
my_frame.pack(pady=10)

# create Listbox
my_list = Listbox(my_frame,
                  font=my_font,
                  width=25,
                  height=5,
                  bg="SystemButtonFace",
                  bd=0,
                  fg="#464646",
                  highlightthickness=0,
                  selectbackground="#a6a6a6",
                  activestyle="none")
my_list.pack()

# stuff in Listbox demo
stuff = ["walk the dog","bug grocery","kill a gay","pay money"]
for item in stuff:
    my_list.insert(END,item)

# create scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT,fill=BOTH)

# add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# create entry box
my_entry = Entry(root,font=("Helvetica",20))
my_entry.pack(pady=20)

# button Frame
button_frame = Frame(root)
button_frame.pack(pady=20)

def delete_item():
    my_list.delete(ANCHOR)


def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

def cross_off_item():
    pass

def uncross_item():
    pass



# delete button 
delete_button = Button(button_frame,text="delete task",command=delete_item)
add_button = Button(button_frame,text="add task",command=add_item)
cross_off_button = Button(button_frame,text="cross off",command=cross_off_item)
uncross_button = Button(button_frame,text="uncross",command=uncross_item)


delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0,column=2)
uncross_button.grid(row=0, column=3,padx=20)






if __name__ == "__main__":
   root.mainloop()
