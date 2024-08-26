# 5 5 5 5 5 
# 4 4 4 4 4
# 3 3 3 3 3

# for i in range(3) :
#     for j in range(5) :
#         print(i+1 , end=" ")
#     print()

# 5 5 5 5 5 
# 4 4 4 4 4
# 3 3 3 3 3

# for i in range(5,2,-1) :
#     for j in range(5) :
#         print(i , end=" ")
#     print()


# 1 2 3 4 5
# 2 3 4 5 6
# 3 4 5 6 7
# 4 5 6 7 8

for i in range(4):
    for j in range(1,6) :
        print(j+i , end=" ")
    print()

# 8 7 6 5 4
# 7 6 5 4 3
# 6 5 4 3 2
# 5 4 3 2 1
    
for i in range(4) :
    for j in range(8,3,-1) :
        print(j-i , end=" ")
    print()

# 1 2 3 4 5 6
# 3 4 5 6 7 8
# 5 6 7 8 9 10
# 7 8 9 10 11 12

x=0
for i in range(8,4,-1) :
    for j in range(8,3,-1) :
        print(j-x , end=" ")
    x += 1
    print()

# atau 
    
for i in range(1,8,2) :
    for j in range(i,i+6):
        print(j, end=" ")
    print()
    

# 9 7 5 3 1
# 6 4 2 0 -2 
# 3 1 -1 -3 -5
# 0 -2 -4 -6 -8


# x=0
# for i in range(4) :
#     for j in range(9,0,-2) :
#         print(j-x , end=" ")
#     x += 3
#     print()

for i in range(9,-1,-3) :
    for j in range(i,i-9,-2):
        print(j, end=" ")
    print()

# 1 
# 2 2 
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
    
for i in range(1,6):
    for j in range(6-i) :
        print(i, end=" ")
    print()

# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5
    


    
