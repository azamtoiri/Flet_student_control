# Вход
После входа выводить в snackbar что пользователь успешно авторизовался
```python
class SuccessSnackBar(ft.SnackBar):
    def __init__(self, message: str) -> None:
        super().__init__(content=ft.Row())
        self.bgcolor = ft.colors.GREEN

        self.message = ft.Text()
        self.message.value = message
        self.message.text_align = ft.TextAlign.CENTER
        self.message.color = ft.colors.WHITE
        self.message.size = 20
        self.message.expand = True

        self.content.controls.append(self.message)
```

Пример `warining banner`[https://flet-controls-gallery.fly.dev/dialogs/banner]
```python
class WarningBanner(ft.Banner):
    def __init__(self, page: ft.Page, message: str) -> None:
        super().__init__()
        self.page = page
        self.bgcolor = ft.colors.RED

        self.message = ft.Text()
        self.message.value = message
        self.message.text_align = ft.TextAlign.CENTER
        self.message.color = ft.colors.WHITE
        self.message.expand = True

        self.leading = ft.Icon()
        self.leading.name = ft.icons.DANGEROUS
        self.leading.color = ft.colors.WHITE

        self.close_button = ft.IconButton()
        self.close_button.icon = ft.icons.CLOSE
        self.close_button.icon_color = ft.colors.WHITE
        self.close_button.on_click = lambda e: self.close()
        self.actions.append(self.close_button)

        self.content = ft.Row()
        self.content.controls.append(self.message)

    def close(self) -> None:
        self.page.banner.open = False
        self.page.update()
```
# Перестройка класса
Использовать функции для каждого класса

Почистить код

Можно использовать функцию `append` вместо того чтобы вызывать целый класс и прописывать ее внутри
так выглядит более понятливое и более лаконично пример ниже:
```python
class ApplicationAppBar(ft.AppBar):
    def __init__(self) -> None:
        super().__init__()

        self.title = ft.Text()
        self.title.value = 'Flet Alchemy'
        self.leading = self.title

        self.logout_button = ft.IconButton()
        self.logout_button.icon = ft.icons.LOGOUT
        self.logout_button.tooltip = 'Logout'
        self.actions.append(self.logout_button)
```


# Handler (обработчик событий)

Добавить класс обработчик событий который будет обрабатывать:
* вход
* выход
* регистрацию и тд

### Нужно добавить такие функции похожие на это с `@property`
```python
# сама Функция которая возвращает объект `register_button`
class Application:
    def __init__(self):
        self.register_view = RegisterView()
    
    @property
    def register_button(self) -> ft.OutlinedButton:
        return self.register_view.register_button

# потом ее можно использовать в другом классе таким образом
class Handler:
    def __init__(self, application: 'Application') -> None:
        self.application = application

        self.database = DataBase(constants.DB_NAME)
        self.user: Optional[User] = None

        # ok, lets configure widgets events.
        self.application.register_button.on_click = (
            lambda e: self.register_click()
        )
```

# Keyboard enters

Добавить поддержку нажатий клавиш на клавиатуре, 
таких как enter вход backspace назад и тп