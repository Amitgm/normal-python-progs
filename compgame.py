# a game between human player vs computer

player='max'
player1points=0
player2points=0
counter=1
import random
import check;
# we are taking a list
list1 =[6,8];
while (list1!=[]):
   length=len(list1)
   print("the current length of list",length) # the length of list
   print("the current list1 is",list1)        # the current list
# here we are taking which number we want from our list
   while True:
     if player=='min':
      t=random.randint(0,length-1) # player 2 turn (computer)
      print("the value chosen by min",t)
     else:
      t =int(input('the number for list1')) # player 1 turn
     if list1[t]!=2:
      break                  # making sure a wrong moveis not made
     print("invalid move")   
   print('you selected this part of the list',list1[t])
   
   if  list1[t] % 2 !=0:
     counter=0
     list1[t]=list1[t]*3+1
     if list1[t]>10:
         list1[t]=10
     print("the list1[t] is now",list1[t])
     print("the current list is now",list1)
   if counter !=0:
    while True:
     if player=='min':
       y=random.randint(2,5)
       print("how many ways to split 2 for 2 3 for 3 and 4 for 4 and 5 for 5",y)
     else:
      y = int(input('enter how many ways to split 2 for 2 3 for 3 and 4 for 4 and 5 for 5'))
     if y == 2:
      if 4 or 6 or 10 in list1[t]:
        n=int(list1[t]-(list1[t]/2))
        print("value of n",n)
        for x in range (0,y):
         list1.append(n)
        del list1[t]
        print(list1)
        break
      elif 8 in list1[t]:
         n=int(list1[t]/4)
         print("value of n",n)
         for x in range (0,y):
           list1.append(n)
         del list1[t]
         print(list1)
         break
     elif y == 3 :
      if list1[t] == 6:
        n=int(list1[t]/3)
        print("value of n",n)
        for x in range (0,y):
         list1.append(n)
        del list1[t]
        print(list1)
        break
      elif list1[t] == 8:
         n=int(list1[t]/4)
         print("value of n",n)
         for x in range (0,2):
           list1.append(n)
         list1.append(2*n)
         del list1[t]
         print(list1)
         break
     elif y == 4 :
      if list1[t] == 8:
         n=int(list1[t]/4)
         print("value of n",n)
         for x in range (0,y):
           list1.append(n)
         del list1[t]
         print(list1)
         break
     elif y == 5 :
       if list1[t] == 10:
         n=int(list1[t]/5)
         print("value of n",n)
         for x in range (0,y):
           list1.append(n)
         del list1[t]
         print(list1)
         break
     else:
       exit(0)
    
   print(list1)
   counter=counter+1
   print("the counter value",counter)
   if(player=='max'):
     player='min'
   else:
     player='max'
   print("the current player is ",player)
 
# here we look at removing the two to gain our points
   while 2 in list1:
     if player=='min':
       s=random.randint(0,1)
       print("the value chosen by player 2",s)
     else:
          s=int(input("you have gotten a 2 in the list,do you wish to remove one,if so type 1 "))
     if s == 1:
      list1.remove(2)
      if(player=='max'):
         player1points=player1points+2
      else:
          player2points=player2points+2
      print("list1 when 2 is removed",list1)
      
      if(player=='max'):
         player='min'
      else:
         player='max'
      print("the current player is ",player)
     else:
      print("nop")
      if(len(set(list1))==1):
          player1points,player2points=check.checker.func(list1,player1points,player2points,player)
          print("player1points",player1points)
          print("player2points",player2points)
      break;
   print("player1points",player1points)
   print("player2points",player2points)
print("final points for player 1",player1points)
print("finalpoints for player 2",player2points)
if (player1points>player2points):
    print("player1wins!!")
else:
    print("player2wins!!")
