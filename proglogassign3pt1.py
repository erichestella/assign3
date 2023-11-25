

from tkinter.constants import *
from tkinter import *
from tkinter import messagebox
from datetime import date
import customtkinter



tsu=customtkinter.CTk()
tsu.title('RICH IN FRUITIES')
tsu.geometry("1500x860")
tsu.config(bg="#D7682B")
tsu.resizable(False,False)

font1=('Georgia', 30, 'bold')
font2=('Eras Bold ITC', 30, 'bold')
font3=('Forte', 30, 'bold')
font4=('Cooper Black', 35, 'bold')
font5=('Imprint MT Shadow', 20, 'bold')

price_list=[20, 25]
total_price=0


bill_frame=customtkinter.CTkFrame(tsu,width=350,height=400, fg_color="#EB984E")
bill_frame.place(relx=0.51,rely=0.0)
 


wow_label=customtkinter.CTkLabel(tsu,text="(๑´• .̫ •ू`๑) RICH IN FRUITIES (˵¯͒〰¯͒˵)", font=font4,text_color="black", bg_color="#C39BD3")
wow_label.place(relx=0.02,rely=0.03)


img1=PhotoImage(file=r"download__19_-removebg-preview.png")
img2=PhotoImage(file=r"download__18_-removebg-preview (1).png")
img3=PhotoImage(file=r"eRICH_IN_FRUITIES__1_-removebg-preview.png")
img4=PhotoImage(file=r"download__14_-removebg-preview.png")
img5=PhotoImage(file=r"Calico_Cat_Gifts___Merchandise_for_Sale-removebg-preview.png")
img6=PhotoImage(file=r"Pomeranian_Magnet___Pomeranian-removebg-preview.png")
img7=PhotoImage(file=r"Killer_Chicken_Sticker_by_InvisibleMind-removebg-preview.png")
img8=PhotoImage(file=r"download__16_-removebg-preview.png")


def total():
    global total_price
    if(customer_entry.get()==''):
        messagebox.showwarning(title="Error",message="HEY! YOU FORGOT TO TYPE YOUR NAME :( - SHADEY")
    else:
      total_price=int(quntity1_combobox.get())*price_list[0]+int(quntity2_combobox.get())*price_list[1]
      if(total_price==0):
       messagebox.showwarning(title="Error", message= "Please select how many fruits do you prefer")
      else:
         title_label=customtkinter.CTkLabel(bill_frame, text='Bill Receipt', font=font3, bg_color="#EB984E")
         title_label.place(relx=0.25,rely=0.15)
         name_label=customtkinter.CTkLabel(bill_frame,text=f'Name: {customer_entry.get()}', font=font3, bg_color="#EB984E")
         name_label.place(relx=0.05,rely=0.25)
         price_label=customtkinter.CTkLabel(bill_frame,text=f'Total Price: ₱{total_price}',font=font3, bg_color="#EB984E")
         price_label.place(relx=0.07,rely=0.50)
         date_label=customtkinter.CTkLabel(bill_frame,text=f'Date Today: {date.today()}', font=font3, bg_color="#EB984E")
         date_label.place(relx=0.03,rely=0.38)
         twitter_label=customtkinter.CTkLabel(bill_frame, text='@_RICH_IN_FRUITIES', font=font5, bg_color="#EB984E")
         twitter_label.place(relx=0.15,rely=0.0)

def new():
   if(customer_entry.get()==''):
        messagebox.askyesno(title="Error",message="LOVEY, ARE YOU SURE YOU ARE CREATING NEW? - ILLIA")
   customer_entry.delete(0, END)
   quntity1_combobox.set(0)
   quntity2_combobox.set(0)

def save():
   if(customer_entry.get()==''):
        messagebox.askretrycancel(title="NOTE THIS! >:( )",message="HEY! PLEASE ENTER FIRST YOUR NICKNAME BEFORE ENTERING SAVE!! - MIKASA")
   f= open(f'{customer_entry.get()} Bill', "w")
   f.write(f'Customer Nickname: {customer_entry.get()}\n')
   f.write(f'Total Price: {total_price}₱ \n')
   f.write(f'Bill Date Purchase: {date.today()}')
   messagebox.showinfo(title="SAVED", message= 'BILL HAS BEEN SAVED')



img1_label=customtkinter.CTkLabel(tsu,image=img2, text="APPLES\n Price: ₱ 20", font=font2, text_color="black", fg_color="#E6B0AA", width=270, height=200, compound=TOP, anchor=N)
img1_label.place(relx=0.06,rely=0.17)

img2_label=customtkinter.CTkLabel(tsu,image=img1, text="ORANGES\n Price: ₱ 25", font=font2, text_color="black", fg_color="#E6B0AA", width=270, height=200, compound=TOP, anchor=N)
img2_label.place(relx=0.06,rely=0.58)


img3_label=customtkinter.CTkLabel(tsu,image=img3,text="", font=font2,fg_color="#D7682B", width=130, height=50, compound=TOP, anchor=N)
img3_label.place(relx=0.73,rely=0.0)

img4_label=customtkinter.CTkLabel(tsu, image=img4, text="", font=font2,fg_color="#EB984E", width=130, height=50, compound=TOP, anchor=N )
img4_label.place(relx=0.52, rely=0.27)

img5_label=customtkinter.CTkLabel(tsu, image=img5, text="", font=font2,fg_color="#D7682B", width=130, height=50, compound=TOP, anchor=N )
img5_label.place(relx=0.62, rely=0.76)


img6_label=customtkinter.CTkLabel(tsu, image=img6, text="", font=font2,fg_color="#D7682B", width=130, height=50, compound=TOP, anchor=N )
img6_label.place(relx=0.45, rely=0.76)

img7_label=customtkinter.CTkLabel(tsu, image=img7, text="", font=font2,fg_color="#D7682B", width=130, height=50, compound=TOP, anchor=N )
img7_label.place(relx=0.80, rely=0.76)

img8_label=customtkinter.CTkLabel(tsu, image=img8, text="", font=font2,fg_color="#D7682B", width=130, height=50, compound=TOP, anchor=N )
img8_label.place(relx=0.77, rely=0.42)

quntity1_combobox=customtkinter.CTkComboBox(tsu,font=font3,text_color="white",fg_color="#1F618D", values=('1','2','3','4', '5'), state="readonly")
quntity1_combobox.place(relx=0.29,rely=0.35)
quntity1_combobox.set(0)

quntity2_combobox=customtkinter.CTkComboBox(tsu,font=font3,text_color="white",fg_color="#1F618D", values=('1','2','3','4', '5'), state="readonly")
quntity2_combobox.place(relx=0.29,rely=0.73)
quntity2_combobox.set(0)


nickname_label=customtkinter.CTkLabel(tsu,text= "Your Nickname:", font=font2,text_color="black", fg_color="#AF7AC5", corner_radius=10)
nickname_label.place(relx=0.45, rely=0.58)

customer_entry=customtkinter.CTkEntry(tsu, font=font2, fg_color="#FFBFE9", text_color="black", border_color="black", width=350)
customer_entry.place(relx=0.65, rely=0.58)

total_button=customtkinter.CTkButton(tsu,command=total, text="TOTAL PRICE:", font=font2, text_color="yellow", border_color="black", fg_color="#2E86C1", corner_radius=20, cursor="hand2")
total_button.place(relx=0.43,rely=0.70)

save_button=customtkinter.CTkButton(tsu,command=save, text="SAVE TOTAL:", font=font2, text_color="yellow", border_color="black",fg_color="#2E86C1", corner_radius=20, cursor="hand2")
save_button.place(relx=0.61, rely=0.70)

new_button=customtkinter.CTkButton(tsu,command=new, text="NEW RECEIPT:",font=font2, text_color="yellow", border_color="black", fg_color="#2E86C1",corner_radius=20, cursor="hand2")
new_button.place(relx=0.79,rely=0.70)

quantity_label=customtkinter.CTkLabel(tsu,text="QUANTITY:", font=font2,text_color="black", fg_color="brown", corner_radius=20)
quantity_label.place(relx=0.27,rely=0.28)

quantity_label=customtkinter.CTkLabel(tsu,text="QUANTITY:", font=font2,text_color="black", fg_color="brown", corner_radius=20)
quantity_label.place(relx=0.27,rely=0.65)


tsu.mainloop()
