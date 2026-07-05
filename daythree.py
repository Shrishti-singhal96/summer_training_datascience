#LIST TUPLES DICTIONARY
# LIST=[] MUTUABLE DUPLICATE ALLOWED, USE INDEXING
# TUPLE=() IMMUTUABLE DUPLICATE ALLOWED, USE INDEXING
# DICTIONARY={KEY:VALUE} MUTUABLE DUPLICATE KEYS NOT ALLOWED, USE KEYS FOR INDEXING




#world cup problem 2021 and 2027
year=int(input("enter year about which you want to know\nenter 0 for 2021 and enter 1 for 2027"))
worldcupyear=[2021,2027]
print(worldcupyear[year])

teamyear=int(input("enter 2021 to get teams of 2021 and enter 2027 to get teams of 2027"))
teams={2021:("india", "aus","usa","uk","pak","bangladesh"),2027:["india", "aus","usa","uk","pak","bangladesh","africa"]}
print(teams[teamyear])
print("enter 0 for india ,1 for aus and 2 for africa")
country=int(input("enter choice:"))
countries=["india","aus","africa"]
print(countries[country])


india={2021:{"players":{"rohit":["batsman", "opener","captain"],"jasprit":["bowler","vc"],"hardik":["bowler","batsman","xyx"]}},2027:{"players":{"rohit":["batsman", "opener","captain"],"jasprit":["bowler","vc"],"sky":["bowler","batsman","xyx"]}}}
aus={2021:{"players":{"A":["batsman", "opener","captain"],"B":["bowler","vc"],"C":["bowler","batsman","xyx"]}},2027:{"players":{"A":["batsman", "opener","captain"],"B":["bowler","vc"],"D":["bowler","batsman","xyx"]}}}
africa={2021:"didn't participated",2027:{"players":{"X":["batsman", "opener","captain"],"Y":["bowler","vc"],"Z":["bowler","batsman","xyx"]}}}
y=int(input("enter the year you want to see team ofchosen country"))

if country==0:
   print(india[y])
if country==1:
   print(aus[y])
if country==2:
   print(africa[y])

p=input("enter the name of player you want to know about")
if p=="rohit":
   print(india[y]["players"][p])
if p=="jasprit":
   print(india[y]["players"][p])
if p=="hardik":
   print(india[y]["players"][p])
if p=="sky":
   print(india[y]["players"][p])
if p=="A":
   print(aus[y]["players"][p])
if p=="B":
   print(aus[y]["players"][p])
if p=="C":
   print(aus[y]["players"][p])
if p=="D":
   print(aus[y]["players"][p])
if p=="X":
   print(africa[y]["players"][p])
if p=="Y":
   print(africa[y]["players"][p])
if p=="Z":
   print(africa[y]["players"][p])

#OR
worldcup={
    2021:{"Teams":["India","Australia","Pakistan","England"],
          "captains":{"India":"Virat Kohli","Australia":"Aaron Finch","England":"Eoin Morgan","Pakistan":"Babar Azam"},
          "Total players":{"India":15,"Australia":15,"England":15,"Pakistan":15},
          "winner":"India"
          },
    2027:{"Teams":["India","Australia","England","South Africa"],
          "captains":{"India":"Rohit Sharma","Australia":"Pat Cummins","England":"Jos Buttler","South Africa":"Temba Bavuma"},
          "Total players":{"India":15,"Australia":15,"England":15,"South Africa":15},
          "winner":"To be decided"
          }
    }

#year=int(input("Enter world cup year:"))

while True:
    print("\t\t\t\t\n\nWORLD CUP\t\t\t")
    print("\n1 Show Years")
    print("\n2 Show Teams")
    print("\n3 Show Captain")
    print("\n4 Show Winner")
    print("\n5 Show Total Players")
    print("\n6 Exit")

    ch=int(input("Enter choice; "))

    if ch==1:
        print("Availabe years:",list(worldcup.keys()))

    elif ch==2:
        year=int(input("Enter worldcup year"))
        print("Teams",worldcup[year]["Teams"])

    elif ch==3:
        year=int(input("Enter worldcup year"))
        team=input("Enter Team name: ")
        print("Captains",worldcup[year]["captains"][team])

    elif ch==4:
        year=int(input("Enter worldcup year"))
        print("winner:",worldcup[year]["winner"])

    elif ch==5:
        year=int(input("Enter worldcup year"))
        team=input("Enter Team name: ")
        print("Total Players",worldcup[year]["Total players"][team])

    elif ch==6:
        print("Thank you")
        break
    else:
        print("Invalid choice")










#atm management system
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