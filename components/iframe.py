from hybrid.element import Element




class Iframe(Element):
    """Represents the <iframe> tag"""
    def __init__(self, allowfullscreen, height, src, width):
        super().__init__('iframe',allowfullscreen, height, src, width)

