'''
A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
'''


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


nodes = set()
graph = {}
with open('./data/p079_keylog.txt') as f:
    lines = f.readlines()
    for line in lines:
        for i in range(len(line)):
            current = line[i]
            next = line[i + 1]
            if current not in graph:
                nodes.add(current)
                if next != '\n':
                    graph[current] = set(next)
                else:
                    graph[current] = set()
                    break
            else:
                if next != '\n':
                    graph[current].add(next)
                else:
                    break

for key in graph:
    if len(graph[key]) == 0:
        target = key
    else:
        for n in graph[key]:
            nodes.discard(n)
start = nodes.pop()

pathes = list(bfs_paths(graph, start, target))
password = max(pathes, key=len)
print(''.join(password))
