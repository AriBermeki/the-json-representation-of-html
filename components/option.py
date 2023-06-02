from hybrid.element import Element


    

class Option(Element):
    """Represents the <option> tag"""
    def __init__(self,    disabled, label, selected, value):
        super().__init__('option', )
