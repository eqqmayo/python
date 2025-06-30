# print('*')
# print('**')
# print('***')
# print('****')
# print('*****')

def draw_right_triangle(lines):
    for i in range(1, lines + 1):
        print(('*' * i).rjust(lines, ' ')) 

def draw_inverse_right_triangle(lines):
    for i in range(lines, 0, -1):
        print(('*' * i).rjust(lines, ' ')) 

def draw_center_triangle(lines):
    for i in range(1, lines + 1, 2):
        print(('*' * i).center(lines, ' ')) 


# draw_right_triangle(6)
draw_inverse_right_triangle(5)
# draw_center_triangle(11)

