n = int(input())
student_marks = {}
for _ in range(n):
    name , *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()

for i in student_marks.keys():
    print("Value of i : ",i)
    if i == query_name:
        print(format((sum(student_marks[i])/len(student_marks[i])),".2f"))
        

        
