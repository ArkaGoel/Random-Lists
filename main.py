from tkinter import *
import random

root = Tk()
root.title("Random Lists")
root.geometry("400x400")
root.configure(background="aqua")
label_random_lists = Label(root)
label_random_lists_sort = Label(root)
label_random_lists.place(relx=0.5, rely=0.4, anchor=CENTER)
label_random_lists_sort.place(relx=0.5, rely=0.5, anchor=CENTER)
label_random_lists.configure(fg="red")
label_random_lists_sort.configure(fg="green")
def randomList():
    list1 = random.sample(range(0,100),10)
    label_random_lists["text"]="The random list generated is: " + str(list1)
    list1.sort()
    label_random_lists_sort["text"]= "The sorted random list is: " + str(list1)
button = Button(root, text="Generate Random List", command=randomList)
button.place(relx=0.5, rely=0.6, anchor=CENTER)
button.configure(bg="black", background="yellow", fg="purple")
root.mainloop()