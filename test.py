import flet as ft


def main(page: ft.Page):
    page.title = "Flet Brush"
    page.scroll = ft.ScrollMode.ALWAYS

    card = ft.Card(
        col={"sm": 6, "md": 4},
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.ALBUM),
                        title=ft.Text("The Enchanted Nightingale"),
                        subtitle=ft.Text(
                            "Music by Julie Gable. Lyrics by Sidney Stein."
                        ),
                    ),
                    ft.Row(
                        [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
    )
    column = ft.ResponsiveRow(run_spacing=20)
    for i in range(10):
        column.controls.append(card)

    text_field = ft.TextField()

    page.add(column, text_field, ft.OutlinedButton(icon=ft.icons.ADD))
    page.update()


ft.app(main)
