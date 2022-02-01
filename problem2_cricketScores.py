
def cricket_scores(scores):
    p1,p2=0,0
    to_add=None
    for i in range(0,len(scores)):
        player_score=scores[i]

        #for first elemnt of array
        if i==0 and player_score%2!=0:
            to_add='p2'
            p1+=player_score
        elif i==0 and player_score%2==0 :
            p2+=player_score
            to_add='p1'
        
        
        if i!=0:
            if to_add=='p1':
                p1+=player_score
            else:
                p2+=player_score

            
            to_add='p2' if player_score%2==0 and to_add=='p2' else 'p1'
   
    individual_scores={'p1':p1,'p2':p2}
    return individual_scores

print(cricket_scores([1,2,3,2,1]))