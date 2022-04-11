# функции
from random import randint

min_limit = -10
max_limit = 10


def print_point(point):
    print(f'({point["x"]}, {point["y"]}, {point["z"]})')


def create_point(min_limit, max_limit):
    # print(min_limit, test_value)
    point = {"x": randint(min_limit, max_limit),
             "y": randint(min_limit, max_limit),
             "z": randint(min_limit, max_limit)}
    return point


test_value = 12

point_a = create_point(min_limit, max_limit)
print_point(point_a)

point_b = create_point(1, 100)
print_point(point_b)

point_c = create_point(-200, -100)
print_point(point_c)

triangle_abc = (point_a, point_b, point_c)
print(triangle_abc, min_limit)
