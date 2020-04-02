class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if Singleton.__instance is None:
            Singleton.__instance = super(Singleton, cls).__new__(cls)
        return Singleton.__instance