# this is for a computer Vs computer using random number generator
class supernim:
 player='max' # initialized  a player
 player1points=0
 player2points=0
 counter=1
 import random
 import check;
 # we are taking a list
 list1 =[6,8];
 print("the current list1 is",list1) # the current list
 print("the current player is ",player)
 #here we check if our list is empty or not
 while (list1!=[]):  
   length=len(list1)       
# here we are taking which number we want from our list
   while True:
     if player=='min':
      t=random.randint(0,length-1)  # player 2 turn
     else:
      t =random.randint(0,length-1)  # player 1 turn
     if list1[t]!=2:
      break                               # making sure a wrong moveis not made
    
# here we are stating wether the number is odd in our list  ( here a player chooses a state or heap for an odd computation)

   if  list1[t] % 2 !=0:
     counter=0                  # this is used to indicate that only a odd computation is happening and musnt go to the part of even computation of a heap
     list1[t]=list1[t]*3+1
     if list1[t]>10:
         list1[t]=10
     print("the current list is now",list1)
     
# If our number is even we split our even heap into sub heap portions of even values or odd values

   if counter !=0:                    # we use a counter here so that the execution does not flow into the even portion computation of a heap
    while True:
     if player=='min':
       y=random.randint(2,5)
     else:
      y =random.randint(2,5)                 #( here a player chooses a state or heap for even number computation)
     if y == 2:                              # if the heap is to be divided into 2 parts
      if 4 or 6 or 10 in list1[t]:
        n=int(list1[t]-(list1[t]/2))
        for x in range (0,y):
         list1.append(n)
        del list1[t]
        print(list1)
        break
      elif 8 in list1[t]:
         n=int(list1[t]/4)
         for x in range (0,y):
           list1.append(n)
         del list1[t]
         print(list1)
         break
     elif y == 3 :# if the heap is to be divided into 3 parts
      if list1[t] == 6:
        n=int(list1[t]/3)
        for x in range (0,y):
         list1.append(n)
        del list1[t]
        print(list1)
        break
      elif list1[t] == 8:
         n=int(list1[t]/4)
         for x in range (0,2):
           list1.append(n)
         list1.append(2*n)
         del list1[t]
         print(list1)
         break
     elif y == 4 :# if the heap is to be divided into four parts
      if list1[t] == 8:
         n=int(list1[t]/4)
         for x in range (0,y):
           list1.append(n)
         del list1[t]
         print(list1)
         break
     elif y == 5 : # if the heap is to be divided into five parts
       if list1[t] == 10:
         n=int(list1[t]/5)
         for x in range (0,y):
           list1.append(n)
         del list1[t]
         print(list1)
         break
     else:
       exit(0)
     
   counter=counter+1      # the counter is updated
   if(player=='max'):      # here it becomes a turn for another player after the previous player has made a move
     player='min'
   else:
     player='max'
   print("the current player is ",player)
 
 # here we look at removing the two to gain our points

   while 2 in list1:
     if player=='min':
       s=random.randint(0,1)
     else:
          s=random.randint(0,1)                  # here we choose wether to remove a 2 from our list 
     if s == 1:                   
      list1.remove(2)
      if(player=='max'):
         player1points=player1points+2
      else:
          player2points=player2points+2
      print("list1 when 2 is removed",list1)
      
 # here if either of the player has made a move in removing a 2 from the list. then it becomes the next players turn
 
      if(player=='max'):       
         player='min'
      else:
         player='max'
      print("the current player is ",player)
     else:
      if(len(set(list1))==1):
          player1points,player2points=check.checker.func(list1,player1points,player2points,player)
      break;  
 print("final points for player 1",player1points)
 print("finalpoints for player 2",player2points)
 if (list1==[]):
  def terminal(list1,player1points,player2points):   #terminal function to return a 100 or -100 depending on who won
   if (player1points>player2points):
     print("max wins!!")
     return 100;
   else:
     print("min wins!!")
     return -100;
  res = terminal(list1,player1points,player2points);
  print(res)
  




