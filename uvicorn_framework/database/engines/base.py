class DatabaseEngine:

    def __init__(self, settings, *args, **kwargs):
        self.settings = settings
        self.args = args
        self.kwargs = kwargs
        self.setup()

    @property
    def engine(self):
        return None

    @property
    def cursor(self):
        return None

    def setup(self):
        pass
