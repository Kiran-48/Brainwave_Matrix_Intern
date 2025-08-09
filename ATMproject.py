   # ATM Machine Project In Python

print ("Welcome To BOP Bank \n\n Please Insert Your Card ...")

password = 3696
balance = 15000
choice = 0

pin = int (input("Enter Your Four Digit Pin Number: "))

if (pin == password): 
    while(choice != 4):
      print ("\n\n______Menu______")
      print ("1 == Balance")
      print ("2 == Deposit")
      print ("3 == Withdraw")
      print ("4 == Cancel\n")

      choice = int (input("\nEnter Your Option: "))
      
      if (choice == 1):
        print ("Balance = Rs", balance)
      elif (choice == 2):
        deposit = int (input("Enter Your Deposit: Rs"))
        balance += deposit
        print ("\nDeposited Amount: Rs", deposit)
        print ("Total Balance = Rs", balance)
      elif (choice == 3):
        withdraw = int (input("Enter Your Withdraw Amount: Rs"))
        balance -= withdraw
        print ("\nWithdraw Amount: Rs",withdraw)
        print ("Total Balance = Rs", balance)
      elif(choice == 4):
        print ("\nSession Ended!! GoodBye")
      else:
        print ("\nInvalid Entry!!")
else:
 print ("Incorrect Pin Number!! Please Try Again...!")
