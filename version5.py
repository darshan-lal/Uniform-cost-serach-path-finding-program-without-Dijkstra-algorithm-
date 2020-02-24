#darshan lal
#1001667684
#dnl7684


#										#For using heap queue 
from heapq import heappush, heappop

#										#User input
query=raw_input("Enter the input in the form (find_route inputfile.txt source destination )") #taking input query

#										#Spliting the raw input into variables
try:
	_, inputfile, Source, Destination, h_file = query.split()
	#									#h is used to know wheather heuristic file is provided or not 
	h=1
except:
	_, inputfile, Source, Destination = query.split()
	#									#h is used to know wheather heuristic file is provided or not
	h=0

#										#Reading input file into a list
file = open(inputfile, 'r')                                  			#The graph file is opened here in read mode
data = file.readlines() 
data = [x.strip().split() for x in data] 

#										#Checking for end of file
if data[-1:][0][0] == 'END':
	data.pop()

#										Dictionary is used to store the data of the input file 
Graph = {} 
for record in data:
	src = record[0]
	dest = record[1]
	cst = record[2]
	if src not in Graph:
		Graph[src] = {}
	if dest not in Graph:
		Graph[dest] = {}
	
	#									#As the graph is bidirectional from cost(src to dest)=cost(dest to src )
	Graph[src][dest] = int(cst)
	Graph[dest][src] = int(cst)

#										#if we have a heuristic enter 
if h==1:
	#									#Reading heuristic file into a list
	file = open("h_kassel.txt", 'r')
	data = file.readlines()
	data = [x.strip().split() for x in data] 

	#									#Checking for end of file
	if data[-1:][0][0] == 'END': 
	        data.pop()

	#									#Dictionary is used to store the data of the input file
	H_of = {}

	for record in data:
        	city = record[0]
        	heu = record[1]
        	if city not in H_of:
        	        H_of[city] = {}
        	H_of[city] = int(heu)

#										#This function expands the nodes	
def expand(graph,s,goal,h_of,h):
        
	fringe = []								#Fringe (Heap queue is used)
        visited_nodes = {}							#To keep track of nodes visited
        prev_nodes = {}
        visi=0									#To keep track of nodes expanded
        
        #                                                                       #if we have a heuristic enter
        if h==1:
                heu=h_of[s]
        else:
                heu=0
        
	heappush(fringe,(heu,0,s,None,0))                                  	#putting the source into the fringe
        for nodes in graph:
                visited_nodes[nodes] = False
                prev_nodes[nodes] = None
        i = 1
        while len(fringe) != 0:
                i = i+1
                #								#fringe pops the lowest node for optimial path
                hval,total_cost, current_node, prev_node, link_cost = heappop(fringe) 
                visi=visi+1

                #								#checking if node visited or not
		if visited_nodes[current_node] == False:     
			visited_nodes[current_node] = True 
                        prev_nodes[current_node] = []
                        prev_nodes[current_node].append(prev_node)
                        prev_nodes[current_node].append(link_cost)

                        #							#Checking if we got the goal	
                        if current_node == goal:
 
                                final_path = []
                                while current_node != s:
                                        temp = []
                                        temp.append(current_node)
                                        for i in prev_nodes[current_node]:
                                                temp.append(i)
                                        final_path.append(temp)
                                        current_node = prev_nodes[current_node][0]
                                final_path.reverse()

                                return total_cost,final_path,visi		#returning the result
 
                        for neighbors, ncost in graph[current_node].items():
                                if visited_nodes[neighbors] == False:
                                        this_link_cost = ncost
					if h==1:
						heu2=h_of[neighbors]
					else:
						heu2=0
                                        new_cost = total_cost + ncost 
					new_h=new_cost+heu2
                                        heappush(fringe, (new_h,new_cost, neighbors, current_node, ncost))
        return 0,visi  								#if no path is available

#                                                                               #if we have a heuristic enter
if h==1:
	result = expand(Graph,Source,Destination,H_of,h)
else:
	result = expand(Graph,Source,Destination,0,h)                                                                                                             
if result[0] == 0:
	print "\nnodes expanded: ",result[1]
	print "distance: infinity"
	print "route: none\n"
else:
	print "\nnodes expanded: ",result[2]
	print "distance:",result[0],"km"
	print "route: "
	for line in result[1]:

		print "%s to %s, %s km" % (line[1],line[0],line[2])
