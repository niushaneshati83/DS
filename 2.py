import pdb

graph = {}
color={}
depth={}
parents = {}
k =  []
n = input()
for i in range(int(n)):
    graph[i + 1] = []
    color[i + 1] = "white"
    depth[i + 1] = 0
    parents[i+ 1] = 0

for i in range(int(n)-1):
    u1, u2 = input().split()
    graph[int(u1)].append(int(u2)) 
    graph[int(u2)].append(int(u1))

k = input().split()
def dfs(u):
    color[u] = "gray"
    for v in graph[u]:
        if color[v] == "white":
            depth[v] = depth[u] + 1  
            parents[v] = u
            dfs(v)
    color[u] = "black"  

start_node = 1 
dfs(start_node)

# for i in range(int(n)):
#     print(graph[i+1], color[i+1], parents[i+1])

def find_path(n1, n2):
    global depth
    path = []
    path_fake = []
    # print(depth[n1])
    # print(n2)
    if depth[n1] >= depth[n2]:
        for i in range(depth[n1] - depth[n2]):
            path.append(n1)
            n1 = parents[n1]
        while n1 != n2:
            path.append(n1)
            path_fake.append(n2)
            n2 = parents[n2]
            n1 = parents[n1]
        path.append(n1)
        path_fake.reverse()
        path.extend(path_fake)
    else:
        for i in range(depth[n2] - depth[n1]):
            path_fake.append(n2)
            n2 = parents[n2]
        while n1 != n2:
            path.append(n1)
            path_fake.append(n2)
            n2 = parents[n2]
            n1 = parents[n1]
        path.append(n1)
        path_fake.reverse()
        path.extend(path_fake)
    return path

# pdb.set_trace()
paths = []
# print(depth, parents)
 
paths.extend(find_path(start_node, int(k[0])))
for i in range(len(k) - 1):
    paths.pop()
    paths.extend(find_path(int(k[i]), int(k[i + 1])))
paths.pop()
paths.extend(find_path(int(k[-1]), start_node))

paths.pop()
if len(paths) == 2*int(n) - 2:
    print(*paths)
else:
    print(-1)


