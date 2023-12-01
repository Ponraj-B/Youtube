print("Enter the row value")
row = int(input())
print("Enter the colmn value")
col = int(input())
num = 1
for i in range(row):
    for j in range(col):
        print(num,end=" ")
        num+=1
    print("\n")
