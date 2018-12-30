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


class ParsingRightsAnswer(object):

    @staticmethod
    def prepare_rights_answer(data):

        assert isinstance(data, list)

        rights = data[0]

        return RightsSpec(
            confirmed=bool(rights[1]),
            allow_read=bool(rights[2]),
            allow_write=bool(rights[3]),
            allow_partial_edit=bool(rights[4]),
            allow_edit=bool(rights[5]),
            allow_print=bool(rights[6]),
            allow_manage=bool(rights[7]),
            blocked=bool(rights[8])
        )