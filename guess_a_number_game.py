
main_ans={10:1,20:2,30:3,40:4,50:5,60:6,70:7,80:8,90:9,100:10}
li=[]

print("\t\tGuess any number in your mind upto 1 - 10 \n\n")

print("***************************************************************************\n\n")

option_1=input("Enter Y or N to analys that your guessed number in this line  (8,1,5,6,10) :")

if option_1.upper()=="Y":
    li.append(10)
    option_2=input("Enter Y or N to analys that your guessed number in this line  (10,6,2,9) :")
    if option_2.upper()=="Y":
        li.append(20)
        option_3=input("Enter Y or N to analys that your guessed number in this line  (10,9,8,3,6,7) :")
        if option_3.upper()=="Y":
            li.append(30)
            option_4=input("Enter Y or N to analys that your guessed number in this line  (10,9,4,5,7,8) :")
            if option_4.upper()=="Y":
                li.append(40)
                print(f"your guessed number is {main_ans[sum(li)]}")
            else:
                print("check your input, enter  valid option")
        elif option_3.upper()=="N":
            option_4=input("Enter Y or N to analys that your guessed number in this line  (10,9,4,5,7,8) :")
            if option_4.upper()=="Y":
                li.append(40)
                print(f"your guessed number is {main_ans[sum(li)]}")
            else:
                print("check your input, enter  valid option")
        else:
            print("check your input, enter  valid option")
    elif option_2.upper()=="N":
        option_3=input("Enter Y or N to analys that your guessed number in this line  (10,9,8,3,6,7) :")
        if option_3.upper()=="Y":
            li.append(30)
            option_4=input("Enter Y or N to analys that your guessed number in this line  (10,9,4,5,7,8) :")
            if option_4.upper()=="Y":
                li.append(40)
                print(f"your guessed number is {main_ans[sum(li)]}")
            else:
                print("check your input, enter  valid option")
        elif option_3.upper()=="N":
            option_4=input("Enter Y or N to analys that your guessed number in this line  (10,9,4,5,7,8) :")
            if option_4.upper()=="Y":
                li.append(40)
                print(f"your guessed number is {main_ans[sum(li)]}")
            else:
                print("check your input,enter  valid option")
        else:
            print("check your input,enter  valid option")
elif option_1.upper()=="N":
    option_2=input("Enter Y or N to analys that your guessed number in this line  (10,6,2,9) :")
    if option_2.upper()=="Y":
        li.append(20)
        option_3=input("Enter Y or N to analys that your guessed number in this line  (10,9,8,3,6,7) :")
        if option_3.upper()=="Y":
            li.append(30)
            option_4=input("Enter Y or N to analys that your guessed number in this line  (10,9,4,5,7,8) :")
            if option_4.upper()=="Y":
                li.append(40)
                print(f"your guessed number is {main_ans[sum(li)]}")
            else:
                print("check your input,enter  valid option")
        elif option_3.upper()=="N":
            option_4=input("Enter Y or N to analys that your guessed number in this line  (10,9,4,5,7,8) :")
            if option_4.upper()=="Y":
                li.append(40)
                print(f"your guessed number is {main_ans[sum(li)]}")
            else:
                print(f"check your input,enter  valid option")
        else:
            print("check you answer,enter  valid option")
    elif option_2.upper()=="N":
        option_3=input("Enter Y or N to analys that your guessed number in this line  (10,9,8,3,6,7) :")
        if option_3.upper()=="Y":
            li.append(30)
            option_4=input("Enter Y or N to analys that your guessed number in this line  (10,9,4,5,7,8) :")
            if option_4.upper()=="Y":
                li.append(40)
                print(f"your guessed number is {main_ans[sum(li)]}")
            else:
                print("check your inpput,enter  valid option")
        elif option_3.upper()=="N":
            option_4=input("Enter Y or N to analys that your guessed number in this line  (10,9,4,5,7,8) :")
            if option_4.upper()=="Y":
                li.append(40)
                print(f"your guessed number is {main_ans[sum(li)]}")
            else:
                print("check your input,enter  valid option")
        else:
            print("check your input,enter  valid option")
    else:
        print("check your input,enter  valid option")
        
else:
    print("check your input,enter  valid option")
    

print("\n\n\t\t\t\tThank You ")

