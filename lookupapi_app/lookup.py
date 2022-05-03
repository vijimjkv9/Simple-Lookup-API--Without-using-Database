
class Common(object):
    """
     assigning fields to the values
    """
    def __init__(self, **kwargs):
        for field in ('id', 'name'):
            setattr(self, field, kwargs.get(field, None))


departments = {
    1: Common(id=1, name='IT'),
    2: Common(id=2, name='HR'),
    3: Common(id=3, name='Finance'),
    4: Common(id=4, name='Administration'),
}
