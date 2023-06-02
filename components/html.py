from hybrid.element import Element


class Html(Element):
    """Represents the <html> tag"""
    def __init__(self, content=None, **kwargs):
        super().__init__('html', content=content, **kwargs)

class Head(Element):
    """Represents the <head> tag"""
    def __init__(self, content=None, **kwargs):
        super().__init__('head', content=content, **kwargs)

class Body(Element):
    """Represents the <body> tag"""
    def __init__(self, content=None, **kwargs):
        super().__init__('body', content=content, **kwargs)

class Article(Element):
    """Represents the <article> tag"""
    def __init__(self, content=None, **kwargs):
        super().__init__('article', content=content, **kwargs)

class Section(Element):
    """Represents the <section> tag"""
    def __init__(self, content=None, **kwargs):
        super().__init__('section', content=content, **kwargs)

class Nav(Element):
    """Represents the <nav> tag"""
    def __init__(self, content=None, **kwargs):
        super().__init__('nav', content=content, **kwargs)

class Header(Element):
    """Represents the <header> tag"""
    def __init__(self, content=None, **kwargs):
        super().__init__('header', content=content, **kwargs)

class Footer(Element):
    """Represents the <footer> tag"""
    def __init__(self, content=None, **kwargs):
        super().__init__('footer', content=content, **kwargs)


