### account holder info

def fun_info():
    while True:
        name = input("Enter your name : ").lower()
        password = int(input("Enter your password : "))

        with open("user_info.txt","r") as f:
            content = f.read()


        if name in content and str(password) in content:
            print(f"Welcome {name} !!!")
            ##break
            info_choice = input("Do you want to enter your details or check them ? (yes or no) : ").lower()

            if info_choice == "yes":
                yes_choice = int(input("1.Enter details : \n2.Check details : "))

                if yes_choice == 1:
                    age = int(input("Enter your age : "))
                    city = input("Enter your city : ")

                    with open ("user_info.txt","a") as f:
                        f.write()
                        break

                else:
                    with open("user_info.txt","r") as f:
                        content = f.read()
                        print(content)
                        break

            else:
                break

        else:
            print("Account not found,")
            choice = int(input("1.Try again : \n2.Create a new account : "))

            if choice == 1:
                break

            elif choice == 2:
                    age = int(input("Enter your age : "))
                    city = input("Enter your city : ")

                    with open("user_info.txt","a") as f:
                        f.write(f"Name({name}) : Password({password}) : Age({age}) : City({city})\n")

                    break

            else:
                print("Invalid choice !!!")