
from hybrid.element import Element





class Audio(Element):
    """Represents the <audio> tag"""
    def __init__(self,accesskey, autoplay, className, contenteditable, controls, crossorigin, dir, hidden, id, lang, loop, muted, preload, src, style, tabindex, title, translate):
        super().__init__(
            'audio',accesskey=accesskey, 
            autoplay=autoplay, className=className, contenteditable=contenteditable, 
            controls=controls, crossorigin=crossorigin, dir=dir, hidden=hidden, id=id,
            lang=lang, loop=loop, muted=muted, preload=preload, src=src, style=style, 
            tabindex=tabindex, title=title, translate=translate)

