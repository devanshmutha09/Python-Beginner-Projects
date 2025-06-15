import qrcode as qr
import PIL
    # IMPORT THE INITIAL MODULE/LIBRARY

qr_dict = {
    
    "GooglePay" : "upi://pay?pa=yourupiid&cu=INR&am=0&pn=Name",
    "PhonePe" : "upi://pay?pa=yourupiid&cu=INR&am=0&pn=Name",
    "Paytm" : "upi://pay?pa=yourupiid&cu=INR&am=0&pn=Name",

}

    #DEFINE THE DICTIONARY FOR UPI QR CODE GENERATION WITH THEIR UPI FORMAT

print('\nThese are the following QR Code you can Generate :')
for idx, name in enumerate(qr_dict,start=1):
    print(f"{idx} : {name}")

    #DISPLAY THE DICTIONARY USING FOR LOOP AND 
    #ENUMERATE FUNCTION --> ENUMERATE FUNCTION IS USED TO DISPLAY THE INDEX (CUSTOMIZABLE)


try: #TRY BLOCK
    choice_qr = input("Enter the QR You Want to Generate from above (Case Sensitive): ").strip().replace(" ","")
    #ENTER THE CHOICE
    FixAmount_Check = input("Want to Enter any Fix Amount (Yes/No) : ").lower()
    # ENTER YES IF YOU WANT FIX AMOUNT ELSE NO
    # old_part = 'am=0'
    if choice_qr in qr_dict:                      #IF ENTERED CHOICE IN DICTIONARY


        if(FixAmount_Check=="yes"):               #IF FIXAMOUNT_CHECK IS YES
            amount = input("Enter the Amount you want to Initialize : \n")
            new_part = f'am={amount}'
            qr_dict[choice_qr] = qr_dict[choice_qr].replace('am=0',new_part)
            data = qr.make(qr_dict[choice_qr])
            filename = input("Enter Your Filename (without extension) : ").strip()
            image = data.save(f"{filename}.png")
            
            print(f"Your File has been Successfully Saved as {filename}.png")

            
        elif (FixAmount_Check=="no"):           #IF FIXAMOUNT_CHECK IS NO
            data = qr.make(qr_dict[choice_qr])
            filename = input("Enter Your Filename (without extension) : ").strip()
            image = data.save(f"{filename}.png") 
            print(f"Your File has been Successfully Saved as {filename}.png")


    else:                                        #ELSE INVALID CHOICE
        print("Invalid Choice or Case Sensitive")

    
except Exception as e:                          #EXCEPT BLOCK RUNS WHEN ERROR OCCURED IN TRY BLOCK
    print("Error")