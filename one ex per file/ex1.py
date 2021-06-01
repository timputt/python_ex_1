# part 1
# task:  L = [0, [], [1,2,3,4], [[5],[6,7]], [8,9,10]]
# using both, indexing and slicing on L, assemble and print a new list N that contains:
# [0,2,3,[5,6],8,10] 
# as an example, here's  how i've constructed a similar list X which contains [[2, 3], [10]] from L:
#
# L = [0, [], [1,2,3,4], [[5],[6,7]], [8,9,10]]
# X = [ L[2][1:-1], L[-1][2] ] 
# print(x)  => [[2, 3], [10]]
# You need to do something similar but end up with [0,2,3,[5,6],8,10] instead. One way to work 
# through this is to break the process down in small steps, store result of each step in a new variable
# and use those variables in the next step
print("start of part 1") # set breakpoint here
L = [0, [], [1,2,3,4], [[5],[6,7]], [8,9,10]]
print(L)


print("Tim's code:") # This is where my stuff starts
# GOAL [0,2,3,[5,6],8,10] 


#I chunked each value so I could approach it one at a time. A lot of trial and error!!
#Definitely spent some time on www.learnbyexample.org/python-list-slicing/

value1 = L[0]
value2 = L[2][1]
value3 = L[2][2]
value4 = [L[3][0][0],L[3][1][0]]
value56 = L[4][0:3:2]

#I pieced the values together in a way so that the new list would look like the target goal. 
N = [value1,value2, value3, value4, value56[0],value56[1]]
print(N)



print("end of 1") # set breakpoint here 
'''

























# solution 2
L = [0, [], [1,2,3,4], [[5],[6,7]], [8,9,10]]
print("L is", L)
tmp1 = L[0] # 0
tmp2 = L[2][1] # 2
tmp3 = L[2][2] # 3
tmp4 = [L[3][0][0], L[3][1][0]] # [5, 6]
tmp5 = L[4][0] # 8
tmp6 = L[4][-1] # 10 
newL = [tmp1, tmp2, tmp3, tmp4, tmp5, tmp6] # create final list
print(newL) # [0, 2, 3, [5, 6], 8, 10]
'''