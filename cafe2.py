from tkinter import *
import os
import random
import time
import datetime
os.system('cls')
root=Tk()
root.geometry("1350x750+0+0")
root.title("Cafe Management System")
root.configure(background="black")

Tops=Frame(root,width=1350,height=100,bd=14,relief="raise")
Tops.pack(side=TOP)

f1=Frame(root,width=900,height=650,bd=8,relief="raise")
f1.pack(side=LEFT)
f2=Frame(root,width=440,height=650,bd=8,relief="raise")
f2.pack(side=RIGHT)

ft2=Frame(f2,width=440,height=650,bd=12,relief="raise")
ft2.pack(side=TOP)
fb2=Frame(f2,width=440,height=50,bd=16,relief="raise")
fb2.pack(side=BOTTOM )

f1a=Frame(f1,width=900,height=330,bd=8,relief="raise")
f1a.pack(side=TOP)
f2a=Frame(f1,width=900,height=320,bd=6,relief="raise")
f2a.pack(side=BOTTOM)

f1aa=Frame(f1a,width=400,height=330,bd=16,relief="raise")
f1aa.pack(side=LEFT)
f1ab=Frame(f1a,width=400,height=330,bd=16,relief="raise")
f1ab.pack(side=RIGHT)

f2aa=Frame(f2a,width=450,height=330,bd=14,relief="raise")
f2aa.pack(side=LEFT)

f2ab=Frame(f2a,width=450,height=330,bd=14,relief="raise")
f2ab.pack(side=RIGHT)

Tops.configure(background="black")
f1.configure(background="black")
f2.configure(background="black")

#***************************************Cost of Items*************************************
def CostofItem():
    Item1=float(E_Tea.get())
    Item2=float(E_Coffee.get())
    Item3=float(E_Pepsi.get())
    Item4=float(E_Frooti.get())
    Item5=float(E_Dew.get())
    Item6=float(E_Juice.get())
    Item7=float(E_Bisleri.get())
    Item8=float(E_Sprite.get())

    Item9=float(E_Samosa.get())
    Item10=float(E_Thali.get())
    Item11=float(E_Eggs.get())
    Item12=float(E_Pastri.get())
    Item13=float(E_Chips.get())
    Item14=float(E_Burger.get())
    Item15=float(E_Biscuit.get())
    Item16=float(E_Noodles.get())

    PriceofDrinks = (Item1 * 10) + (Item2 * 15) + (Item3 * 12) + (Item4 * 10) + (Item5 * 15) + (Item6 * 30) + (Item7 * 15) + (Item8 * 15)

    PriceofFoods = (Item9 * 15) + (Item10 * 35) + (Item11 * 20) + (Item12 * 20) + (Item13 * 10) + (Item14 * 15) + (Item15 * 10) + (Item16 * 20)

    DrinksPrice='Rs. %0.2f'%(PriceofDrinks)
    FoodsPrice='Rs. %0.2f'%(PriceofFoods)
    CostofFoods.set(FoodsPrice)
    CostofDrinks.set(DrinksPrice)
    y=(PriceofDrinks+PriceofFoods)
    SC='Rs.%0.2f'%(y*0.10)
    ServiceCharge.set(SC)

    SubTotalofITEMS='Rs. %0.2f'%(PriceofDrinks+PriceofFoods )
    SubTotal.set(SubTotalofITEMS)

    Tax='Rs. %0.2f'%(y*0.15)
    PaidTax.set(Tax)
    TC='Rs. %0.2f'%(SubTotalofITEMS+ SC +Tax)
    TotalCost.set(TC)


def qExit():
    root.destroy()
    return


def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    CostofFoods.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)

    E_Tea.set("0")
    E_Coffee.set("0")
    E_Pepsi.set("0")
    E_Frooti.set("0")
    E_Dew.set("0")
    E_Juice.set("0")
    E_Bisleri.set("0")
    E_Sprite.set("0")


    E_Samosa.set("0")
    E_Thali.set("0")
    E_Eggs.set("0")
    E_Pastri.set("0")
    E_Chips.set("0")
    E_Burger.set("0")
    E_Biscuit.set("0")
    E_Noodles.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txtTea.configure(state=DISABLED)
    txtCoffee.configure(state=DISABLED)
    txtPepsi.configure(state=DISABLED)
    txtFrooti.configure(state=DISABLED)
    txtDew.configure(state=DISABLED)
    txtJuice.configure(state=DISABLED)
    txtBisleri.configure(state=DISABLED)
    txtSprite.configure(state=DISABLED)


    txtSamosa.configure(state=DISABLED)
    txtThali.configure(state=DISABLED)
    txtEggs.configure(state=DISABLED)
    txtPastri.configure(state=DISABLED)
    txtChips.configure(state=DISABLED)
    txtBurger.configure(state=DISABLED)
    txtBiscuit.configure(state=DISABLED)
    txtNoodles.configure(state=DISABLED)

def Receipt():
    txtReceipt.delete("1.0",END)
    x = random.randint(200, 500)
    randomRef = str(x)
    Receipt_Ref,set("BILL"+ randomRef)
    txtReceipt.insert(END,'                                 Green Hut Cafe                   \n')
    txtReceipt.insert(END,'Receipt Ref:             ' +Receipt_Ref.get()+ '                  ' +DateofOrder.get()+ "\n")
    txtReceipt.insert(END,'Items                    ' + 'Quantity of Items \n')
    txtReceipt.insert(END,'Tea:                      ' +E_Tea.get()+ "\n")
    txtReceipt.insert(END,'Coffee:                 ' +E_Coffee.get()+ "\n")
    txtReceipt.insert(END,'Pepsi:                   ' +E_Pepsi.get()+ "\n")
    txtReceipt.insert(END,'Frooti:                  ' +E_Frooti.get()+ "\n")
    txtReceipt.insert(END,'Dew:                     ' +E_Dew.get()+ " \n")
    txtReceipt.insert(END,'Juice:                   ' +E_Juice.get()+ "\n")
    txtReceipt.insert(END,'Bisleri:                 ' +E_Bisleri.get()+ "\n")
    txtReceipt.insert(END,'Sprite:                  ' +E_Sprite.get()+ "\n")
    txtReceipt.insert(END,'Samosa:               ' +E_Samosa.get()+ "\n")
    txtReceipt.insert(END,'Thali:                   ' +E_Thali.get()+ "\n")
    txtReceipt.insert(END,'Eggs:                   ' +E_Eggs.get()+ "\n")
    txtReceipt.insert(END,'Pastri:                  ' +E_Pastri.get()+ "\n")
    txtReceipt.insert(END,'Chips:                  ' +E_Chips.get()+ "\n")
    txtReceipt.insert(END,'Burger:                ' +E_Burger.get()+ "\n")
    txtReceipt.insert(END,'Biscuit:                ' +E_Biscuit.get()+ "\n")
    txtReceipt.insert(END,'Noodles:              ' +E_Noodles.get()+ "\n")
    txtReceipt.insert(END,'Cost of Drinks:' +CostofDrinks.get()+ '        Tax paid:' +PaidTax.get()+ "\n")
    txtReceipt.insert(END,'Cost of Foods:' +CostofFoods.get()+ '        Subtotal:' +SubTotal.get()+ "\n")
    txtReceipt.insert(END,'Service Charge:' +ServiceCharge.get()+ '        Total Cost:' +TotalCost.get()+ "\n")

#*************************************Heading*******************
lblInfo=Label(Tops,font=("arial",70,"bold"),text="   Cafeteria For You   ",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)


#*************************************************Calculator**********************
def chkbutton_value():
    if (var1.get()==1):
        txtTea.configure(state=NORMAL)
    elif var1.get()==0:
        txtTea.configure(state=DISABLED)
        E_Tea.set("0")
    if (var2.get()==1):
        txtCoffee.configure(state=NORMAL)
    elif var2.get()==0:
        txtCoffee.configure(state=DISABLED)
        E_Coffee.set("0")
    if (var3.get()==1):
        txtPepsi.configure(state=NORMAL)
    elif var3.get()==0:
        txtPepsi.configure(state=DISABLED)
        E_Pepsi.set("0")
    if (var4.get()==1):
        txtFrooti.configure(state=NORMAL)
    elif var4.get()==0:
        txtFrooti.configure(state=DISABLED)
        E_Frooti.set("0")
    if (var5.get()==1):
        txtDew.configure(state=NORMAL)
    elif var5.get()==0:
        txtDew.configure(state=DISABLED)
        E_Dew.set("0")
    if (var6.get()==1):
        txtJuice.configure(state=NORMAL)
    elif var6.get()==0:
        txtJuice.configure(state=DISABLED)
        E_Juice.set("0")
    if (var7.get()==1):
        txtBisleri.configure(state=NORMAL)
    elif var7.get()==0:
        txtBisleri.configure(state=DISABLED)
        E_Bisleri.set("0")
    if (var8.get()==1):
        txtSprite.configure(state=NORMAL)
    elif var8.get()==0:
        txtSprite.configure(state=DISABLED)
        E_Sprite.set("0")
    if (var9.get()==1):
        txtSamosa.configure(state=NORMAL)
    elif var9.get()==0:
        txtSamosa.configure(state=DISABLED)
        E_Samosa.set("0")
    if (var10.get()==1):
        txtThali.configure(state=NORMAL)
    elif var10.get()==0:
        txtThali.configure(state=DISABLED)
        E_Thali.set("0")
    if (var11.get()==1):
        txtEggs.configure(state=NORMAL)
    elif var11.get()==0:
        txtEggs.configure(state=DISABLED)
        E_Eggs.set("0")
    if (var12.get()==1):
        txtPastri.configure(state=NORMAL)
    elif var12.get()==0:
        txtPastri.configure(state=DISABLED)
        E_Pastri.set("0")
    if (var13.get()==1):
        txtChips.configure(state=NORMAL)
    elif var13.get()==0:
        txtChips.configure(state=DISABLED)
        E_Chips.set("0")
    if (var14.get()==1):
        txtBurger.configure(state=NORMAL)
    elif var14.get()==0:
        txtBurger.configure(state=DISABLED)
        E_Burger.set("0")
    if (var15.get()==1):
        txtBiscuit.configure(state=NORMAL)
    elif var15.get()==0:
        txtBiscuit.configure(state=DISABLED)
        E_Biscuit.set("0")
    if (var16.get()==1):
        txtNoodles.configure(state=NORMAL)
    elif var16.get()==0:
        txtNoodles.configure(state=DISABLED)
        E_Noodles.set("0")

#**************************Variables*******************************************
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateofOrder=StringVar()
Receipt_Ref=StringVar()
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofFoods=StringVar()
CostofDrinks=StringVar()
ServiceCharge=StringVar()

E_Tea=StringVar()
E_Coffee=StringVar()
E_Pepsi=StringVar()
E_Frooti=StringVar()
E_Dew=StringVar()
E_Juice=StringVar()
E_Bisleri=StringVar()
E_Sprite=StringVar()


E_Samosa=StringVar()
E_Thali=StringVar()
E_Eggs=StringVar()
E_Pastri=StringVar()
E_Chips=StringVar()
E_Burger=StringVar()
E_Biscuit=StringVar()
E_Noodles=StringVar()

E_Tea.set("0")
E_Coffee.set("0")
E_Pepsi.set("0")
E_Frooti.set("0")
E_Dew.set("0")
E_Juice.set("0")
E_Bisleri.set("0")
E_Sprite.set("0")


E_Samosa.set("0")
E_Thali.set("0")
E_Eggs.set("0")
E_Pastri.set("0")
E_Chips.set("0")
E_Burger.set("0")
E_Biscuit.set("0")
E_Noodles.set("0")

DateofOrder.set(time.strftime("%d/%m/%Y"))


#*****************Drink************************
Tea=Checkbutton(f1aa,text="Tea Rs.10/unit \t",variable=var1,onvalue=1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row=0,sticky=W)
Coffee=Checkbutton(f1aa,text="Coffee Rs.15/unit\t",variable=var2,onvalue=1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row=1,sticky=W)
Pepsi=Checkbutton(f1aa,text="Pepsi Rs.12/unit \t",variable=var3,onvalue=1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row=2,sticky=W)
Frooti=Checkbutton(f1aa,text="Frooti Rs.10/unit\t",variable=var4,onvalue=1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row=3,sticky=W)
Dew=Checkbutton(f1aa,text="Dew Rs.15/unit\t",variable=var5,onvalue=1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row=4,sticky=W)
Juice=Checkbutton(f1aa,text="Juice Rs.30/unit\t",variable=var6,onvalue=1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row=5,sticky=W)
Bisleri=Checkbutton(f1aa,text="Bisleri Rs.15/unit\t",variable=var7,onvalue=1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row=6,sticky=W)
Sprite=Checkbutton(f1aa,text="Sprite Rs.15/unit\t",variable=var8,onvalue=1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row=7,sticky=W)
#**********************Food*************************
Samosa=Checkbutton(f1ab,text="Samosa Rs.15/unit\t",variable=var9,onvalue=1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row=0,sticky=W)
Thali=Checkbutton(f1ab,text="Thali Rs.35/unit\t",variable=var10,onvalue=1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row=1,sticky=W)
Eggs=Checkbutton(f1ab,text="Eggs Rs.20/unit\t",variable=var11,onvalue=1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row=2,sticky=W)
Pastri=Checkbutton(f1ab,text="Pastri Rs.20/unit\t",variable=var12,onvalue=1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row=3,sticky=W)
Chips=Checkbutton(f1ab,text="Chips Rs.10/unit\t",variable=var13,onvalue=1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row=4,sticky=W)
Burger=Checkbutton(f1ab,text="Burger Rs.15/unit\t",variable=var14,onvalue=1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row=5,sticky=W)
Biscuit=Checkbutton(f1ab,text="Biscuit Rs.10/unit\t",variable=var15,onvalue=1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row=6,sticky=W)
Noodles=Checkbutton(f1ab,text="Noodles Rs.20/unit\t",variable=var16,onvalue=1,offvalue=0,font=("arial",18,"bold"),command=chkbutton_value).grid(row=7,sticky=W)

#*****************Enter widget for drink************************
txtTea=Entry(f1aa,font=('arial',16,'bold'),textvariable=E_Tea,bd=8,width=6,justify='left',state=DISABLED)
txtTea.grid(row=0,column=1)
txtCoffee=Entry(f1aa,font=('arial',16,'bold'),textvariable=E_Coffee,bd=8,width=6,justify='left',state=DISABLED)
txtCoffee.grid(row=1,column=1)
txtPepsi=Entry(f1aa,font=('arial',16,'bold'),textvariable=E_Pepsi,bd=8,width=6,justify='left',state=DISABLED)
txtPepsi.grid(row=2,column=1)
txtFrooti=Entry(f1aa,font=('arial',16,'bold'),textvariable=E_Frooti,bd=8,width=6,justify='left',state=DISABLED)
txtFrooti.grid(row=3,column=1)
txtDew=Entry(f1aa,font=('arial',16,'bold'),textvariable=E_Dew,bd=8,width=6,justify='left',state=DISABLED)
txtDew.grid(row=4,column=1)
txtJuice=Entry(f1aa,font=('arial',16,'bold'),textvariable=E_Juice,bd=8,width=6,justify='left',state=DISABLED)
txtJuice.grid(row=5,column=1)
txtBisleri=Entry(f1aa,font=('arial',16,'bold'),textvariable=E_Bisleri,bd=8,width=6,justify='left',state=DISABLED)
txtBisleri.grid(row=6,column=1)
txtSprite=Entry(f1aa,font=('arial',16,'bold'),textvariable=E_Sprite,bd=8,width=6,justify='left',state=DISABLED)
txtSprite.grid(row=7,column=1)

#*****************widget for Foods************************
txtSamosa=Entry(f1ab,font=('arial',16,'bold'),textvariable=E_Samosa,bd=8,width=6,justify='left',state=DISABLED)
txtSamosa.grid(row=0,column=1)
txtThali=Entry(f1ab,font=('arial',16,'bold'),textvariable=E_Thali,bd=8,width=6,justify='left',state=DISABLED)
txtThali.grid(row=1,column=1)
txtEggs=Entry(f1ab,font=('arial',16,'bold'),textvariable=E_Eggs,bd=8,width=6,justify='left',state=DISABLED)
txtEggs.grid(row=2,column=1)
txtPastri=Entry(f1ab,font=('arial',16,'bold'),textvariable=E_Pastri,bd=8,width=6,justify='left',state=DISABLED)
txtPastri.grid(row=3,column=1)
txtChips=Entry(f1ab,font=('arial',16,'bold'),textvariable=E_Chips,bd=8,width=6,justify='left',state=DISABLED)
txtChips.grid(row=4,column=1)
txtBurger=Entry(f1ab,font=('arial',16,'bold'),textvariable=E_Burger,bd=8,width=6,justify='left',state=DISABLED)
txtBurger.grid(row=5,column=1)
txtBiscuit=Entry(f1ab,font=('arial',16,'bold'),textvariable=E_Biscuit,bd=8,width=6,justify='left',state=DISABLED)
txtBiscuit.grid(row=6,column=1)
txtNoodles=Entry(f1ab,font=('arial',16,'bold'),textvariable=E_Noodles,bd=8,width=6,justify='left',state=DISABLED)
txtNoodles.grid(row=7,column=1)


#******************************Item cost Info*************************
lblCostofDrinks=Label(f2aa,font=('arial',16,'bold'),text='Cost of Drinks',bd=8,anchor='w')
lblCostofDrinks.grid(row=2,column=0,sticky=W)
txtCostofDrinks=Entry(f2aa,font=('arial',16,'bold'),textvariable=CostofDrinks,bd=8,insertwidth=2,justify='left')
txtCostofDrinks.grid(row=2,column=1)

lblCostofFoods=Label(f2aa,font=('arial',16,'bold'),text='Cost of Food',bd=8,anchor='w')
lblCostofFoods.grid(row=3,column=0,sticky=W)
txtCostofFoods=Entry(f2aa,font=('arial',16,'bold'),textvariable=CostofFoods,bd=8,insertwidth=2, justify='left')
txtCostofFoods.grid(row=3,column=1)

lblServiceCharge=Label(f2aa,font=('arial',16,'bold'),text='Service Charge',bd=8,anchor='w')
lblServiceCharge.grid(row=4,column=0,sticky=W)
txtServiceCharge=Entry(f2aa,font=('arial',16,'bold'),textvariable=ServiceCharge,bd=8,insertwidth=2, justify='left')
txtServiceCharge.grid(row=4,column=1)

#******************************Payment Info*************************
lblPaidTax=Label(f2ab,font=('arial',16,'bold'),text='GST',bd=8)
lblPaidTax.grid(row=2,column=0,sticky=W)
txtPaidTax=Entry(f2ab,font=('arial',16,'bold'),textvariable=PaidTax,bd=8,justify='left')
txtPaidTax.grid(row=2,column=1)

lblSubTotal=Label(f2ab,font=('arial',16,'bold'),text='Sub Total',bd=8)
lblSubTotal.grid(row=3,column=0,sticky=W)
txtSubTotal=Entry(f2ab,font=('arial',16,'bold'),textvariable=SubTotal,bd=8, insertwidth=2,justify='left')
txtSubTotal.grid(row=3,column=1)

lblTotalCost=Label(f2ab,font=('arial',16,'bold'),text='Total',bd=8)
lblTotalCost.grid(row=4,column=0,sticky=W)
txtTotalCost=Entry(f2ab,font=('arial',16,'bold'),textvariable=TotalCost,bd=8,insertwidth=2,justify='left')
txtTotalCost.grid(row=4,column=1)


#******************************Info*************************
lblReceipt=Label(ft2,font=('arial',12,'bold'),text='Receipt:',bd=2,anchor='w')
lblReceipt.grid(row=0,column=0,sticky=W)
txtReceipt=Text(ft2,width=59,height=22,bg="white",bd=8,font=('arial',11,'bold'))
txtReceipt.grid(row=1,column=0)

#****************************Buttons************************
btnTotal=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Total",command=CostofItem).grid(row=0,column=0)
btnReceipt=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Receipt",command=Receipt).grid(row=0,column=1)
btnReset=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Reset",command=Reset).grid(row=0,column=2)
btnExit=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Exit",command=qExit).grid(row=0,column=3)

root.mainloop()
