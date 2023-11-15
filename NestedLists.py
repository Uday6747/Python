l = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    l.append([name, score])
l = sorted(l, key = lambda x : x[1])
second = l[1][1]
second_name = sorted([item[0] for item in l if item[1]==second])
print("\n".join(second_name))




