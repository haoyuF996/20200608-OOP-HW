class point:

    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return (self.x**2 + self.y**2)**0.5

    def distanceFromPoint(self,point):
        return ((self.x - point.getX())**2+(self.y - point.getY())**2)**0.5

    def reflect_x(self):
        newPoint = point(self.x,-self.y)
        return newPoint
    def reflect_y(self):
        newPoint = point(-self.x,self.y)
        return newPoint

    def slope_from_origin(self):
        if self.x == 0:
            return None
        return self.y / self.x
    
    def get_line_to(self,p1):
        x1,x2,y1,y2 = self.x,p1.getX(),self.y,p1.getY()
        if x1-x2 == 0:
            return (x1,None)
        else:
            a = (y1-y2)/(x1-x2)
            b = y1-x1*a
        return (a,b)

    def move(self,dx,dy):
        newPoint = point(self.x+dx,self.y+dy)
        return newPoint

    def perpendicular_bisector(self,p1):
        mid = point((self.x+p1.getX())/2,(self.y+p1.getY())/2)
        if self.get_line_to(p1)[1] == None:
            return (0,mid.getY())
        elif self.get_line_to(p1)[0] != 0:
            slope = -1/self.get_line_to(p1)[0]
        else:
            return (mid.getX(),None)
        p2 = mid.move(1,slope)
        return mid.get_line_to(p2)

    def circle(self,p1,p2):
        a1,b1 = self.perpendicular_bisector(p1)
        a2,b2 = self.perpendicular_bisector(p2)
        if b1 == None:
            xc = a1
            yc = xc*a2 + b2
        elif b2 == None:
            xc = a2
            xc*a1 + b1
        else:
            xc = (b2-b1)/(a1-a2)
            yc = xc*a1 + b1
        center = point(xc,yc)
        radius = self.distanceFromPoint(center)
        return center,radius

p1 = point(1,-1)
p2 = point(-1,-1)
p3 = point(1,1)
c = p1.circle(p2,p3)[0]
print((c.getX(),c.getY()),p1.circle(p2,p3)[1])