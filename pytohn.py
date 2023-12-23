from tkinter import *
root=Tk()
root.title("Billing system")
root.geometry('1910x1300')
he_label=Label(root,text='Reatil Billing system',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
he_label.pack(fill=X,padx=10)

cus_de_fr=LabelFrame(root,text='Customer Detailse',font=('times new roman',15,'bold'),fg='gray20',bd=8,relief=GROOVE)
cus_de_fr.pack(fill=X)

name_lable=Label(cus_de_fr,text="Name",font=('times new roman',15,'bold'),bg='white',fg='black')
name_lable.grid(row=0,column=0,padx=20,)

name_entry=Entry(cus_de_fr,font=('arial',15),bd=7,width=18)
name_entry.grid(row=0,column=1,padx=10)

phone_lable=Label(cus_de_fr,text="phone",font=('times new roman',15,'bold'),bg='gray20',fg='White')
phone_lable.grid(row=0,column=5,padx=70,pady=10)

phone_entry=Entry(cus_de_fr,font=('arial',15),bd=7,width=18)
phone_entry.grid(row=0,column=6,padx=10)

#heading_Lable=Label(root,text="Reatil Billing System",font=('times new roman',30,'bold','italic','underline')
#                    ,bg='gray20',fg='gold',bd=12,relief=GROOVE)
#heading_Lable.pack(fill=X,pady=10)
#customer_detils_frame=LabelFrame(root,text='Customer Datails',font=('times new roman',15,'bold',),
#                                 fg='green',bd=8,relief=GROOVE,bg='gray20')
#customer_detils_frame.pack(fill=X)

#name_lable=Label(customer_detils_frame,text="Name",font=('times new roman',15,'bold'),bg='gray20',fg='red')
#name_lable.grid(row=0,column=0,padx=20,)

#name_entry=Entry(customer_detils_frame,font=('arial',15),bd=7,width=18)
#name_entry.grid(row=0,column=1,padx=8)


#phone_lable=Label(customer_detils_frame,text="phone",font=('times new roman',15,'bold'),bg='gray20',fg='White')
#phone_lable.grid(row=0,column=2,padx=20,pady=2)

#phone_entry=Entry(customer_detils_frame,font=('arial',15),bd=7,width=18)
#phone_entry.grid(row=0,column=3,padx=8)


#Bill_lable=Label(customer_detils_frame,text="Bill Number",font=('times new roman',15,'bold'),bg='gray20',fg='White')
#Bill_lable.grid(row=0,column=4,padx=20,pady=2)


#Bill_entry=Entry(customer_detils_frame,font=('arial',15),bd=7,width=18)
#Bill_entry.grid(row=0,column=5,padx=8)

#seatchButton=Button(customer_detils_frame,text="SEARCH",font=("arial",12,'bold','italic'),border=10,fg='blue')
#seatchButton.grid(row=0,column=6,padx=20,pady=8)




root.mainloop()
