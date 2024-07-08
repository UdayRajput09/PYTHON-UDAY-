# import messagebox and END from the tkinter
from tkinter import messagebox
from tkinter import END

# creating function named total
def total(self):

    # condition for checking the customer_info field is not empty 
    if (self.c_name.get=="" or self.phone.get()==""):
        messagebox.showerror("Error", "Fill the complete Customer Details!!")
        # getting snack  values
    self.nu=self.nutella.get()*120
    self.no=self.noodles.get()*40
    self.la=self.lays.get()*10
    self.ore=self.oreo.get()*20
    self.mu=self.muffin.get()*30
    self.si=self.silk.get()*60
    self.na=self.namkeen.get()*15
    # total of snacks_price
    total_snacks_price=(
                self.nu+
                self.no+
                self.la+
                self.ore+
                self.mu+
                self.si+
                self.na)
    self.total_sna.set(str(total_snacks_price)+" Rs")
    self.a.set(str(round(total_snacks_price*0.05,3))+" Rs")

    # getting grocery value
    self.at=self.atta.get()*42
    self.pa=self.pasta.get()*120
    self.oi=self.oil.get()*113
    self.ri=self.rice.get()*160
    self.su=self.sugar.get()*55
    self.te=self.tea.get()*480
    self.da=self.dal.get()*76

    # total of grocery_price
    total_grocery_price=(
        self.at+
        self.pa+
        self.oi+
        self.ri+
        self.su+
        self.te+
        self.da)

    self.total_gro.set(str(total_grocery_price)+" Rs")
    self.b.set(str(round(total_grocery_price*0.01,3))+" Rs")

    # getting hygine value
    self.so=self.soap.get()*30
    self.sh=self.shampoo.get()*180
    self.cr=self.cream.get()*130
    self.lo=self.lotion.get()*500
    self.fo=self.foam.get()*85
    self.ma=self.mask.get()*100
    self.sa=self.sanitizer.get()*20

    #total of hygin_price
    total_hygine_price=(
        self.so+
        self.sh+
        self.cr+
        self.lo+
        self.fo+
        self.ma+
        self.sa)

    self.total_hyg.set(str(total_hygine_price)+" Rs")
    self.c.set(str(round(total_hygine_price*0.10,3))+" Rs")

    # total of whole bill
    self.total_all_bill=(total_snacks_price+
                total_grocery_price+
                total_hygine_price+
                (round(total_grocery_price*0.01,3))+
                (round(total_hygine_price*0.10,3))+
                (round(total_snacks_price*0.05,3)))
    self.total_all_bil=str(self.total_all_bill)+" Rs"
    billarea(self)

# function for intro
def intro(self):
    self.txtarea.delete(1.0,END)
    self.txtarea.insert(END,"\tWELCOME TO SUPER MARKET\n\tPhone-No.739275410")
    self.txtarea.insert(END,f"\n\nBill no. : {self.bill_no.get()}")
    self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
    self.txtarea.insert(END,f"\nPhone No. : {self.phone.get()}")
    self.txtarea.insert(END,"\n====================================\n")
    self.txtarea.insert(END,"\nProduct\t\tQty\tPrice\n")
    self.txtarea.insert(END,"\n====================================\n")
# function for billarea
def billarea(self):
    intro(self)
    if self.nutella.get()!=0:
        self.txtarea.insert(END,f"Nutella\t\t {self.nutella.get()}\t{self.nu}\n")
    if self.noodles.get()!=0:
        self.txtarea.insert(END,f"Noodles\t\t {self.noodles.get()}\t{self.no}\n")
    if self.lays.get()!=0:
        self.txtarea.insert(END,f"Lays\t\t {self.lays.get()}\t{self.la}\n")
    if self.oreo.get()!=0:
        self.txtarea.insert(END,f"Oreo\t\t {self.oreo.get()}\t{self.ore}\n")
    if self.muffin.get()!=0:
        self.txtarea.insert(END,f"Muffins\t\t {self.muffin.get()}\t{self.mu}\n")
    if self.silk.get()!=0:
        self.txtarea.insert(END,f"Silk\t\t {self.silk.get()}\t{self.si}\n")
    if self.namkeen.get()!=0:
        self.txtarea.insert(END,f"Namkeen\t\t {self.namkeen.get()}\t{self.na}\n")
    if self.atta.get()!=0:
        self.txtarea.insert(END,f"Atta\t\t {self.atta.get()}\t{self.at}\n")
    if self.pasta.get()!=0:
        self.txtarea.insert(END,f"Pasta\t\t {self.pasta.get()}\t{self.pa}\n")
    if self.rice.get()!=0:
        self.txtarea.insert(END,f"Rice\t\t {self.rice.get()}\t{self.ri}\n")
    if self.oil.get()!=0:
        self.txtarea.insert(END,f"Oil\t\t {self.oil.get()}\t{self.oi}\n")
    if self.sugar.get()!=0:
        self.txtarea.insert(END,f"Sugar\t\t {self.sugar.get()}\t{self.su}\n")
    if self.dal.get()!=0:
        self.txtarea.insert(END,f"Daal\t\t {self.dal.get()}\t{self.da}\n")
    if self.tea.get()!=0:
        self.txtarea.insert(END,f"Tea\t\t {self.tea.get()}\t{self.te}\n")
    if self.soap.get()!=0:
        self.txtarea.insert(END,f"Soap\t\t {self.soap.get()}\t{self.so}\n")
    if self.shampoo.get()!=0:
        self.txtarea.insert(END,f"Shampoo\t\t {self.shampoo.get()}\t{self.sh}\n")
    if self.lotion.get()!=0:
        self.txtarea.insert(END,f"Lotion\t\t {self.lotion.get()}\t{self.lo}\n")
    if self.cream.get()!=0:
        self.txtarea.insert(END,f"Cream\t\t {self.cream.get()}\t{self.cr}\n")
    if self.foam.get()!=0:
        self.txtarea.insert(END,f"Foam\t\t {self.foam.get()}\t{self.fo}\n")
    if self.mask.get()!=0:
        self.txtarea.insert(END,f"Mask\t\t {self.mask.get()}\t{self.ma}\n")
    if self.sanitizer.get()!=0:
        self.txtarea.insert(END,f"Sanitizer\t\t {self.sanitizer.get()}\t{self.sa}\n")

    self.txtarea.insert(END,f"------------------------------------\n")
    if self.a.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Snacks Tax : {self.a.get()}\n")
    if self.b.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Grocery Tax : {self.b.get()}\n")
    if self.c.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Beauty&Hygine Tax : {self.c.get()}\n")
    self.txtarea.insert(END,f"Total Bill Amount : {self.total_all_bil}\n")
    self.txtarea.insert(END,f"------------------------------------\n")

# function for the clear the whole tkinter window
def clear(self):
        self.txtarea.delete(1.0,END)
        self.nutella.set(0)
        self.noodles.set(0)
        self.lays.set(0)
        self.oreo.set(0)
        self.muffin.set(0)
        self.silk.set(0)
        self.namkeen.set(0)
        self.atta.set(0)
        self.pasta.set(0)
        self.rice.set(0)
        self.oil.set(0)
        self.sugar.set(0)
        self.dal.set(0)
        self.tea.set(0)
        self.soap.set(0)
        self.shampoo.set(0)
        self.lotion.set(0)
        self.cream.set(0)
        self.foam.set(0)
        self.mask.set(0)
        self.sanitizer.set(0)
        self.total_sna.set(0)
        self.total_gro.set(0)
        self.total_hyg.set(0)
        self.a.set(0)
        self.b.set(0)
        self.c.set(0)
        self.c_name.set(0)
        self.bill_no.set(0)
        self.bill_no.set(0)
        self.phone.set(0)
# function for the exit the tkinter window 
def exit1(self):
    self.root.destroy()