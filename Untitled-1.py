
2
3
4
5
6
def solution(array, commands):
    answer = []
    for com in commands:
        answer.append(sorted(array[com[0]-1:com[1]])[com[2]-1])#이 줄 해석하기
   #append : ()안에 값을 입력하면 새로운 요소를 array 맨끝에 객체로 추가
   #sorted : 첫번째 매게변수로 들어온 이터러블한 데이터를 새로운 정렬된 리스트로 만들어서 반환해주는 함수
   #[com[0]-1:com[1]])[com[2]-1] : 선호오빠에게 물어보기
    return answer

