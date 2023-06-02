from hybrid.element import Element


class TextArea(Element):
    """Represents the <textarea> tag"""
    def __init__(self, autocomplete, autofocus, cols, disabled, form, maxlength, name, placeholder, readonly, required, rows, wrap):
        super().__init__('textarea', )
