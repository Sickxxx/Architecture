from Seminars.Lesson_1.Stuff import Point3D, Angle3D, Color


class Camera:
    def __init__(self, location: Point3D.Point3D(), angle: Angle3D.Angle3D()):
        self.location = location
        self.angle = angle

    def rotate(self, angle):
        pass

    def move(self, location):
        pass
