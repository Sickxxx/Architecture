import Poligon, Texture


class PoligonalModel:
    poligons = []
    textures = []

    def __init__(self, poligon: Poligon, texture: Texture):
        self.poligons.append(poligon.points)
        self.textures.append(texture)
