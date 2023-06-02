from hybrid.element import Element


class Form(Element):
    """Represents the <form> tag"""
    def __init__(
            self,
            action, 
            autocomplete, 
            enctype, 
            method,
            name, 
            novalidate, 
            target 
        ):
        super().__init__(
            'form', 
            action, 
            autocomplete, 
            enctype, 
            method,
            name, 
            novalidate, 
            target 
            )