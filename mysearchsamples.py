def bfs(graph, start_node):
  """Performs a breadth-first search on a graph.

  Args:
    graph: A graph represented as a dictionary of adjacency lists.
    start_node: The starting node for the BFS.

  Returns:
    A list of the nodes visited in the BFS.
  """

  visited = set()
  queue = [start_node]

  while queue:
    node = queue.pop(0)
    visited.add(node)

    for neighbor in graph[node]:
      if neighbor not in visited:
        queue.append(neighbor)

  return visited
graph = {
  0: [1, 2],
  1: [3],
  2: [4],
  3: [],
  4: [],
}

start_node = 0
visited_nodes = bfs(graph, start_node)

print(visited_nodes)


# Here is a pseudocode implementation of DFS:

def dfs(graph, start_node):
  # Mark the start node as visited.
  visited[start_node] = True

  # Explore all of the neighbors of the start node.
  for neighbor in graph[start_node]:
    if not visited[neighbor]:
      dfs(graph, neighbor)
  # Backtrack.
def dfs(graph, start_node):
  visited = set()

  def _dfs(node):
    visited.add(node)

    for neighbor in graph[node]:
      if neighbor not in visited:
        _dfs(neighbor)

  _dfs(start_node)

  return visited

graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': [],
  'F': [],
}

start_node = 'A'
end_node = 'F'

visited = dfs(graph, start_node)

path = []

current_node = end_node

while current_node != start_node:
  path.append(current_node)
  current_node = visited[current_node]

path.reverse()

print(path)