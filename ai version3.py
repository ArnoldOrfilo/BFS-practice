     #    ######   #     #  #####  #       ####
    # #   #     #  # #   # #     # #       #   #
   #   #  ######   #  #  # #     # #       #    #
  ####### # #      #   # # #     # #       #    #
 #       ##  #     #    ## #     # #       #   #
#         #    # ###     #  #####  ####### # #


# In my code, I divide the task into three functions. The first function is to extract information from the file. It will create a dictionary which containing all connections between nodes. I create the connections in both way, for example, if A is connected to B, then A will in key B, B will also in key A. 
# Then, in the second function, it takes the start node and the end node as input. It will find out the visited nodes from the start node to the end node level by level in BFS. Basically the same method as we simulation on the white broad. it add nodes to visited and queue based on levels.
# Afer that, I withdraw the path by reversing the visited list, it will find out the path to the end node in a reversed order. then, reverse the reversed path, you get the path in the correct order.



def extract_connection():

    key_set=[] 
    d={}
    

    f = open("Graph_info.txt","r")
    content = f.readlines()
    f.close()


    for temp_line in content:
        if temp_line[1] not in key_set:
            key_set.append(temp_line[1])

    for temp_line in content:
        if temp_line[20] not in key_set:
            key_set.append(temp_line[20])


    for n in content: # n is each line
        if n[1] not in d: # the first node
            d[n[1]] = [] # create all keys according to discription 

    for late_key in key_set:
        if late_key not in d:
            d[late_key]=[] #add keys that not in the discription

        
    for m in content: # m is each line
        if n[1] in d: 
            d[m[1]].append(m[20]) # fill in content to keys



    for keys in d: 
        for values in d[keys]: 
            if values in d: # if the value also a key
                if keys not in d[values]:#if it haven't in the list yet
                    d[values].append(keys)

    return d



def find_path(d,start,end):
        
        key_set=[]
        for keys in d:
            key_set.append(keys)
        
        
        queue=[]
        visited=[]
       
        

        for i in key_set:
            if i==start:
                
                queue.append(start)

        while queue:

            temp_list=[]
            temp_list2=[]

            for child_node in queue:
                    
                if child_node!=end:
                        
                    for counter in range(len(d[child_node])):
                        visited_=False

                        for index in range(len(visited)):
                            if d[child_node][counter] in visited[index]:
                                visited_=True

                        if visited_==False:
                            temp_list.append(d[child_node][counter])

                    if child_node not in temp_list2 :
                        temp_list2.append(child_node)   
                            

                        
                        
                            
                elif child_node==end:
                        
                    visited.append([end])
                    return visited
                        
            visited.append(temp_list2)
                

                        


                
            queue.clear()

            for counter in range(len(temp_list)):
                _visited=False
                for index in range(len(visited)):

                    if temp_list[counter] in visited[index]:
                        _visited=True

                if _visited==False:
                    queue.append(temp_list[counter])


def complete_visited_list(d,start):
        
        key_set=[]
        for keys in d:
            key_set.append(keys)
        
        
        queue=[]
        visited=[]
       
        

        for i in key_set:
            
            if i==start:
                
                queue.append(start)
               

        while queue:
          

            temp_list=[]
            temp_list2=[]

            for child_node in queue:
                    
                
                        
                for counter in range(len(d[child_node])):
                    visited_=False

                    for index in range(len(visited)):
                        if d[child_node][counter] in visited[index]:
                            visited_=True

                    if visited_==False:
                        temp_list.append(d[child_node][counter])

                if child_node not in temp_list2 :
                    temp_list2.append(child_node)
                             

            visited.append(temp_list2)
                
                
            queue.clear()

            for counter in range(len(temp_list)):
                _visited=False

                for index in range(len(visited)):
                    if temp_list[counter]in visited[index]:
                        _visited=True

                if _visited==False:
                    queue.append(temp_list[counter])


        return visited








def extract_connection():

    key_set=[] 
    d={}
    

    f = open("Graph_info.txt","r")
    content = f.readlines()
    f.close()


    for temp_line in content:
        if temp_line[1] not in key_set:
            key_set.append(temp_line[1])

    for temp_line in content:
        if temp_line[20] not in key_set:
            key_set.append(temp_line[20])


    for n in content: # n is each line
        if n[1] not in d: # the first node
            d[n[1]] = [] # create all keys according to discription 

    for late_key in key_set:
        if late_key not in d:
            d[late_key]=[] #add keys that not in the discription

        
    for m in content: # m is each line
        if n[1] in d: 
            d[m[1]].append(m[20]) # fill in content to keys



    for keys in d: 
        for values in d[keys]: 
            if values in d: # if the value also a key
                if keys not in d[values]:#if it haven't in the list yet
                    d[values].append(keys)

    return d




        
       


def withdraw_path(d,visited):

    visited_reverse=[]
    path_reverse=[]
    counter=len(visited)-1

    while counter>=0:
        
        visited_reverse.append(visited[counter])
        counter-=1
    
    #print(visited_reverse)
        counted=[]
    path_reverse.append(visited_reverse[0][0]) #add the very first element which is the end node of path

    for i in range(len(visited_reverse)-1): 
        for j in visited_reverse[i]: # node in current level
            for node in visited_reverse[i+1]: #node in previous level
                if j in d[node] and node not in path_reverse and visited_reverse[i+1]not in counted: # check if current node connected with previous level node, and only add one in same level
                    path_reverse.append(node)
                    counted.append(visited_reverse[i+1])
                    
    

    path=[]
    counter2=len(path_reverse)-1

    while counter2>=0:
        path.append(path_reverse[counter2])
        counter2-=1

    print("\n This is the path >> \n",path)
                
       



d=extract_connection()
print("\nThis is the connection between nodes >> \n",d)

while True:

    start_node=input("Enter the start node in uppercase >>")
    end_node=input("Enter the end node in uppercase >>")
    if start_node not in d or end_node not in d:
        print("Error!")

    else: 
        visited=find_path(d,start_node,end_node)
        complete_visited=complete_visited_list(d,start_node)
        print("\nThis is the path divided by levels in BFS >> \n",visited)
        print("\n And this is the complete visited list>> \n",complete_visited)

        withdraw_path(d,visited)
        break
