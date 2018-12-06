from collections import namedtuple

RightsSpec = namedtuple("RightsSpec", "confirmed allow_read allow_write allow_partial_edit allow_edit allow_manage"
                                      " allow_print blocked")


class ParsingRights(object):

    @staticmethod
    def parsing_rigths(data):

        confirmed = False
        allow_read = data["allow_read"]
        allow_write = data["allow_write"]
        allow_partial_edit = data["allow_partial_edit"]
        allow_edit = data["allow_edit"]
        allow_manage = data["allow_manage"]
        allow_print = data["allow_print"]
        blocked = True

        return RightsSpec(
            confirmed=confirmed,
            allow_read=allow_read,
            allow_write=allow_write,
            allow_partial_edit=allow_partial_edit,
            allow_edit=allow_edit,
            allow_print=allow_print,
            allow_manage=allow_manage,
            blocked=blocked
        )