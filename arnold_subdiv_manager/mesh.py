import attr


@attr.s(frozen=True)
class Mesh(object):
    name = attr.ib(type=str)
