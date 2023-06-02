from hybrid.element import Element

class Embed(Element):
    """Represents the <embed> tag"""

    def __init__(
        self,
        height=None,
        src=None,
        type=None,
        width=None
    ):
        super().__init__('embed', height=height, src=src, type=type, width=width)

