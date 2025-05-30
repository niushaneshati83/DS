graph = {}
color={}
depth={}
n, m = (input().split())
for i in range(int(n)):
    graph[i + 1] = []
    color[i + 1] = "white"
    depth[i + 1] = 0
for i in range(int(m)):
    u1, u2 = input().split()
    graph[int(u1)].append(int(u2)) 
    graph[int(u2)].append(int(u1))

def bfs(start):
    # visited = set()  
    queue = [start]  
    # visited.add(start)

    while queue:
        node = queue.pop(0)  
        color[node] = 'black'
        for nei in graph[node]:
            if color[nei] == 'white':
                # visited.add(nei)
                color[nei] = 'black'
                depth[nei] = depth[node] + 1
                queue.append(node)


for i in range(int(n)):
    if color[i + 1] == "white":
        bfs(i + 1) # starting node bfs


ans = []
for i in range(int(n)):
    if(depth[i + 1] % 2 == 1):
        ans.append(str(i + 1))

print(len(ans))
print(' '.join(ans))
