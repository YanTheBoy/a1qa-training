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
    triangle_tops_coordinates = sorted(triangle_tops_coords, key=lambda x_cord: x_cord[1])
    tops_nearest_to_ox = [triangle_tops_coordinates[0]]
    for top in triangle_tops_coordinates[1:]:
        if triangle_tops_coordinates[0][1] in top[1]:
            tops_nearest_to_ox.append(top)
    return tops_nearest_to_ox


def get_vectors_and_angles(triangle_tops_coords):
    for topA, topB, topC in triangle_tops_coords:
        tops = {}
        vector_ab = calculate_vector(topA, topB)
        vector_ac = calculate_vector(topA, topC)
        vector_bc = calculate_vector(topB, topC)
        tops[topA] = calculate_angle(vector_ab, vector_ac)
        tops[topB] = calculate_angle(vector_ab, vector_bc)
        tops[topC] = calculate_angle(vector_ac, vector_bc)
        yield [topA, topB, topC, tops]


def get_triangle_values(tops_coords, angle):
    top_a, top_b, top_c, tops = tops_coords
    all_tops = [top_a, top_b, top_c]
    for top_name, top_degrees in tops.items():
        if top_degrees == angle:
            side_ab = calculate_side(top_a, top_b)
            side_ac = calculate_side(top_b, top_c)
            side_bc = calculate_side(top_c, top_a)
            triangle_area = calculate_triangle_area(side_ab, side_bc, side_ac)
            tops_closest_to_axis = find_top_nearest_to_0x(all_tops)
            return {
                'top_name': top_name,
                'area': triangle_area,
                'closest_to_axis': tops_closest_to_axis
                }


if __name__ == '__main__':
    set_angle = 90
    file_path = 'file.txt'
    coordinates = get_triangle_coords(file_path)
    triangles_tops = (triangle_coords.split(';') for triangle_coords in coordinates)
    tops_coordinates = get_vectors_and_angles(triangles_tops)
    for triangle in tops_coordinates:
        values = get_triangle_values(triangle, set_angle)
        if values is not None:
            print(f'Координаты вершины прямого угла: {values["top_name"]}')
            print(f'Площадь треугольника: {values["area"]}')
            print('Ближайшие к оси ОХ вершины:', *values["closest_to_axis"])
            print('-----------------------')
