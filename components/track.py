from hybrid.element import Element









class Track(Element):
    """Represents the <track> tag"""
    def __init__(self, default, kind, label, src, srclang):
        super().__init__('track', )
