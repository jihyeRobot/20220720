
from collections import Counter

N=5

stages=[2, 1, 2]
def solution(N, stages):
    
    print('힝')
    counter=Counter(stages)
    
    for  N in stages:
        stages[N]+=1
                
    print(stages)
    
    for i in range(N):
        if i ==True :
            i+=1
        else :
            return
        
       
solution(N, stages)
        
        