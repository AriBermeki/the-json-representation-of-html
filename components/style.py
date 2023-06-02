from hybrid.element import Element



class Style(Element):
    """Represents the <style> tag"""
    def __init__(self,media, nonce, title, type ):
        super().__init__('style', )
