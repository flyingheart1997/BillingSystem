import os
from tkinter import *
import random,os
from tkinter import messagebox

class Billing_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing System")
        bg_color = "#074463"
        title = Label(self.root,text=". . .Billing System. . .",bd=12,relief=GROOVE,bg=bg_color,fg="yellow",font=("times new roman",20,"bold"),pady=2).place(relwidth=1)

        #==================================================Variables=====================================================
        #==================================================Cosmetics====================================================
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.hair_gail=IntVar()
        self.body_loshan=IntVar()
        self.body_spray=IntVar()

        #==================================================Grocery======================================================
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

        #==================================================Cold Drink===================================================
        self.maza=IntVar()
        self.cock = IntVar()
        self.frooti = IntVar()
        self.thumbs_up = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        #============================================Product Price & Tax================================================
        self.cosmetics_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetics_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        #==================================================Customer=====================================================
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()

        #============================================Customer Details Frame=============================================

        F1 = LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="yellow",bg=bg_color,)
        F1.place(x=0,y=65,relwidth=1)
        cname_lbl = Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_text = Entry(F1,width=17,textvariable=self.c_name,font="ts 15",bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5)

        cphn_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="white",font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_text = Entry(F1, width=17,textvariable=self.c_phone, font="ts 15", bd=5, relief=SUNKEN).grid(row=0, column=3, pady=5)

        cbil_lbl = Label(F1, text="Bill No.", bg=bg_color, fg="white",font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        cbil_text = Entry(F1, width=17,textvariable=self.search_bill, font="ts 15", bd=5, relief=SUNKEN).grid(row=0, column=5, pady=5)

        bil_btn=Button(F1,text="Search",command=self.find_bill,bd=7,fg="black",width=10).grid(column=6,row=0,padx=45,pady=10)

        #=================================================Cosmetics Frame===============================================
        F2 = LabelFrame(self.root, text="Cosmetics", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),fg="yellow", bg=bg_color, )
        F2.place(x=0, y=160, width=320,height=380)

        soap_lbl = Label(F2, text="Bath Soap", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=0, column=0, padx=10, pady=10,sticky="w")
        soap_text = Entry(F2, width=10,textvariable=self.soap, font="ts 15", bd=5, relief=SUNKEN).grid(row=0, column=1, pady=10,padx=10)

        fcream_lbl = Label(F2, text="Face Cream", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        fcream_text = Entry(F2, width=10,textvariable=self.face_cream, font="ts 15", bd=5, relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        fwash_lbl = Label(F2, text="Face Wash", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        fwash_text = Entry(F2, width=10, font="ts 15",textvariable=self.face_wash, bd=5, relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        hgail_lbl = Label(F2, text="Hair Gail", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        hgail_text = Entry(F2, width=10, font="ts 15",textvariable=self.hair_gail, bd=5, relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        bloshan_lbl = Label(F2, text="Body Loshan", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=4, column=0, padx=10, pady=10, sticky="w")
        bloshan_text = Entry(F2, width=10, font="ts 15",textvariable=self.body_loshan, bd=5, relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        bspray_lbl = Label(F2, text="Body Spray", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=5, column=0, padx=10, pady=10, sticky="w")
        bspray_text = Entry(F2, width=10, font="ts 15",textvariable=self.body_spray, bd=5, relief=SUNKEN).grid(row=5, column=1, pady=10, padx=10)

        # =================================================Grocery Frame===============================================
        F3 = LabelFrame(self.root, text="Grocery", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),fg="yellow", bg=bg_color, )
        F3.place(x=325, y=160, width=280, height=380)

        rice_lbl = Label(F3, text="Rice", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        rice_text = Entry(F3, width=10, font="ts 15",textvariable=self.rice, bd=5, relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        foil_lbl = Label(F3, text="Food Oil", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        foil_text = Entry(F3, width=10, font="ts 15", bd=5,textvariable=self.food_oil, relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        daal_lbl = Label(F3, text="Daal", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        daal_text = Entry(F3, width=10, font="ts 15",textvariable=self.daal, bd=5, relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        wheat_lbl = Label(F3, text="Wheat", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        wheat_text = Entry(F3, width=10, font="ts 15",textvariable=self.wheat, bd=5, relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        sugar_lbl = Label(F3, text="Sugar", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=4, column=0, padx=10, pady=10, sticky="w")
        sugar_text = Entry(F3, width=10, font="ts 15",textvariable=self.sugar, bd=5, relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        tea_lbl = Label(F3, text="Tea", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=5, column=0, padx=10, pady=10, sticky="w")
        tea_text = Entry(F3, width=10, font="ts 15",textvariable=self.tea, bd=5, relief=SUNKEN).grid(row=5, column=1, pady=10, padx=10)

        # =================================================Cold Drink Frame===============================================
        F4 = LabelFrame(self.root, text="Cold Drink", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),fg="yellow", bg=bg_color, )
        F4.place(x=610, y=160, width=300, height=380)

        maza_lbl = Label(F4, text="Maza", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rmaza_text = Entry(F4, width=10, font="ts 15",textvariable=self.maza, bd=5, relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        cock_lbl = Label(F4, text="Cock", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        cock_text = Entry(F4, width=10, font="ts 15",textvariable=self.cock, bd=5, relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        frooti_lbl = Label(F4, text="Frooti", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        frooti_text = Entry(F4, width=10, font="ts 15",textvariable=self.frooti, bd=5, relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        tup_lbl = Label(F4, text="Thumbs Up", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        tup_text = Entry(F4, width=10, font="ts 15",textvariable=self.thumbs_up, bd=5, relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        limca_lbl = Label(F4, text="Limca", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        limca_text = Entry(F4, width=10, font="ts 15",textvariable=self.limca, bd=5, relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        sprite_lbl = Label(F4, text="Sprite", bg=bg_color, fg="lightgreen", font=("times new roman", 16, "bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        sprite_text = Entry(F4, width=10, font="ts 15",textvariable=self.sprite, bd=5, relief=SUNKEN).grid(row=5, column=1, pady=10, padx=10)

        # =================================================Bill Area===============================================
        F5 = LabelFrame(self.root,bd=10, relief=GROOVE, bg="white", )
        F5.place(x=917, y=160, width=360, height=380)
        bill_title=Label(F5,text="Bill Area",bd=7,relief=GROOVE,font=("times new roman", 16, "bold")).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #===================================================Button Frame===================================================
        F6 = LabelFrame(self.root, text="Bill Menu", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),fg="yellow", bg=bg_color, )
        F6.place(x=0, y=545, relwidth=1,height=145)

        m1_lbl=Label(F6,text='Total Cosmetics Price',bg=bg_color,fg='white',font=("times new roman", 14, "bold")).grid(row=0,column=0,pady=1,sticky='w')
        m1_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.cosmetics_price,bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=2)

        m2_lbl = Label(F6, text='Total Grocery Price', bg=bg_color, fg='white',font=("times new roman", 14, "bold")).grid(row=1, column=0, pady=1, sticky='w')
        m2_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.grocery_price, bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=2)

        m3_lbl = Label(F6, text='Total Cold Drink Price', bg=bg_color, fg='white',font=("times new roman", 14, "bold")).grid(row=2, column=0, pady=1, sticky='w')
        m3_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.cold_drink_price, bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=2)

        t1_lbl = Label(F6, text='Cosmetics Tax', bg=bg_color, fg='white',font=("times new roman", 14, "bold")).grid(row=0, column=2, pady=1, sticky='w')
        t1_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.cosmetics_tax, bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=2)

        t2_lbl = Label(F6, text='Grocery Tax', bg=bg_color, fg='white',font=("times new roman", 14, "bold")).grid(row=1, column=2, pady=1, sticky='w')
        t2_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.grocery_tax, bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=2)

        t3_lbl = Label(F6, text='Cold Drink Tax', bg=bg_color, fg='white',font=("times new roman", 14, "bold")).grid(row=2, column=2, pady=1, sticky='w')
        t3_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.cold_drink_tax, bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=2)

        btn_F=Frame(F6,bd=12,relief=GROOVE)
        btn_F.place(x=660,y=3,width=595,height=100)
        total_btn=Button(btn_F,command=self.total,text="Total",bd=5,bg="cadetblue",fg="white",font="bold",pady=7,padx=20,).grid(row=0,column=0,padx=9,pady=7)
        gbill_btn = Button(btn_F,command=self.bill_area, text="Generate Bill",bd=5, bg="cadetblue", fg="white", font="bold", pady=7, padx=20, ).grid(row=0,column=1,padx=7,pady=7)
        clear_btn = Button(btn_F, text="Clear",command=self.clear_data, bg="cadetblue",bd=5, fg="white", font="bold", pady=7, padx=20, ).grid(row=0,column=2,padx=7,pady=7)
        exit_btn = Button(btn_F, text="Exit",command=self.exit, bg="cadetblue", fg="white",bd=5, font="bold", pady=7, padx=28, ).grid(row=0,column=3,padx=14,pady=7)

        self.welcome_bill()


    def total(self):
        self.c_s_p=self.soap.get() * 40
        self.c_fc_p=self.face_cream.get() * 120
        self.c_fw_p=self.face_wash.get() * 60
        self.c_hg_p=self.hair_gail.get() * 140
        self.c_bl_p=self.body_loshan.get() * 160
        self.c_bs_p=self.body_spray.get() * 180

        self.total_cosmetics_price=float(
            self.c_s_p +
            self.c_fc_p +
            self.c_fw_p +
            self.c_hg_p +
            self.c_bl_p +
            self.c_bs_p
        )
        self.cosmetics_price.set("Rs.   "+str(self.total_cosmetics_price))
        self.c_tax=round((self.total_cosmetics_price*0.05),2)
        self.cosmetics_tax.set("Rs.   "+str(self.c_tax))

        self.g_rice_p=self.rice.get() * 40
        self.g_foil_p=self.food_oil.get() * 120
        self.g_daal_p=self.daal.get() * 140
        self.g_wheat_p=self.wheat.get() * 20
        self.g_sugar_p=self.sugar.get() * 45
        self.g_tea_p=self.tea.get() * 80


        self.total_grocery_price = float(
            self.g_rice_p +
            self.g_foil_p +
            self.g_daal_p +
            self.g_wheat_p +
            self.g_sugar_p +
            self.g_tea_p
        )
        self.grocery_price.set("Rs.   "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price * 0.1),2)
        self.grocery_tax.set("Rs.   "+str(self.g_tax))

        self.g_maza_p =self.maza.get() * 70
        self.g_cock_p =self.cock.get() * 120
        self.g_frooti_p =self.frooti.get() * 80
        self.g_tu_p =self.thumbs_up.get() * 100
        self.g_limca_p =self.limca.get() * 95
        self.g_sprite_p =self.sprite.get() * 90


        self.total_cold_drink_price = float(
            self.g_maza_p +
            self.g_cock_p +
            self.g_frooti_p +
            self.g_tu_p +
            self.g_limca_p +
            self.g_sprite_p
        )
        self.cold_drink_price.set("Rs.   "+str(self.total_cold_drink_price))
        self.d_tax=round((self.total_cold_drink_price * 0.05), 2)
        self.cold_drink_tax.set("Rs.   " + str( self.d_tax))

        self.Total_bill=float(self.total_cosmetics_price+self.total_grocery_price+self.total_cold_drink_price+self.c_tax+self.g_tax+self.d_tax)

    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END, "\t\t  WELCOME\n")
        self.textarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number : {self.c_phone.get()}")
        self.textarea.insert(END, f"\n ======================================")
        self.textarea.insert(END, f"\n Products\t\tQuantity\t\tPrice")
        self.textarea.insert(END, f"\n ======================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer Details are must")
        elif self.cosmetics_price.get()=="Rs.   0.0" and self.grocery_price.get()=="Rs.   0.0" and self.cold_drink_price.get()=="Rs.   0.0":
            messagebox.showerror("Error","No products are selected")
        else:

            self.welcome_bill()

            #======Cosmatics=======
            if self.soap.get()!=0:
                self.textarea.insert(END, f"\n Bath Soap\t\t  {self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.textarea.insert(END, f"\n Face Cream\t\t  {self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.textarea.insert(END, f"\n Face Wash\t\t  {self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.hair_gail.get()!=0:
                self.textarea.insert(END, f"\n Hair Gail\t\t  {self.hair_gail.get()}\t\t{self.c_hg_p}")
            if self.body_loshan.get()!=0:
                self.textarea.insert(END, f"\n Body Loashan\t\t  {self.body_loshan.get()}\t\t{self.c_bl_p}")
            if self.body_spray.get()!=0:
                self.textarea.insert(END, f"\n Body Spray\t\t  {self.body_spray.get()}\t\t{self.c_bs_p}")

            # ======Grocery=======
            if self.rice.get() != 0:
                self.textarea.insert(END, f"\n Rice\t\t  {self.rice.get()}\t\t{self.g_rice_p}")
            if self.food_oil.get() != 0:
                self.textarea.insert(END, f"\n Food Oil\t\t  {self.food_oil.get()}\t\t{self.g_foil_p}")
            if self.daal.get() != 0:
                self.textarea.insert(END, f"\n Daal\t\t  {self.daal.get()}\t\t {self.g_daal_p}")
            if self.wheat.get() != 0:
                self.textarea.insert(END, f"\n Wheat\t\t  {self.wheat.get()}\t\t{self.g_wheat_p}")
            if self.sugar.get() != 0:
                self.textarea.insert(END, f"\n Sugar\t\t  {self.sugar.get()}\t\t{self.g_sugar_p}")
            if self.tea.get() != 0:
                self.textarea.insert(END, f"\n Tea\t\t  {self.tea.get()}\t\t{self.g_tea_p}")

            # ======Cold Drink=======
            if self.maza.get() != 0:
                self.textarea.insert(END, f"\n Maza\t\t  {self.maza.get()}\t\t {self.g_maza_p}")
            if self.cock.get() != 0:
                self.textarea.insert(END, f"\n Cock\t\t  {self.cock.get()}\t\t{self.g_cock_p}")
            if self.frooti.get() != 0:
                self.textarea.insert(END, f"\n Frooti\t\t  {self.frooti.get()}\t\t{self.g_frooti_p}")
            if self.thumbs_up.get() != 0:
                self.textarea.insert(END, f"\n Thumbs Up\t\t  {self.thumbs_up.get()}\t\t{self.g_tu_p}")
            if self.limca.get() != 0:
                self.textarea.insert(END, f"\n Limca\t\t  {self.limca.get()}\t\t{self.g_limca_p}")
            if self.sprite.get() != 0:
                self.textarea.insert(END, f"\n Sprite\t\t  {self.sprite.get()}\t\t{self.g_sprite_p}")

            self.textarea.insert(END, f"\n --------------------------------------")
            if self.cosmetics_tax.get()!="Rs.   0.0":
                self.textarea.insert(END, f"\n Cosmetics Tax\t\t\t  {self.cosmetics_tax.get()}")
            if self.grocery_tax.get()!="Rs.   0.0":
                self.textarea.insert(END, f"\n Grocery Tax\t\t\t  {self.grocery_tax.get()}")
            if self.cold_drink_tax.get()!="Rs.   0.0":
                self.textarea.insert(END, f"\n Cold Drink Tax\t\t\t  {self.cold_drink_tax.get()}")
            self.textarea.insert(END, f"\n --------------------------------------")

            self.textarea.insert(END, f"\n Total Bill :\t\t\t Rs.   {str(self.Total_bill)}")
            self.textarea.insert(END, f"\n --------------------------------------")

            self.save_bill()


    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill")
        if op>0:
            self.bill_data=self.textarea.get("1.0",END)
            f1=open("all_bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved Bill", f"Bill No.{self.bill_no.get()} saved successfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("all_bills/"):
            if i.split('.')[0]==self.search_bill.get():
                k1=open(f"all_bills/{i}","r")
                self.textarea.delete('1.0',END)
                for d in k1:
                    self.textarea.insert(END,d)
                k1.close()
                present="yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid bill no.")

    def clear_data(self):
        # ==================================================Cosmetics====================================================
        self.soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.hair_gail.set(0)
        self.body_loshan.set(0)
        self.body_spray.set(0)

        # ==================================================Grocery======================================================
        self.rice.set(0)
        self.food_oil.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.tea.set(0)

        # ==================================================Cold Drink===================================================
        self.maza.set(0)
        self.cock.set(0)
        self.frooti.set(0)
        self.thumbs_up.set(0)
        self.limca.set(0)
        self.sprite.set(0)

        # ============================================Product Price & Tax================================================
        self.cosmetics_price.set(" ")
        self.grocery_price.set(" ")
        self.cold_drink_price.set(" ")

        self.cosmetics_tax.set(" ")
        self.grocery_tax.set(" ")
        self.cold_drink_tax.set(" ")

        # ==================================================Customer=====================================================
        self.c_name.set(" ")
        self.c_phone.set(" ")
        self.bill_no.set(" ")
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill.set(" ")
        self.welcome_bill()

    def exit(self):
        op=messagebox.askyesno("Exit","Do you want to exit")
        if op>0:
            self.root.destroy()

root = Tk()
obj = Billing_System(root)
root.mainloop()