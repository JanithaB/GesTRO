from tkinter import *
import random
import customtkinter
from PIL import Image, ImageTk
import btwithcport #python code for processing
import webbrowser



sun = btwithcport.connection()
#print(sun)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Gestro")
root.geometry("900x600")
root.iconbitmap("title.ico")
root.resizable(False, False)


#canvas setup
canvas=Canvas(root,height=900, width=600, bg="#181818", highlightthickness=0)
canvas.pack(fill="both", expand=True)


#logo
logo = Image.open("logo.png")
new_size=(330,110)
resized_logo = logo.resize(new_size)
tk_logo=ImageTk.PhotoImage(resized_logo)
logo_label=Label(root, image=tk_logo, bg="#181818")
logo_label.place(x=380, y=10)

#create two frames
page1_frame = Frame(root, bg="#181818")
page2_frame = Frame(root, bg="#181818")

#global variable to store the slider value
f_slider_value = 6

#
#comport = cportforgui.detect_esp32_com_port()

#home_window

def homePage():
    page2_frame.place_forget()
    page1_frame.place(x=0, y=200, height=520, width=1130)

    con_label = Label(page1_frame, text="Connection Status", font=("Montserrat Bold",16), bg="#181818", fg="white")
    con_label.place(x=50 ,y=150)

if (sun == 1):
    con_status = Label(page1_frame, text="GesTRO Wave Connected", font=("Montserrat Bold",16), bg="#181818", fg="green")
    con_status.place(x=500 ,y=150)

    DPI_label = Label(page1_frame, text="DPI Level", font=("Montserrat Bold",16), bg="#181818", fg="white")
    DPI_label.place(x=50 ,y=300)

#====================================================================================================================================================


    def change(val):
        global slider_value
        slider_value = str(val)
        #print (str(val))


    def save():
        global f_slider_value
        f_slider_value = int(slider_value)
        btwithcport.save(f_slider_value)
        
#====================================================================================================================================================

#DPI slider 
    DPI_slider = Scale(page1_frame, from_=1, to=11, orient=HORIZONTAL, length=500, width=30, sliderlength=20,command=change)
    DPI_slider.configure(troughcolor="#274156", activebackground="#605856", background="#d0ccd0", highlightcolor="blue", showvalue=False)
    DPI_slider.set(f_slider_value)
    DPI_slider.place(x=500, y=300)


    save_button = customtkinter.CTkButton(master=page1_frame, text="Save", fg_color=("#38b6ff","#3f4045") ,font=("Montserrat Bold",14), width=80, height=20, border_width=0, corner_radius=8)#, command=save)
    save_button.place(x=720, y=350)

    
else:
    con_status = Label(page1_frame, text="Not Connected", font=("Montserrat Bold",16), bg="#181818", fg="red")
    con_status.place(x=500 ,y=150)

    error_msg = Label(page1_frame, text="Check the bluetooth connectivity and restart the program", font=("Montserrat Bold",12), bg="#181818", fg="white")
    error_msg.place(x=350 ,y=300)
    


    


def aboutPage():
    page1_frame.place_forget()
    page2_frame.place(x=0, y=200, height=520, width=1130)

    about_para = Label(page2_frame, text="Gestro: Unlock the Full Potential of Your Mouse with our Powerful Software. Customize settings, macros, and \nDPI with ease, and experience a new level of productivity. Tailor your mouse to match your unique needs with \nGestro.", font=("Montserrat",11) , bg="#181818", fg="white", justify="left")
    about_para.place(x=30, y=50)

    link_label1 = Label(page2_frame,text="Check our official website for more information: ", font=("Montserrat",11), bg="#181818", fg="white")
    link_label1.place(x=30, y=200)

    def open_website():
        webbrowser.open("https://bit.ly/Gestro")

    link_label2 = Label(page2_frame, text="Click here", font=("Montserrat",11), fg="#38b6ff", bg="#181818", cursor="hand2")
    link_label2.place(x=500, y=200)
    link_label2.bind("<Button-1>", lambda event: open_website())

    #QR
    global tk_qr_image
    qr_image = Image.open("qr.png")
    qr_image = qr_image.resize((200, 200))
    tk_qr_image = ImageTk.PhotoImage(qr_image)
    qr_label = Label(page2_frame, image=tk_qr_image, bg="#181818")
    qr_label.place(x=450, y=270)



#buttons
#home
home_button = customtkinter.CTkButton(master=root, text="Home", fg_color=("#38b6ff","#3f9aaf") ,font=("Montserrat Bold",14), width=80, height=20, border_width=0, corner_radius=8, command=homePage)
home_button.place(x=20, y=120)


'''
#settings
settings_button = customtkinter.CTkButton(master=root, text="Settings", fg_color=("#38b6ff","#3f9aaf") ,font=("Montserrat Bold",14), width=80, height=20, border_width=0, corner_radius=8)
settings_button.place(x=115, y=120)
'''
#about
about_button = customtkinter.CTkButton(master=root, text="About", fg_color=("#38b6ff","#3f9aaf") ,font=("Montserrat Bold",14), width=80, height=20, border_width=0, corner_radius=8, command=aboutPage)
about_button.place(x=800, y=120)
#210

homePage()

root.mainloop()
