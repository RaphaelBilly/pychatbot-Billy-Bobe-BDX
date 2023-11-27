from common import get_list_of_files_in_directory
from basic_functions import get_cleaned_speeches


files_names = get_list_of_files_in_directory("./speeches")
get_cleaned_speeches(files_names)

# print("Menu :")
# print("1. ")
# print("2. ")
#
#
# choice = input("Enter your choice [1-2]: ")
# choice = int(choice)
#
# match choice:
#     case 1:
#         print("You chose 1")
#     case 2:
#         print("You chose 2")
#     case _:
#         print("Invalid choice")
