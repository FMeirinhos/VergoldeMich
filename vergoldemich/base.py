class Parameters(object):

    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)


class MetaBase(object):

    def __init__(self):
        self.p = Parameters(**self.params)
