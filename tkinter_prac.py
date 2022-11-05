# import tkinter as tk

# root=tk.Tk()
# root.geometry("600x400")
# name_var=tk.StringVar()

# def submit():
#     name=name_var.get()
#     name_var.set("")
#     label_name=tk.Label(text=name,font=("Arial",10,'bold'))
#     label_name.grid(row=3,column=2) 
#     # result = ""
#     # for char in name_var:
#     #     result = char + result
#     # return result



# name_label=tk.Label(root,text="Enter a Word:",font=("Arial",10,'bold'))    
# name_entry = tk.Entry(root,textvariable = name_var, font=("Arial",10,'normal'))
# sub_btn=tk.Button(root,text = 'Validate', command = submit)


# name_label.grid(row=0,column=0)
# name_entry.grid(row=0,column=1)
# sub_btn.grid(row=2,column=1)

# root.mainloop()



# -----------------------------------------------------------2----------------------------------------------------------------------

# import tkinter as tk

# root=tk.Tk()
# root.geometry("600x400")
# name_var=tk.StringVar()

# def submit():
#     name=name_var.get()
#     name_var.set("")
#     label_name=tk.Label(text=name,font=("Arial",10,'bold'))
#     label_name.grid(row=3,column=2) 


# name_label=tk.Label(root,text="Enter value of integer N:",font=("Arial",10,'bold'))    
# name_entry = tk.Entry(root,textvariable = name_var, font=("Arial",10,'normal'))
# sub_btn=tk.Button(root,text = 'Validate', command = submit)


# name_label.grid(row=0,column=0)
# name_entry.grid(row=0,column=1)
# sub_btn.grid(row=2,column=1)

# root.mainloop()




# -----------------------------------------------------------3-----------------------------------------------------------------------
# from tkinter import*
# import tkinter as tk

# window=Tk()
# window.title("Hello Python")
# window.geometry("500x500")

# Checkbutton1=tk.IntVar()
# Checkbutton2=tk.IntVar()

# r1=tk.Radiobutton(window,text='male',value='A')
# r1.place(x=100,y=10)
# r2=tk.Radiobutton(window,text='female',value='B')
# r2.place(x=200,y=10)


# Button1=Checkbutton(window,text="Cricket",variable=Checkbutton1,
# onvalue=1,offvalue=0,height=2,width=10)

# Button2=Checkbutton(window,text="Tennis",variable=Checkbutton2,
# onvalue=1,offvalue=0,height=2,width=10)

# Button1.place(x=100,y=30)
# Button2.place(x=200,y=30)

# window.mainloop()




# ------------------------------------------------------------4------------------------------------------------------------------

# from tkinter import*
# import tkinter as tk
# from tkinter import messagebox


# window=Tk()
# window.title("Radio Button Demo")
# window.geometry("500x500")


# def fun():
#     messagebox.showinfo("Result","S")

# def fun1():
#     messagebox.showinfo("Result","M") 

# def fun2():
#     messagebox.showinfo("Result","L")

# def fun3():
#     messagebox.showinfo("Result","XL")

# def fun4():
#     messagebox.showinfo("Result","XXL")

# name_var=tk.StringVar()

# name_label=tk.Label(window,text="What's your t-shirt size?",font=("Arial",10,'bold'))    
# name_entry = tk.Entry(window,textvariable = name_var, font=("Arial",10,'normal'))
# name_label.grid(row=0,column=0)


# r1=tk.Radiobutton(window,text='Small',value='A',command=fun)
# r1.place(x=20,y=30)

# r2=tk.Radiobutton(window,text='Medium',value='B',command=fun1)
# r2.place(x=20,y=60)

# r3=tk.Radiobutton(window,text='Large',value='C',command=fun2)
# r3.place(x=20,y=90)

# r4=tk.Radiobutton(window,text='Extra Large',value='D',command=fun3)
# r4.place(x=20,y=120)

# r5=tk.Radiobutton(window,text='Extra Extra Large',value='E',command=fun4)
# r5.place(x=20,y=150)


# window.mainloop()




# ----------------------------------------------------------5--------------------------------------------------------------------------