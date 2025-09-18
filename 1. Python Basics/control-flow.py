# check if the shop is open
shopeIsOpen = True
if shopeIsOpen:
    print("Welcome to the shop!")
else:
    print("Sorry, we are closed.")  

customerWaiting = input("How many customers are waiting?: ")
while not customerWaiting.isdigit() or int(customerWaiting) < 0:
    print("Please enter a valid number.")
    customerWaiting = input("How many customers are waiting?: ")

customerWaiting = int(customerWaiting)
print(f"There are {customerWaiting} customers waiting.")

    