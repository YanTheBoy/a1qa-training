import math


def get_triangle_coords(filepath):
    with open(filepath, 'r') as file:
        coords = file.read().rstrip().split('\n')
    return coords


def calculate_vector(top1_coords, top2_coords):
    top1 = top1_coords.split(',')
    top2 = top2_coords.split(',')
    x = int(top2[0]) - int(top1[0])
    y = int(top2[1]) - int(top1[1])
    return [x, y]


def calculate_angle(vector1, vector2):
    cos_angle = ((vector1[0] * vector2[0]) + (vector1[1] * vector2[1])) \
                / (math.sqrt((vector1[0] ** 2) + (vector1[1] ** 2))
                   * (math.sqrt((vector2[0] ** 2) + (vector2[1] ** 2))))
    angle = math.degrees(math.acos(cos_angle))
    return int(angle)


def calculate_side(top1_coords, top2_coords):
    top1 = top1_coords.split(',')
    top2 = top2_coords.split(',')
    side = math.sqrt(
        ((int(top2[0]) - int(top2[1])) ** 2) +
        ((int(top1[0]) - int(top1[1])) ** 2)
    )
    return side


def calculate_triangle_area(side_a, side_b, side_c):
    p = (side_a + side_b + side_c) / 2
    triangle_s = math.sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))
    return round(triangle_s, 2)


def find_top_nearest_to_0x(tops_coords):
    triangle_tops_coords = [top.split(',') for top in tops_coords]
    tops_coordinates = sorted(triangle_tops_coords, key=lambda x_cord: x_cord[1])
    tops_nearest_to_ox = [tops_coordinates[0]]
    for top in tops_coordinates[1:]:
        if tops_coordinates[0][1] in top[1]:
            tops_nearest_to_ox.append(top)
    return tops_nearest_to_ox


if __name__ == '__main__':
    file_path = 'file.txt'
    coordinates = get_triangle_coords(file_path)
    triangles_tops = (triangle_coords.split(';') for triangle_coords in coordinates)
    for topA, topB, topC in triangles_tops:
        tops = {}
        all_tops = [topA, topB, topC]
        vectorAB = calculate_vector(topA, topB)
        vectorAC = calculate_vector(topA, topC)
        vectorBC = calculate_vector(topB, topC)
        tops[topA] = calculate_angle(vectorAB, vectorAC)
        tops[topB] = calculate_angle(vectorAB, vectorBC)
        tops[topC] = calculate_angle(vectorAC, vectorBC)
        for top_name, top_degrees in tops.items():
            if top_degrees == 90:
                print(f'Координаты вершины прямого угла: {top_name}')
                side_ab = calculate_side(topA, topB)
                side_ac = calculate_side(topB, topC)
                side_bc = calculate_side(topC, topA)
                triangle_area = calculate_triangle_area(side_ab, side_bc, side_ac)
                print(f'Площадь треугольника: {triangle_area}')
                tops_closest_to_axis = find_top_nearest_to_0x(all_tops)
                print('Ближайшие к оси ОХ вершины:', *tops_closest_to_axis)
                print('-----------------------')
