from hybrid.element import Element




class Picture(Element):
    """Represents the <picture> tag"""
    def __init__(self,accesskey,alt,contenteditable,crossorigin,dir,height,hidden,id,ismap,lang,loading,sizes,spellcheck,src,srcset,style,tabindex,title,translate,usemap,width):
        super().__init__('picture', )
