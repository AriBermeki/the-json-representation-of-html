from hybrid.element import Element







class Input(Element):
    """Represents the <input> tag"""
    def __init__(
            self,  
            accept, 
            autocomplete,
            autofocus,  
            checked, 
            disabled, 
            form, 
            list, 
            max, 
            maxlength,
            min, 
            multiple, 
            name, 
            pattern, 
            placeholder, 
            readonly, 
            required, 
            size, 
            step, 
            type, 
            value
            ):
        super().__init__(
            'input', 
            accept, 
            autocomplete,
            autofocus,  
            checked, 
            disabled, 
            form, 
            list, 
            max, 
            maxlength,
            min, 
            multiple, 
            name, 
            pattern, 
            placeholder, 
            readonly, 
            required, 
            size, 
            step, 
            type, 
            value
            )