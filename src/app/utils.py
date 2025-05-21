def handleGetText(parent, tag, required= True, default = None):
    el = parent.find(tag)
    if el is not None and el.text:
        return el.text
    elif required:
        raise ValueError(f"El tag {tag} es requerido")
    else:
        return default
    
def handleSafeCast(value, to_type, default=None):
    try:
        return to_type(value)
    except (ValueError, TypeError):
        return default
    