from hybrid.element import Element


class Source(Element):
    """Represents the <source> tag"""
    def __init__(self,media, sizes, src, srcset, type ):
        super().__init__('source', )
