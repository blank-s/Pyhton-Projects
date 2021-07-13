from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1250x700+0+0")

        title=Label(self.root,text="STUDENT MANAGEMENT SYSTEM",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)
        #------------all variables---------------
        self.Roll_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()

        self.search_by=StringVar()
        self.search_text=StringVar()


        #---------manage frame-------------------

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="sky blue")
        Manage_Frame.place(x=20,y=100,width=400,height=560)
        
        m_title=Label(Manage_Frame,text="Manage Frame",bg="sky blue",fg="red",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_Frame,text="Roll no.",bg="sky blue",fg="red",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,padx=5,pady=8,sticky="w")

        txt_roll=Entry(Manage_Frame,textvariable=self.Roll_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE )
        txt_roll.grid(row=1,column=1,padx=5,pady=8,sticky="w")

        lbl_name=Label(Manage_Frame,text="Name ",bg="sky blue",fg="red",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,padx=5,pady=8,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE )
        txt_name.grid(row=2,column=1,padx=5,pady=8,sticky="w")

        lbl_email=Label(Manage_Frame,text="Email",bg="sky blue",fg="red",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,padx=5,pady=8,sticky="w")

        txt_email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE )
        txt_email.grid(row=3,column=1,padx=5,pady=8,sticky="w")

        lbl_Gender=Label(Manage_Frame,text="Gender",bg="sky blue",fg="red",font=("times new roman",20,"bold"))
        lbl_Gender.grid(row=4,column=0,padx=5,pady=8,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,width=18,height=5,font=("times new roman",14,"bold"),state="readonly")
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=6,pady=8,sticky="w" )

        lbl_contact=Label(Manage_Frame,text="Contact",bg="sky blue",fg="red",font=("times new roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,padx=5,pady=8,sticky="w")

        txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE )
        txt_contact.grid(row=5,column=1,padx=5,pady=8,sticky="w")

        lbl_dob=Label(Manage_Frame,text="D.O.B",bg="sky blue",fg="red",font=("times new roman",20,"bold"))
        lbl_dob.grid(row=6,column=0,padx=5,pady=8,sticky="w")

        txt_dob=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE )
        txt_dob.grid(row=6,column=1,padx=5,pady=8,sticky="w")

        lbl_address=Label(Manage_Frame,text="Address",bg="sky blue",fg="red",font=("times new roman",20,"bold"))
        lbl_address.grid(row=7,column=0,padx=5,pady=8,sticky="w")

        self.txt_address=Text(Manage_Frame,width=30,height=5)
        self.txt_address.grid(row=7,column=1,padx=6,pady=8,sticky="w")

        #----------button-----------------
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="sky blue")
        btn_Frame.place(x=10,y=499,width=380,height=43)

        Addbtn=Button(btn_Frame,text="ADD",width=10,command=self.add_students).grid(row=0,column=0,padx=7,pady=5)
        updatebtn=Button(btn_Frame,text="UPDATE",width=10,command=self.update_data).grid(row=0,column=1,padx=7,pady=5)
        deletebtn=Button(btn_Frame,text="DELETE",width=10,command=self.delete_data).grid(row=0,column=2,padx=7,pady=5)
        clearbtn=Button(btn_Frame,text="CLEAR",width=10,command=self.clear).grid(row=0,column=3,padx=7,pady=5)


        

        #-----------detail frame------------
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="red")
        Detail_Frame.place(x=450,y=100,width=780,height=560)
        
        lbl_search=Label(Detail_Frame,text="Search By",bg="red",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,padx=5,pady=8,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",14,"bold"),state="readonly")
        combo_search['values']=("Roll_no","Name","Contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10 )

        txt_search=Entry(Detail_Frame,textvariable=self.search_text,width=19,font=("times new roman",20,"bold"),bd=5,relief=GROOVE )
        txt_search.grid(row=0,column=2,padx=5,pady=8,sticky="w")

        searchbtn=Button(Detail_Frame,text="SEARCH",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=7,pady=5)
        showbtn=Button(Detail_Frame,text="SHOW ALL",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=7,pady=5)

        #------------------table frame
        Table_Frame=Frame(Detail_Frame,bd=4,relief=GROOVE,bg="red")
        Table_Frame.place(x=20,y=70,width=730,height=470)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("roll",text="Roll_No")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("dob",text="D.O.B")
        self.student_table.heading("address",text="Address")
        self.student_table['show']='headings'
        self.student_table.column("roll",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("contact",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("address",width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cur)
        self.fetch_data()
    def add_students(self):
        if self.Roll_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:    
            con=pymysql.connect(host="localhost",user="root",password="",database="stm") 
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_var.get(),self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_address.get('1.0',END)))
            
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm") 
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()
    def clear(self):
        self.Roll_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("")
    def get_cur(self,ev):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        row=content['values']       
        self.Roll_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("")
        self.txt_address.insert(END,row[6])
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm") 
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where Roll_no=%s",(self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_address.get('1.0',END),self.Roll_var.get()))
        
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm") 
        cur=con.cursor()
        cur.execute("delete from students where Roll_no=%s",self.Roll_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm") 
        cur=con.cursor()

        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        else:
            messagebox.showerror("Sorry","No Related Data")
        con.close()





root=Tk()
ob=student(root)
root.mainloop()
