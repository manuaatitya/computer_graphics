# Point class to store the x and y values of the coordinates
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

# Man class to check if the point intersects the triangle
class point_and_triangle:

    # Initiaization function
    def __init__(self):
        self.triangle = []

        # Barycentric weights
        self.u = 0
        self.v = 0

        self.point_outside_triangle = 0
        self.point_on_triangle = 0
        self.point_inside_triangle = 0
        self.intersecting_edge = [-5,-5]   # Dummy variable for initialization
        self.intersecting_vertex = -1

        print('Python program to test if a Point is within a triangle')

    # Get the Point data as input data from the user
    def get_input_point(self):
        print('\nEnter the cordinates for the point \n')
        x,y = map(float,input('Enter the x and y cordinates of the Point P to be tested  ').split())
        self.point = Point(x,y)
    
    # Get the triangle coordinates as input data from the user
    def get_input_triangle(self):
        print('\nEnter the cordinates for the triangle \n')
        for i in range(3):
            x,y = map(float,input('Enter the x and y cordinates of the Point {} of the triangle  '.format(i+1)).split())
            self.triangle.append(Point(x,y))

    # Compute a vector from the given points
    def compute_vector(self, point1, point2):
        return Point(point2.x - point1.x, point2.y - point1.y)

    # Method to compute dot product between two vectors
    def compute_dot_product(self, vector1, vector2):
        return vector1.x * vector2.x + vector1.y + vector2.y

    def solve2equation2variable(self,a1,a2,b1,b2,c1,c2):
        x = float('inf')
        y = float('inf')
        if (a1*b2 - b1*a2) != 0:
            if (b1*c2 - b2*c1) == 0:
                
                x = 0
            elif (a2*c1 - c2*a1) == 0:
                y = 0
            else:
                x = (b1*c2 - b2*c1)/(a1*b2 - a2*b1)
                y = (a2*c1 - c2*a1)/(a1*b2 - a2*b1)
        return x,y
    
    # Barycentric method to determine if point is within the triangle
    def point_within_triangle_barycentric(self):

        # Define some local variables for easy computation
        v0 = self.compute_vector(self.triangle[0], self.triangle[2])   # (C - A)
        v1 = self.compute_vector(self.triangle[0], self.triangle[1])   # (B - A)
        v2 = self.compute_vector(self.triangle[0], self.point)   # (P - A)

        a1 = v1.x
        a2 = v1.y
        b1 = v0.x
        b2 = v0.y
        c1 = -1 * v2.x
        c2 = -1 * v2.y

        print('Value of a1 is {}, a2 is {}, b1 is {}, b2 is {}, c1 is {}, c2 is {}'.format(a1,a2,b1,b2,c1,c2))
        self.u, self.v = self.solve2equation2variable(a1,a2,b1,b2,c1,c2)
        print('u is {} and v is {}'.format(self.u,self.v))

        if (self.u < 0 or self.v < 0 or self.u > 1 or self.v > 1 or (self.u + self.v) > 1):
            self.point_outside_triangle = 1
        elif (self.u < 1 and self.v ==0):
            self.point_on_triangle = 1
            self.intersecting_edge = [1,0]
        elif (self.v < 1 and self.u == 0):
            self.point_on_triangle = 1
            self.intersecting_edge = [2,0]
        elif (self.u < 1 and self.v < 1) and (self.u + self.v == 1):
            self.point_on_triangle = 1
            self.intersecting_edge = [2,1]
        elif (self.u == 0 and self.v == 0):
            self.point_on_triangle = 1
            self.intersecting_vertex = 0
        elif (self.v == 0 and self.u == 1):
            self.point_on_triangle = 1
            self.intersecting_vertex = 2
        elif (self.u == 1 and self.v == 0):
            self.point_on_triangle = 1
            self.intersecting_vertex = 1
        else:
            self.point_inside_triangle = 1
    
    def debug(self):
        # Printing the given point
        print('The given point is {} {}'.format(self.point.x, self.point.y))

        # Printing the given triangle points
        for i in range(3):
            print('The entered cordinates of the point {} in the triangle is {} {}'.format(i+1, self.triangle[i].x, self.triangle[i].y))

        print('Barycentric weights u = {} and v = {}'.format(self.u, self.v))

t = point_and_triangle()
t.get_input_point()
t.get_input_triangle()
t.point_within_triangle_barycentric()

if (t.point_outside_triangle):
    print('The given point lies outside the triangle')
elif (t.point_inside_triangle):
    print('The given point lies inside the triangle')
elif (t.point_on_triangle):
    a = t.intersecting_vertex
    if(a >= 0):
       print('The given point lies on the vertex {} of the triangle i.e on the point ({} {})'.format(a+1, t.triangle[a].x, t.triangle[a].y))
    
    b = t.intersecting_edge
    if(b[0]+b[1] != -10):
        print('The given point intersects the edge containing Point ({} {}) and Point ({} {}) of the triangle '.format(t.triangle[b[0]].x, t.triangle[b[0]].y, t.triangle[b[1]].x, t.triangle[b[1]].y))