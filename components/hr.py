from hybrid.element import Element

class Hr(Element):
    """Represents the <hr> tag"""
    def __init__(self,class_,id,lang,style,title,translate):
        super().__init__('hr', class_,id,lang,style,title,translate)
