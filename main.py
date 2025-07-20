### Bank Managment system

from user_control import fun_user_control
from info import fun_info

main_choice = int(input("Enter \n1.User account : \n2.User transactions : "))

if main_choice == 1:
    fun_info()

elif main_choice == 2:
    fun_user_control()

else:
    print("Invalid choice !!!")