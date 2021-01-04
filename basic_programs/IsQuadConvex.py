class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Quad:

    def __init__(self):
        self.quad = []
        self.isConvex = 0
    
    def dot(self, vector1, vector2):
        return vector1.x * vector1.x + vector1.y * vector2.y
    
    def cross(self, vector1, vector2):
        return vector1.x * vector2.y - vector1.y * vector2.x
    
    def vector(self, point1, point2):
        return Point(point2.x - point1.x, point2.y - point1.y)

    def getQuadData(self):
        print('\nEnter the data for the quadrilateral in a cyclic order \n')
        for i in range(4):
            x,y = map(float,input('Enter the x and y cordinate of the Point {} of the quadrilateral  '.format(i+1)).split())
            self.quad.append(Point(x,y))
    
    def quadConvexity(self):
        bd = self.vector(self.quad[1], self.quad[3])   # BD vector
        ba = self.vector(self.quad[1], self.quad[0])   # BA vector
        bc = self.vector(self.quad[1], self.quad[2])   # BC vector

        ac = self.vector(self.quad[0], self.quad[2])   # AC vector
        ad = self.vector(self.quad[0], self.quad[3])   # AD vector
        ab = self.vector(self.quad[0], self.quad[1])   # AB vector
        

        normal1 = self.cross(bd,ba) * self.cross(bd,bc)
        normal2 = self.cross(ac,ad) * self.cross(ac,ab)

        if(normal1 < 0 and normal2 < 0):
            self.isConvex = 1