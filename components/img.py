from hybrid.element import Element

class Img(Element):
    """Represents the <img> tag"""
    def __init__(self,alt, height, src, width):
        super().__init__('img', alt, height, src, width)



