print("THIS IS A ATM MANAGEMENT SYSTEM ")
lang=["hindi","english","marathi","urdu"]
l=int(input("choose ur language \n select 0 for hindi\n select 1 for english \n select 2 for marathi \n select 3 for urdu \n"))
print("you have selected",lang[l])
while True:
  options={1:"CASH WITHDRAWAL",2:"CHECK BALANCE",3:"CHANGE PASSWORD",4:"HELP",5:"EXIT"}
  balance = 50000
  old_password="1234"
  contact =9999999999
  o=int(input("Enter 1 for CASH WITHDRAWAL \n 2 to CHECK BALANCE \n 3 to CHANGE PASSWORD  \n 4 for HELP \n 5 for EXIT"))
  print("you want to ",options[o])
  if o==1:
      p=input("enter your password")
      if p == old_password:
        w=int(input("enter money you want to withdraw"))
        if balance>=w:
           balance=balance-w
           print("you have withdrawed",w,"and your remaining balance is",balance)
        else: print("insufficient amount")
      else: print("pls enter correct password to withdraw cash")
  elif o==2:
      p=input("enter your password")
      if p == old_password:
        print("current balance",balance)
      else: print("pls enter correct password to check balance")
  elif o==3:
      x=input("enter your registered contact no")
      if x==contact:
         password=input("enter new password")
         if password==old_password:
           print("new pass can't be same")
         else:
           print(" new password is",password)
      else: print("enter contact no to change password")
  elif o==4:
      print("contact local branch")
  elif o==5:
      print("thankyou for using")  
      break
  else:
      print("invalid choice")