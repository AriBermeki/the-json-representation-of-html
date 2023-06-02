from hybrid.element import Element

class Head(Element):
    """Represents the <head> tag"""
    def __init__(self, class_,id,lang,style,title,translate):
        super().__init__('head', class_,id,lang,style,title,translate)
