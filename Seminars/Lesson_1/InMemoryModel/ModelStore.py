from Seminars.Lesson_1.ModelLelements import Camera, Scene, Flash, PoligonalModel


class ModelStore:

    def __init__(self, models: PoligonalModel.PoligonalModel(), scenes: Scene.Scene(), flashes: Flash.Flash(),
                 cameras: Camera.Camera()):
        self.models = models
        self.scenes = scenes
        self.flashes = flashes
        self.cameras = cameras

    def NotifyChange(self):
        pass

    def GetScene(self, id: int):
        pass
