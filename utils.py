class Utils:
    @staticmethod
    def parse_testing_int_list(a_list):
        return list(map(lambda item: int(str(item).replace('[^\rd]', '')), a_list))
