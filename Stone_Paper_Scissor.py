import random
'''
Stone : 1
Paper : "0"
xcissor : -1

The Game will be played between user and Computer
'''
computer = random.choice(["s","p","x"])
your_input = input("Enter Your Choice : ")
reverse_dict={
    "s":"Stone",
    "p":"Paper",
    "x":"Scissor"
}
print(f"You Choose {reverse_dict[your_input]} and Computer Choose {reverse_dict[computer]} ")

if(computer == your_input):
    print("Its a Draw, Play Again")
else :
    if your_input == "s" and computer == "p":
        print("You Lose! Paper beats Stone")

    elif your_input == "s" and computer == "x":
        print("You Win! Stone beats Scissor")

    elif your_input == "p" and computer == "s":
        print("You Win! Paper beats Stone")

    elif your_input == "p" and computer == "x":
        print("You Lose! Scissor beats Paper")

    elif your_input == "x" and computer == "s":
        print("You Lose! Stone beats Scissor")

    elif your_input == "x" and computer == "p":
        print("You Win! Scissor beats Paper")

    else:
        print("Invalid input! Please enter only 's', 'p', or 'x'.")