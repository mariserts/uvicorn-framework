class DatabaseEngine:

    __engine = None
    __session = None

    def __init__(self, settings, *args, **kwargs):
        self.settings = settings
        self.args = args
        self.kwargs = kwargs
        self.setup()

    @property
    def engine(self):
        raise NotImplemented()

    @property
    def session(self):
        raise NotImplemented()

    def setup(self):
        pass
