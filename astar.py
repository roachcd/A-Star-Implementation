from node import Node
class Astar:
    def __init__(self, maze):
        self.maze = maze.get_maze()
        self.start = maze.get_start()
        self.end = maze.get_end()
        self.open_list = []
        self.closed_list = []
        self.path = []

        #add start node to open list
        x, y = maze.start
        self.open_list.append(maze.maze[y][x])

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1]) #Distance to end node

    def get_path(self):
        return self.path

    #continue to next step of A*
    def step(self):
        current_node = min(self.open_list, key=lambda n: n.f)
        self.open_list.remove(current_node)
        self.closed_list.append(current_node)

        if(current_node.is_end):
            while current_node:
                self.path.append(current_node)
                current_node = current_node.parent
            self.path = self.path[::-1]
            return False
        
        x, y = current_node.position
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            child_pos = (x + dx, y + dy)
            child_x, child_y = child_pos
            if(0 <= child_y < len(self.maze)):
                if(0 <= child_x < len(self.maze[0])):
                    child = self.maze[child_y][child_x]

                    if(child.is_wall):
                        continue

                    if(child in self.closed_list):
                        continue

                    child.parent = current_node
                    child.g = current_node.g + 1
                    child.h = self.heuristic(child_pos, self.end)
                    child.f = child.g + child.h

                    if any(n.position == child.position and n.f <= child.f for n in self.open_list):
                        continue

                    self.open_list.append(child)

        return True
        
