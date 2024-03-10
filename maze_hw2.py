
Maze_Type=input("input the name of maze")

Maze_file=open(Maze_Type+".txt","r")
Maze=Maze_file.readlines()
array=[]
for row in Maze:
    array.append(row.strip("\n").split(","))

row_num=array[0][0]
col_num=array[0][1].strip("\n")
del(array[0])

for j in array:
    print(j)
#print(row_num)
#print(col_num)