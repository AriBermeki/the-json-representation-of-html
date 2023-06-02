from hybrid.element import Element

class Bdi(Element):
    """Represents the <bdi> tag"""
    def __init__(self, accesskey, class_attr, contenteditable, dir_attr, hidden, id_attr, lang, style, tabindex, title, translate):
        super().__init__(
            'bdi', accesskey=accesskey,
            class_attr=class_attr,
            contenteditable=contenteditable,
            dir_attr=dir_attr,
            hidden=hidden,
            id_attr=id_attr,
            lang=lang,
            style=style,
            tabindex=tabindex,
            title=title,
            translate=translate)
