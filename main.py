def hello(name="GitHub Actions"):
    if not isinstance(name,str):
        raise TypeError("Le nomdoit êtreune chaîne")
    return f"Hello, name!"
