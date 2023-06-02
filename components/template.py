from hybrid.element import Element



class Template(Element):
    """Represents the <template> tag"""
    def __init__(self, accesskey ,class_ ,contenteditable ,contextmenu ,dir_ ,draggable ,dropzone ,hidden ,id ,lang ,spellcheck ,style ,tabindex ,title ,translate):
        super().__init__('template', accesskey ,class_ ,contenteditable ,contextmenu ,dir_ ,draggable ,dropzone ,hidden ,id ,lang ,spellcheck ,style ,tabindex ,title ,translate)
