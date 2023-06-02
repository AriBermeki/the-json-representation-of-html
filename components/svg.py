from hybrid.element import Element





class Svg(Element):
    """Represents the <svg> tag"""
    def __init__(self, height, preserveAspectRatio, viewBox, width):
        super().__init__('svg', )