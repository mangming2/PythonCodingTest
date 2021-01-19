s=input()
def solution(s):
    answer = ""
    counter = 0
    for i in range(len(s)):
        if s[i] == " ":
            counter = 0
            answer += " "
        elif counter % 2 == 0:
            answer +=s[i].upper()
            counter +=1
        elif counter % 2 == 1:
            answer += s[i].lower()   
            counter +=1
    return answer
print(solution(s))