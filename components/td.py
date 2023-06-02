from hybrid.element import Element


class Td(Element):
    """Represents the <td> tag"""
    def __init__(self, colspan, headers, rowspan):
        super().__init__('td', )