from hybrid.element import Element





class Link(Element):
    """Represents the <link> tag"""
    def __init__(
            self, 
            href, 
            hreflang, 
            media, 
            rel, 
            sizes, 
            type
        ):
        super().__init__('link', )