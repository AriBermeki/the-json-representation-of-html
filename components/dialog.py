from hybrid.element import Element





class Dialog(Element):
    """Represents the <dialog> tag"""
    def __init__(self, open=None):
        super().__init__('dialog', open=open)
