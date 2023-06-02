from hybrid.element import Element



class Button(Element):
    """Represents the <button> tag"""

    def __init__(self, autofocus=None, disabled=None, form=None, formaction=None, name=None, type=None, value=None):
        super().__init__('button', autofocus=autofocus, disabled=disabled, form=form, formaction=formaction,
                         name=name, type=type, value=value)
        Element.all_elements.append(self.__dict__)
