

import customtkinter 
from tkinter import *
from tkinter import messagebox
from datetime import date
from PIL import ImageTk, Image

rich=customtkinter.CTk()
rich.title('eRICH IN FRUITIES')
rich.geometry("1500x860")
rich.config(bg="pink")
rich.resizable(False,False)

font1=('Bodoni MT Black', 30, 'bold')
font2=('Comic Sans MS', 30, 'bold')
font3=('Eras Bold ITC', 30, 'bold')
font4=('Cooper Black',35, 'bold')
font5=(('Eras Bold ITC', "1"))

price_list=[20, 25, 1]
total_price=0


bill_frame=customtkinter.CTkFrame(rich,width=350,height=400, fg_color="#D5D8DC")
bill_frame.place(relx=0.45,y=0.05)
 
menu_label=customtkinter.CTkLabel(rich,text=" ٩(◕‿◕)۶ RICH IN FRUITIES (っ˘ڡ˘ς)", font=font4,text_color="black", bg_color="#D7BDE2")
menu_label.place(relx=0,rely=0)


img1=PhotoImage(file=r"_Orange__Sticker_for_Sale_by_doodlecarrot-removebg-preview.png")
img2=PhotoImage(file=r"download__13_-removebg-preview.png")
img3=PhotoImage(file=r"eRICH_IN_FRUITIES__1_-removebg-preview.png")
img4=PhotoImage(file=r"Cash_Money_Sticker_by_WRLDS-VIENNA-removebg-preview.png")
img5=PhotoImage(file=r"_cookingmama__cooking_mama__freetoedit-removebg-preview.png")
img6=PhotoImage(file=r"No_sé_xd-removebg-preview.png")
img7=PhotoImage(file=r"Five_youtube_videos_guaranteed_to_make_me_smile-removebg-preview.png")
img8=PhotoImage(file=r"download__15_-removebg-preview.png")

def pay():
    global total_price
    if(customer_entry.get()==''):
        messagebox.showwarning(title="ERROR SPOTTED!!",message="HI, MISS/SIR I THINK YOU FORGOT TO ENTER YOUR NICKNAME. KINDLY PUT IT FIRST BEFORE PROCEEDING. THANK YOU<3- HANGE")
    else:
      total_price=int(quntity1_combobox.get())*price_list[0]-int(quntity3_combobox.get())*price_list[2]+int(quntity2_combobox.get())*price_list[1]
      if(total_price==0):
       messagebox.showwarning(title="Error", message= "PLEASE SELECT THE QUANTITY OF THE FRUITS YOU WANT, THANK YOU<3- TAKINA")
      else:
         bill_label=customtkinter.CTkLabel(bill_frame, text='Bill Receipt', font=font3, bg_color="#D5D8DC")
         bill_label.place(relx=0.20,rely=0.03)
         insta_label=customtkinter.CTkLabel(bill_frame, text='@_RICH_IN_FRUITIES', font=font3, bg_color="#D5D8DC")
         insta_label.place(relx=0.0,rely=0.90)
         name_label=customtkinter.CTkLabel(bill_frame,text=f'Customer: {customer_entry.get()}', font=font2, bg_color="#D5D8DC")
         name_label.place(relx=0.09,rely=0.20)
         price_label=customtkinter.CTkLabel(bill_frame,text=f'Total Change: {total_price}₱',font=font2, bg_color="#D5D8DC" )
         price_label.place(relx=0.09,rely=0.35)
         today_label=customtkinter.CTkLabel(bill_frame,text=f'Date : {date.today()}', font=font2, bg_color="#D5D8DC")
         today_label.place(relx=0.09,rely=0.50)
         


def new():
   global total_price
   if(total_price==0):
       messagebox.askyesno(title="NOTE SPOTTED!!", message= "ARE YOU SURE YOU WANT TO CREATE NEW? - CHISATO<3")
   customer_entry.delete(0, END)
   quntity1_combobox.set(0)
   quntity1_combobox.set(0)

def save():
   f= open(f'{customer_entry.get()} Bill', "w")
   f.write(f'Customer Nickname: {customer_entry.get()}\n')
   f.write(f'Total Price: {total_price}₱ \n')
   f.write(f'Bill Date Purchase: {date.today()}')
   messagebox.showinfo(title="SAVED", message= 'BILL HAS BEEN SAVED')

     

img1_label=customtkinter.CTkLabel(rich,image=img2, text="APPLES\n Price: ₱ 20", font=font2, text_color="black", fg_color="#DE3163", width=50, height=200, corner_radius=20, compound=TOP, anchor=N)
img1_label.place(relx=0.03,rely=0.17)

img2_label=customtkinter.CTkLabel(rich,image=img1, text="ORANGES\n Price: ₱ 25", font=font2, text_color="black", fg_color="#DE3163", width=130, height=200, corner_radius=20, compound=TOP, anchor=N)
img2_label.place(relx=0.23,rely=0.17)

img3_label=customtkinter.CTkLabel(rich,image=img3,text="", font=font2,fg_color="pink", width=130, height=50, compound=TOP, anchor=N)
img3_label.place(relx=0.74,rely=0.0)

img4_label=customtkinter.CTkLabel(rich,image=img4, text="MONEY", font=font2, text_color="black", fg_color="#DE3163", width=130, height=200, corner_radius=20, compound=TOP, anchor=N)
img4_label.place(relx=0.06,rely=0.63)

img5_label=customtkinter.CTkLabel(rich, image=img5, text="", font=font2, text_color="black", fg_color="pink", width=130, height=200,  compound=TOP, anchor=N)
img5_label.place(relx=0.83,rely=0.44)

img6_label=customtkinter.CTkLabel(rich, image=img6, text="", font=font2,fg_color="pink", width=130, height=25, compound=TOP, anchor=N )
img6_label.place(relx=0.45, rely=0.78)

img7_label=customtkinter.CTkLabel(rich, image=img7, text="", font=font2,fg_color="pink", width=130, height=50, compound=TOP, anchor=N )
img7_label.place(relx=0.63, rely=0.76)

img8_label=customtkinter.CTkLabel(rich, image=img8, text="", font=font2,fg_color="pink", width=130, height=50, compound=TOP, anchor=N )
img8_label.place(relx=0.82, rely=0.76)


quntity1_combobox=customtkinter.CTkComboBox(rich,font=font3,text_color="white",fg_color="gray", values=('1','2','3','4', '5'), state="readonly")
quntity1_combobox.place(relx=0.07,rely=0.57)
quntity1_combobox.set(0)

quntity2_combobox=customtkinter.CTkComboBox(rich,font=font3,text_color="white",fg_color="gray", values=('1','2','3','4', '5'), state="readonly")
quntity2_combobox.place(relx=0.28,rely=0.57)
quntity2_combobox.set(0)

quntity3_combobox=customtkinter.CTkComboBox(rich,font=font3,text_color="white",fg_color="gray", values=('10','50','100','200', '250'), state="readonly")
quntity3_combobox.place(relx=0.27,rely=0.81)
quntity3_combobox.set(0)

customer_label=customtkinter.CTkLabel(rich,text= "Customer Nickname:", font=font2,text_color="black", fg_color="#AF7AC5")
customer_label.place(relx=0.45, rely=0.58)

customer_entry=customtkinter.CTkEntry(rich, font=font2, fg_color="white", text_color="black", border_color="white", width=200)
customer_entry.place(relx=0.67,rely=0.58)

pay_button=customtkinter.CTkButton(rich,command=pay, text="TOTAL CHANGE:", font=font2, text_color="yellow", border_color="violet", fg_color="#2E86C1", corner_radius=20, cursor="hand2")
pay_button.place(relx=0.4,rely=0.70)

save_button=customtkinter.CTkButton(rich,command=pay, text="SAVE RECEIPT:", font=font2, text_color="yellow", border_color="violet",fg_color="#2E86C1", corner_radius=20, cursor="hand2")
save_button.place(relx=0.6, rely=0.70)

new_button=customtkinter.CTkButton(rich,command=new, text="CREATE NEW:",font=font2, text_color="yellow", border_color="violet", fg_color="#2E86C1",corner_radius=20, cursor="hand2")
new_button.place(relx=0.79,rely=0.70)



