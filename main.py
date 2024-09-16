import time
Money = 1000000
n = 1
m = 2
y = 0
h = 0
p = "yes"
RawMoney = 0
b = "yes"
SoldRawMoney = RawMoney * 10
correct = False
while correct is False:
  y = y + 1
  passcode = input()
  print("Accessing secure banking system...")
  time.sleep(2)
  if  passcode == "9651":
    print("Access granted. Welcome to your bank account.")
    print("Your current balance is",Money)
    time.sleep(2)
    while Money > 0 and b == "yes":
      print("What would you like to buy?")
      print("Melted chicken 3.70$")
      print("Solid water 2.50$")
      buy = input()
      if buy == "Melted chicken":
        Money = Money - 3.70
        print("Your balance is now")
        print(Money)
        print("Would you like to buy anything else?")
        print("Or would you like to mine for money?")
        b = input()
    correct = True
    while p =="yes":
      if b == "Mine for money":
        print("Answer this question to earn money",m, "*", m) 
        h = int(input())
        x = m * m
        print(x)
        if h == x: 
          m += n
          print("Correct")
          RawMoney = RawMoney + n * m
          print("You have",RawMoney,"Raw money")
          print("Would you like to continue mining or sell raw money?")
          p = input()
          if p == "Sell raw money":
            print("Raw money is worth 10$. You will get",SoldRawMoney)
            print("Selling raw money")
            time.sleep(2)
            Money = Money + SoldRawMoney
            print("Raw money sold you have Gained",SoldRawMoney,"Money")  
            RawMoney = RawMoney - RawMoney
        b = input()
      if buy == "Solid water":
        Money = Money - 2.50
        print("Your balance is now")
        print(Money)
        print("Would you like to buy anything else?")
        print("Or would you like to mine for money?")
        b = input()
    correct = True
    while p =="yes":
      if b == "Mine for money":
        print("Answer this question to earn money",m, "*", m) 
        h = int(input())
        x = m * m
        print(x)
        if h == x: 
          m += n
          print("Correct")
          RawMoney = RawMoney + n * m
          print("You have",RawMoney,"Raw money")
          print("Would you like to continue mining or sell raw money?")
          p = input()
          if p == "Sell raw money":
            print("Raw money is worth 10$. You will get",SoldRawMoney)
            print("Selling raw money")
            time.sleep(2)
            Money = Money + SoldRawMoney
            print("Raw money sold you have Gained",SoldRawMoney,"Money")  
            RawMoney = RawMoney - RawMoney

        else:
          print("Incorrect")
          print("You have",RawMoney,"Raw money")
          print("Would you like to continue mining?")
          p = input()
  else:

    print("Access DENIED, incorrect passcode!")
    correct = False

  if y == 15:
    print("Sytem failed reboot Sytem.")
    x = input()

    if x == "reboot":
      print("Rebooting...")
      time.sleep(2)
      y = 0
      
      print("System rebooted.")
  if y == 5:
    print("Lock enabled input answer to unlock.")
    print("What is the answer to this equation: 1.50 x 4")
    x = int(input())
    if x == 6:
      print("Access granted.")
      