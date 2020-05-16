from tkinter import *
root=Tk()
def getvals():
    print("Submitting The Form.")
    print(f"{firstname_value.get(), lastname_value.get(), address_value.get(), phone_no_value.get(), gender_value.get(), payment_mode_value.get(), food_service_value.get()}")
    with open ("Travel.txt", "a") as f:
        f.write(f"\n\nFirst Name of person:{firstname_value.get()}\nLast Name of Person:{lastname_value.get()}\nAddress:{address_value.get()}\nPhone Number:{phone_no_value.get()}\nGender:{gender_value.get()}\nPayment:{payment_mode_value.get()}\nFood Services:{food_service_value.get()}\n\n")
root.geometry("600x500")
#Heading
Label(root, text="Welcome To Travels", font="comicsansms 12 bold", pady=10).grid(row=0, column=3)
#Text for form
firstname=Label(root, text="First Name").grid(row=1, column=2)
lastname=Label(root, text="Last Name").grid(row=2, column=2)
address=Label(root, text="Address").grid(row=3, column=2)
phone_no=Label(root, text="Phone No.").grid(row=4, column=2)
gender=Label(root, text="Gender").grid(row=5, column=2)
payment_mode=Label(root, text="Payment Mode").grid(row=6, column=2)
#Tkinter variables
firstname_value=StringVar()
lastname_value=StringVar()
address_value=StringVar()
phone_no_value=StringVar()
gender_value=StringVar()
payment_mode_value=StringVar()
food_service_value=IntVar()
#Entry for our form
firstnameentry=Entry(root, textvariable=firstname_value).grid(row=1, column=3)
lastnameentry=Entry(root, textvariable=lastname_value).grid(row=2, column=3)
addressentry=Entry(root, textvariable=address_value).grid(row=3, column=3)
phone_noentry=Entry(root, textvariable=phone_no_value).grid(row=4, column=3)
genderentry=Entry(root, textvariable=gender_value).grid(row=5, column=3)
payment_modeentry=Entry(root, textvariable=payment_mode_value).grid(row=6, column=3)
#Checkbox and packing
foodservice=Checkbutton(text="Want to preorder meal?", variable=food_service_value).grid(row=7, column=3)
#Making buttons
Button(root, text="Submit The Form", command=getvals).grid(row=8, column=3)
root.mainloop()