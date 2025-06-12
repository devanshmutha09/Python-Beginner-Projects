import random
number = random.randint(1,100)
print("Enter a Number Between 1-100")
attempts=0
while True:
    try:
        user_number = int(input("Enter A Number : "))
        attempts+=1
        if(user_number>number):
            print("Too High")
        elif(user_number<number):
            print("Too Low")
        elif(user_number==number):
            print(f"Congrats, You Guessed it Right in {attempts} Attempts!")
            break
        else:
            print("Something Went Wrong")            
    except:
        print("Invalid Number ")