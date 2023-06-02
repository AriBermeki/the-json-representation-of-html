from hybrid.element import Element


class Base(Element):
    """Represents the <base> tag"""
    def __init__(self, href, target):
        super().__init__('base', href=href, target=target)
