S_init = input()
N = int(input())

command = []
S_value = []

for _ in range(N):
    line = input().split()
    cmd = int(line[0])
    command.append(cmd)
    if cmd == 1 or cmd == 2:
        S_value.append(line[1])
    else:
        S_value.append("")

# Please write your code here.
class Node : 
    def __init__(self,data) :
        self.data = data 
        self.prev = None 
        self.next = None 

cur_node = Node(S_init)


for c in range(len(command)) : 
    node = Node(S_value[c])

    if(command[c]==1) :
        #현재 노드에 앞이 없다면 
        if(cur_node.prev == None) :
            #현재 노드의 앞을 노드로 할당 
            cur_node.prev = node 
            #노드의 뒤를 현재 노드로 할당 
            node.next = cur_node
        #현재 노드에 앞이 있다면 
        else :
            #앞에 있던 노드를 새 노드에 앞으로 할당 
            node.prev = cur_node.prev
            #앞에 있던 노드의 뒤를 현재노드로 할당  
            cur_node.prev.next = node 

            #새 노드의 뒤를 현재 노드로 할당 
            node.next = cur_node
            cur_node.prev = node 

    elif(command[c]==2) :
        #현재 노드의 뒤가 없다면
        if(cur_node.next == None) :
            #현재 노드의 뒤를 노드로 할당 
            cur_node.next = node 
            #노드의 앞을 현재 노드로 할당 
            node.prev = cur_node 
        #현재 노드의 뒤가 있다면 
        else :
            #뒤에있던 노드를 새 노드의 뒤로 할당 
            node.next = cur_node.next 
            #뒤에 있던 노드의 앞을 현재 노드로 할당 
            cur_node.next.prev = node 

            #새 노드의 앞을 현재 노드로 할당 
            node.prev = cur_node
            cur_node.next = node 

    elif(command[c]==3) :
        if(cur_node.prev) :
            cur_node = cur_node.prev 

    else :
        if(cur_node.next) :
            cur_node = cur_node.next 
    
    if(cur_node.prev == None) :
        print("(Null)",end=' ')
    else :
        print(cur_node.prev.data,end=' ')
    
    print(cur_node.data,end=' ')
    
    if(cur_node.next == None) :
        print("(Null)",end=' ')
    else :
        print(cur_node.next.data,end=' ')
    print()
    

