from flet import *

from utils.customs import CustomInputField


def main(page: Page):
    def set_error_text(e, message):
        text.input_box_content.error_text = message
        text.input_box_content.update()
        e.page.update()

    text = CustomInputField(False, "TestText")
    button = ElevatedButton("Click")
    button.on_click = lambda e: set_error_text(e, "ERERERE")
    button.expand = True

    page.add(text, button)


if __name__ == '__main__':
    app(target=main)
