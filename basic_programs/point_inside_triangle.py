# Point class to store the x and y values of the coordinates
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

# Man class to check if the point intersects the triangle
class point_within_triangle:

    # Initiaization function
    def __init__(self):
        self.triangle = []
        self.intersecting_edge = 0
        print('Python program to test if a Point is within a triangle')

    # Get the Point data as input data from the user
    def get_input_point(self):
        x,y = map(float,input('Enter the x and y cordinates of the Point P to be tested  ').split())
        self.point = Point(x,y)
    
    # Get the trinagle coordinates as input data from the user
    def get_input_triangle(self):
        for i in range(3):
            x,y = map(float,input('Enter the x and y cordinates of the Point {} of the triangle  '.format(i+1)).split())
            self.triangle.append(Point(x,y))

    # Compute a vector from the given points
    def compute_vector(self, point1, point2):
        return Point(point2.x - point1.x, point2.y - point1.y)
    
    # Function to compute the cross product between 2 vectors in 2D
    def cross_product(self, point1, point2):
        return point1.x * point2.y - point1.y * point2.x

    # Function to check if point exists within or intersects the triangle
    def compute_cross_product(self):
        positive = 0
        negative = 0
        zeros = 0
        for i in range(3):
            temp = self.cross_product(self.compute_vector(self.point, self.triangle[i]), self.compute_vector(self.point, self.triangle[(i+1) % 3]))
            if(temp > 0):
                positive = positive + 1
            elif(temp < 0):
                negative = negative + 1
            else:
                zeros = zeros + 1
                self.intersecting_edge = i

        if(positive == 3 or negative == 3 or zeros == 3):
            self.point_within_triangle = True
            self.point_intersects_triangle = False
        elif((positive + zeros) == 3 or (negative + zeros) == 3):
            self.point_within_triangle = False
            self.point_intersects_triangle = True
        else:
            self.point_intersects_triangle = False
            self.point_within_triangle = False
    
    def debug(self):
        # Printing the given point
        print('The given point is {} {}'.format(self.point.x, self.point.y))

        # Printing the given triangle points
        for i in range(3):
            print('The entered cordinates of the point {} in the triangle is {} {}'.format(i+1, self.triangle[i].x, self.triangle[i].y))



