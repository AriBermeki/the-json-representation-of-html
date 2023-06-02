from hybrid.element import Element






class Meta(Element):
    """Represents the <meta> tag"""
    def __init__(
            self, 
            charset, 
            content, 
            http_equiv, 
            name
        ): #http-equiv
        super().__init__('meta', )