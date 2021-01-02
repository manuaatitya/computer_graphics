from point_inside_triangle import point_within_triangle

# Invoke class to execute the function
t = point_within_triangle()
t.get_input_point()
t.get_input_triangle()
t.compute_cross_product()
if(t.point_within_triangle):
    print('Point lies within the triangle')
elif(t.point_intersects_triangle):
    temp = t.intersecting_edge
    print('Point lies on edge connecting Point {} ({}, {}) and Point {} ({}, {}) of the triangle'.format(temp + 1, t.triangle[temp].x, t.triangle[temp].y, temp + 2, t.triangle[(temp + 1)%3].x, t.triangle[(temp + 1)%3].y))
else:
    print('Point lies outside the triangle')