# normal-python-progs
Super-nim and other code challenges

Super-nim Description:

Python programs(Super-nim game) 
The rule is to to select a number (even or odd) and split the number if it is even or the number is multiplied by 3 and added to one if its is odd

For example [4,3,6]
To choose you have to type the list index number, either 0 or 1 or 2.
if a 4 is chosen,you will be asked if you want to split it 2 or 3 or 4 way.Since only two way is possible (ie from 4 it becomes 2,2.)We will take this case.

The new list becomes[2,2,3,6]
The next player now has to choose,if he chooses 2,he gains a point or he can split the 6 or make the 3 a 10
so possible cases can be:
[2,3,6]   player =2 points.
[2,10,6] where 3*3+1 becomes 10
[2,3,2,2,2] -a three way split.
[2,3,3,3] -a two way split

This is a game of strategy hence there are many ways to increase the points in your table.
Note:- you cannot make an invalid split you will be asked to make the split again nor can you increase a even number.
       If you do not wish to take a 2 when you get a 2 ,hit the enter button. else it will ask you to type yes.

These are the basic rules.
