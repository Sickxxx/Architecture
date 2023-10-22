from Seminars.Lesson_1.Stuff.Point3D import Point3D


class Poligon:
    points = []

    def __init__(self, point3d):
        self.point3d = point3d
        if isinstance(point3d, Point3D):
            self.points.append(point3d)
        else:
            raise ValueError("Обьект не является классом Point3D")
