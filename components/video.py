from hybrid.element import Element






class Video(Element):
    """Represents the <video> tag"""
    def __init__(self, autoplay, controls, height, loop, muted, poster, preload, src, width):
        super().__init__('video', )

