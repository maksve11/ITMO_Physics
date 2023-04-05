import math
from py_linq import Enumerable
import matplotlib.pyplot as plt


# Some helpfull functions. Nothing to see here.
def distance(x1, x2, y1, y2):
    res = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return res


def intersect(x1, x2, y1, y2, eps):
    if len(x1) != len(y1) or len(x2) != len(y2) or len(x2) != len(x1):
        assert ("len x and len y should be equal")

    points = []
    for i in range(len(x1)):
        dist = distance(x1[i], x2[i], y1[i], y2[i])
        if dist <= eps:
            points.append((x1[i], y1[i], dist))

    points = Enumerable(points)
    min_dist = points.select(lambda x: x[2]).min()
    min_point = points.where(lambda x: x[2] == min_dist).first()
    if min_point is None:
        assert ('No intersection found')

    return min_point[0], min_point[1]


def print_points_table(points):
    fig, ax = plt.subplots()
    columns = ('n', 'x', 'y')
    rows = [i + 1 for i in range(len(points))]

    table_data = []
    for i in range(len(points)):
        table_data.append([i + 1, f'{points[i][0]:.3f}', f'{points[i][1]:.3f}'])

    table = ax.table(cellText=table_data,
                     colLabels=columns,
                     rowLabels=rows,
                     loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    for key, cell in table.get_celld().items():
        cell.set_linewidth(1)
    table.scale(1, 1.5)
    ax.axis('off')
    plt.show()


def gorgeous_scientific_print(x):
    for i in x:
        print(f'{i:.3e}', end=" ")
    print('\n')