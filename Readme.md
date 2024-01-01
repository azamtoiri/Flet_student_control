# Student control
## Template construction docs
## Based on flet 

This branch is not tested

# !Routing
Routing on this structure will be carried out on main application

```python
class MainApp(BaseApp, ABC):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.page.client_storage.clear()
        self.page.client_storage.set('is_auth', False)

        # Views
        self.welcome_view = ApplicationView()

        # views which will be used
        self.views: Dict[str, View] = {
            self.welcome_view.route: self.welcome_view,
        }

        # All apps
        self.some_app = SomeAppp(self.page)

        # initialize our routes from other apps
        self.initialize_app_routes(self.some_app)

        # initialize handler
        self.handler = MainHandler(self)

        self.show_welcome_view()
```
### !!!definitely in the order shown

> Only desktop version of sites


# Docs
run script manage.py

```shell
python manage.py start app {application} # app name
```
___
Separated to applications
___
Each application has 2 folders `views` and `utils`

* `Views` - here we create our views which need 
* `Utils` - some utils which we need on this application, here with default we have `handler.py`
* `application.py` - on this file we will aerate our application 

Example of the `application.py` file

```python
from typing import Dict

from flet import Page, View

from application.views.application_view import ApplicationView
from application.utils.handler import Handler


class ApplicationApp:
    def __init__(self, page: Page):
        self.page = page

        # Views
        # sample:
        self.application_view = ApplicationView()
        # views which will be used
        self.views: Dict[str, View] = {
            # our views
            #sample:
            self.application_view.route: self.application_view
        }
        # initialize handler
        self.handler = Handler(self)

    # On this file will be our buttons properties
    
```
Example of the properties

```python
@property
def login_button(self) -> ElevatedButton:
    return self.application_view.button
```

All logic is will be on `handler.py`

```python
class Handler:
    def __init__(self, application: 'ApplicationApp') -> None:
        """Этот класс будет обрабатывать все события"""
        self.app = application

        self.app.login_button.on_click = lambda e: self.login_button_click(e)
    
    def login_button_click(self) -> None:
        """Some login logic"""
        pass
```

And finally Example of the ApplicationView
___
```python
from flet import View, Text


class ApplicationView(View):
    def __init__(self):
        super().__init__()
        # initialize route for this view
        self.route = '/student/courses'

        self.controls = [
            Text("Some controls here")
        ]

```

Global Utils well be on the root of the project on `utils` folder


For comfort was created file `run.py` which runs file main.py

```shell
python run.py
```

Or you can run as default 
```shell
flet run main.py
```