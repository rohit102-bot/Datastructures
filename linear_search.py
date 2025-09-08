ac_list = [1001, 1002, 1003, 1004, 1005]

def linear_search():
    ac_no = int(input("Enter the account number you want to search: "))
    found = False
    for i in ac_list:
        if i == ac_no:
            found = True
            break
    if found:
        print("Account exists in the list.")
    else:
        print("Account does not exist.")

linear_search()
