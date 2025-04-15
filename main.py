from maze import Maze;
from astar import Astar

import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.widgets import Slider
import numpy as np

speed = 1

def update_speed(val):
    global speed
    speed = val

def main():
    maze = Maze()
    data = np.array(maze.get_maze())
    astar = Astar(maze)
    grid = update_grid(maze.maze)

    plt.ion()
    fig, ax = plt.subplots()
    cmap = colors.ListedColormap(['white', 'gray', "purple", "blue", "red", "yellow"])
    bounds = [0,1,2,3,4,5,6]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    img = ax.imshow(grid, cmap=cmap, norm=norm)

    ax_slider = plt.axes([0.3, .9, 0.4, 0.03], facecolor='lightgoldenrodyellow')
    slider = Slider(ax_slider, 'Speed', 0.01, 1, valinit=1)
    slider.on_changed(update_speed)

    while astar.step():
        astar.step()
        draw_grid(img, fig, update_grid(maze.maze))
        plt.pause(speed)

    print(astar.get_path())
    draw_grid(img, fig, update_grid(maze.maze, astar.get_path()))

    plt.ioff()
    plt.show()

#updates matplotlib grid
def draw_grid(img, fig, grid):
    img.set_data(grid)
    fig.canvas.draw()
    fig.canvas.flush_events()

#Convert objects into numbers for rendering
#0 = empty
#1 = wall
#2 = has parent
#3 = is start
#4 = is end
#5 = in path
def update_grid(maze, path=[]):
    grid = []
    for y in maze:
        working = []
        for x in y:
            if(x in path):
                working.append(5)
                continue
            if(x.is_start):
                working.append(3)
            elif(x.is_end):
                working.append(4)
            elif(x.is_wall):
                working.append(1)
            elif(x.parent != None):
                working.append(2)
            else:
                working.append(0)

        grid.append(working)
    return grid

if __name__ == "__main__":
    main()