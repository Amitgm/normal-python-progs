class checker:
 def func(list1,player1points,player2points,player):
    while (list1!=[]):
        print("the end of game, no choice area for player ",player)
        list1.remove(2)
        print(list1)
        if(player=='max'):
             player1points=player1points+2
             print(player1points)
        else:
             player2points=player2points+2
             print(player2points)
        if(player=='max'):
            player='min'
        else:
           player='max'
    return player1points,player2points
 

