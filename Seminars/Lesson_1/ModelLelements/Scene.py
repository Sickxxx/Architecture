from PoligonalModel import PoligonalModel
from Flash import Flash
from Camera import Camera


class Scene:
    def __init__(self, id: int, models: PoligonalModel, flashes: Flash, cameras: Camera):
        self.id = id
        self.models = models
        self.flashes = flashes
        self.cameras = cameras

    def method1(self, t: Flash):
        return t

    def method2(self, type1: Flash, type2: Camera):
        return type1
