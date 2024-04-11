import simple_draw as sd

# Нарисовать ветку дерева из точки (300, 5) вертикальннов верх длиной 100

point_0 = sd.get_point(300, 5)
sd.resolution = (1200, 600)

# сделать функцию рисования из заданной точки
#  Заданна длина с заданным наклоном

def branch(point, angle, length, delta):
    if length < 1:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle- delta
    next_lenght = length * .75
    branch(point=next_point, angle=next_angle, length=next_lenght, delta= delta)

for delta in range (0, 51, 10):
    branch(point=point_0, angle=90, length=150, delta= delta)
for delta in range (-50, 1, 10):
    branch(point=point_0, angle=90, length=150, delta= delta)




sd.pause()
#
# angle_0 = 90
# length_0 = 200
#
# next_point = point_0
# next_angle = angle_0
# next_lenght= length_0
#
# while next_lenght > 10:
#     next_point = branch(point=next_point, angle=next_angle, length=next_lenght)
#     next_angle = next_angle - 30
#     next_lenght = next_lenght * 0.75


#next_point = branch(point=next_point, angle=next_angle, length=next_lenght )
#next_angle = next_angle - 30
#next_lenght = next_lenght* .75
#next_point = branch(point=next_point, angle=next_angle, length=next_lenght)


