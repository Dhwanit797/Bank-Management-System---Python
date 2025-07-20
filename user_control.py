### user controls like check , withdraw , deposit

def fun_user_control():
    name = input("Enter your name : ").lower()

    with open("user_info.txt","r") as f:
                content = f.read()

    while True:

        if name in content:
                print(f"Welcome {name}, ")
                curr_balance = int(input("Enter your Current balance : "))

                act_choice = int(input("Enter 1.Withdraw : \n2.Deposit : \n3.Exit : "))

                if act_choice == 1:
                    withdraw_amount = int(input("Enter withdraw amount : "))
                    if withdraw_amount > curr_balance:
                        print("Insufficient balance !!!")
                        
                    else:
                        new_balance = curr_balance - withdraw_amount
                        print(new_balance)
                        

                elif act_choice == 2:
                    deposit_amount = int(input("Enter deposit amount : "))
                    new_balance = deposit_amount + curr_balance
                    print(new_balance)
                    

                elif act_choice == 3:
                    new_balance = curr_balance
                    print("Exited !!!")
                    break


    with open("user_bank_balance.txt","a") as f:
        f.write(f"Name({name}) : Balance({new_balance})\n")