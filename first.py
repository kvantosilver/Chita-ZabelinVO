n = int(input())
soldiers = []
for _ in range(n):
    soldiers.append(input())
k = int(input())
m = int(input())
for _ in range(m):
    del soldiers[k - 1::k]
for soldier in soldiers:
    print(soldier)