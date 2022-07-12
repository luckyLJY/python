import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk(500000)
    rw.fill_walk()

    # 设置绘图窗口尺寸和屏幕分辨率
    plt.figure(dpi=128,figsize=(10,6))

    # Remove the axes. 注意先后顺序
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    point_numbers = range(rw.num_points)
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolors='none', s=1)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=100)



    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
