from hybrid.element import Element








class Script(Element):
    """Represents the <script> tag"""
    def __init__(self, async_, charset, defer, src, type):#async
        super().__init__('script', )