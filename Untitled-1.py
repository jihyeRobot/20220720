def solution(answers):
    sunho=[1,2,3,4,5]
    namhyeon=[2,1,2,3,2,4,2,5]
    jihye=[3,3,1,1,2,2,4,4,5,5] #반복되는 수열
    
    
    score=[0,0,0]  #세 개의 점수 배열로

    for i in range(len(answers)):
        s1=i%5
        s2=i%8
        s3=i%10 #반복되는 수열의 개수를 계산
     
     #정답과 수열의 수가 같으면 +1   
        if sunho[s1]==answers[i]:
            score[0]+=1 
        if namhyeon[s2]==answers[i]:
            score[1]+=1
        if jihye[s3]==answers[i]:
            score[2]+=1
        
    #가장많이 숫자를 맞춘사람
    
    
    winner=max(score)
    result=[]
    
    #최대값 찾기
    for i in range(3):
        if score[i]==max(score):
            result.append(i+1)
            
    return result

answer=[1,3,2,4,2]

print(solution(answer))


    """
    for 
    """