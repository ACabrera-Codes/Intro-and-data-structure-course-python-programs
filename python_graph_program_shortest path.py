#program to show shortest path from one poitn to another in our graph 
graph = {'a':['c'],'b':['d'],'c':['e'],'d':['a','d'],'e':['b','c']}
def find_shortest_path(graph,start,end,path = []):
    path = path + [start]
    if start == end:
        return path
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph,node,end,path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath #establish a check to look for new path /short through dictioanry to find the short path
#then it repalces new path with the short path 
            return shortest

print(find_shortest_path(graph,'a','e'))