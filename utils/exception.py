class RequiredField(Exception):
    def __init__(self, field: str):
        self.field = field
        super().__init__(f'Пожалуйста заполните поле, {self.field} поле является обязательным.')


class AlreadyRegistered(Exception):
    def __init__(self, field: str):
        self.field = field
        super().__init__(f'Извините, {self.field} уже занято.')


class NotRegistered(Exception):
    ...
