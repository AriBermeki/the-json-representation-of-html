from hybrid.element import Element



class Div(Element):
    """Represents the <div> tag"""

    def __init__(
        self,
        accesskey=None,
        contenteditable=None,
        dir=None,
        hidden=None,
        id=None,
        lang=None,
        spellcheck=None,
        style=None,
        tabindex=None,
        title=None,
        translate=None
    ):
        super().__init__(
            'div',
            accesskey=accesskey,
            contenteditable=contenteditable,
            dir=dir,
            hidden=hidden,
            id=id,
            lang=lang,
            spellcheck=spellcheck,
            style=style,
            tabindex=tabindex,
            title=title,
            translate=translate
        )
