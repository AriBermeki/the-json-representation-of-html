from hybrid.element import Element



class TH(Element):
    """Represents the <th> tag"""
    def __init__(self, abbr, colspan, headers, rowspan, scope, sorted):
        super().__init__('th', )