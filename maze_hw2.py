####################################read the file and store them into an array
Maze_Type=input("input the name of maze")

Maze_file=open(Maze_Type+".txt","r")
Maze=Maze_file.readlines()
array=[]
for row in Maze:
    array.append(row.strip("\n").split(","))

row_num=array[0][0]
col_num=array[0][1].strip("\n")
del(array[0])

###################################check the position of start point and destination
start_j=0
destination_j=0
rows=0
for x in array:
    print(x)
    if "200" in x :
        start_j=x.index("200")
        start_i=rows

    if "201" in x:
        destination_j=x.index("201")
        destination_i=rows
    rows+=1
print("start=",start_i,start_j)
print("destination=",destination_i,destination_j)
#########################################
def move(position_i,position_j):
    if array[position_i+1][position_j]=="201" or array[position_i][position_j+1]=="201" or array[position_i-1][position_j]=="201" or array[position_i][position_j-1]=="201":    #distinguish whether 4 directions are the destination
        success=1
        array[position_i][position_j]="p"
        return success
        
    else:
        if array[position_i][position_j+1]=='0'and array[position_i][position_j+1]!="p":    #right
            array[position_i][position_j]="p"
            print("right")
            move(position_i,position_j+1)  
        elif array[position_i+1][position_j]=='0' and array[position_i+1][position_j]!='p': #down
            array[position_i][position_j]="p"
            move(position_i+1,position_j)  
            print("down")

        elif array[position_i][position_j-1]=='0' and array[position_i][position_j-1]!="p": #left
            array[position_i][position_j]="p"
            move(position_i,position_j-1)
            print("left")
        elif array[position_i-1][position_j]=='0' and array[position_i-1][position_j]!="p": #up
            array[position_i][position_j]="p"
            move(position_i-1,position_j)
            print("up")

        else:
            move(position_i,position_j-1)   #deal with the condition facing dead end
            array[position_i][position_j]="N"
        

start=[start_i,start_j]
destination=[destination_i,destination_j]

move(start_i,start_j)
for x in array:
    print(x)

# note:
# array[i][j]="p" first or recursion first???
