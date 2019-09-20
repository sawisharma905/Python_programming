print(".....welcome to Children's bank.....")
d1={11111111111:'######', 22222222222:'$$$$$$' , 33333333333:'%%%%%%' ,
    44444444444:'******', 55555555555:'@@@@@@'}
Acc_no=int(input("Account no :"))
Password=input("Password : ")

if (Acc_no,Password) in d1.items():
    print("correct data !!")
    
else:
    print("incorrect entry !!")

d2={11111111111:2356456, 22222222222:56346743 , 33333333333:55462 ,
    44444444444:457543, 55555555555:6743452}

if Acc_no in d2.keys():
    print("Balance=" ,d2[Acc_no])


#ans='y'
#while ans=='y'||ans=='Y':
flag=1
for k in d1.keys():
      if k==Acc_no and d1[k]==Password:
          while True:
              flag=0
              print("MENU")
              print("1.Check Balance")
              print("2.Withdraw")
              print("3.Deposit")
              print("4.exit")
              choice=int(input("choice :"))

              if choice==1:
                  print("...Check balance...")
                  print("Balance is :" ,d2[Acc_no])

              elif choice==2:
                  print("...Withdraw...")
                  withdraw=int(input("enter the amount :"))
                  d2[Acc_no]-=withdraw
                  print("New Balance :" ,d2[Acc_no] )
              elif choice==3:
                  print("...Deposits...")
                  deposit=int(input("enter the amount :"))
                  d2[Acc_no]+=deposit
                  print("New Balance :" ,d2[Acc_no] )

              elif choice==4:
                  print("Exit !!!")
                  break

              else:
                  print("wrong choice !!!")
                
                  
     
     
