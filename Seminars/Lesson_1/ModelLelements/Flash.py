from Seminars.Lesson_1.Stuff import Point3D, Angle3D, Color


class Flash:
    def __init__(self, location: Point3D.Point3D(), angle: Angle3D.Angle3D(), color: Color.Color(), power: float):
        self.location = location
        self.angle = angle
        self.color = color
        self.power = power

    def rotate(self, angle):
        pass

    def move(self, location):
        pass
