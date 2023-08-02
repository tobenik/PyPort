class Security:
    def __init__(self, name: str):
        if not name:
            raise ValueError("security must have a name")

        self.name = str(name)
