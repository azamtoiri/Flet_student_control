from flet import *

from utils.constants import LEFT_COL_COLOR, RIGHT_COL_COLOR, LOGO_PATH, SHEET

# from service.auth import load_token, get_name
# from utils.colors import BLUE
BLUE = '9caede'


class Student(Container):
    def __init__(self, page: Page):
        super().__init__()

        page.padding = 0
        self.expand = True
        # self.current_user_name = get_name(load_token())

        self.content = Row(
            spacing=0,
            controls=[
                # region: Left nav bar
                Container(
                    width=255,
                    bgcolor=LEFT_COL_COLOR,
                    padding=padding.only(top=20, left=10, right=10),
                    content=Column(
                        controls=[
                            # region: Top header container
                            Container(
                                padding=padding.only(left=15),
                                content=Row(
                                    controls=[
                                        Image(
                                            src=LOGO_PATH,
                                            height=50, width=50,
                                        ),
                                        Text(value="FoxHub", size=19, weight=FontWeight.BOLD)
                                    ]
                                )
                            ),
                            # endregion

                            Container(height=30),

                            # region: 1st page
                            Container(
                                width=255,
                                height=56,
                                bgcolor=colors.with_opacity(0.1, color=SHEET),
                                alignment=alignment.center,
                                padding=padding.only(left=10),
                                content=Row(
                                    controls=[
                                        Icon(
                                            name=icons.PIE_CHART,
                                            size=20,
                                        ),
                                        Text(value="Домашняя страница", size=12, weight=FontWeight.BOLD)
                                    ]
                                )
                            ),
                            # endregion

                            # region: 2nd page
                            Container(
                                width=255,
                                height=56,
                                # using bgcolor for active page
                                # bgcolor=colors.with_opacity(0.1, color=SHEET),
                                alignment=alignment.center,
                                padding=padding.only(left=10),
                                content=Row(
                                    controls=[
                                        Icon(
                                            name=icons.PIE_CHART,
                                            size=20,
                                        ),
                                        Text(value="Задания", size=12, weight=FontWeight.BOLD)
                                    ]
                                )
                            ),
                            # endregion

                            # region: 3rd page
                            Container(
                                width=255,
                                height=56,
                                # using bgcolor for active page
                                # bgcolor=colors.with_opacity(0.1, color=SHEET),
                                alignment=alignment.center,
                                padding=padding.only(left=10),
                                content=Row(
                                    controls=[
                                        Icon(
                                            name=icons.GRADE,
                                            size=20,
                                        ),
                                        Text(value="Оценки", size=12, weight=FontWeight.BOLD)
                                    ]
                                )
                            ),
                            # endregion

                            # region: 4th page
                            Container(
                                width=255,
                                height=56,
                                # using bgcolor for active page
                                # bgcolor=colors.with_opacity(0.1, color=SHEET),
                                alignment=alignment.center,
                                padding=padding.only(left=10),
                                content=Row(
                                    controls=[
                                        Icon(
                                            name=icons.GOLF_COURSE,
                                            size=20,
                                        ),
                                        Text(value="Курсы", size=12, weight=FontWeight.BOLD)
                                    ]
                                )
                            ),
                            # endregion

                            # region: 5nd page
                            Container(
                                width=255,
                                height=56,
                                # using bgcolor for active page
                                # bgcolor=colors.with_opacity(0.1, color=SHEET),
                                alignment=alignment.center,
                                padding=padding.only(left=10),
                                content=Row(
                                    controls=[
                                        Icon(
                                            name=icons.EXIT_TO_APP_ROUNDED,
                                            size=20,
                                        ),
                                        Text(value="Выйти", size=12, weight=FontWeight.BOLD)
                                    ]
                                )
                            ),
                            # endregion
                        ]
                    ),
                ),
                # endregion

                # region: Right Main Student page
                Container(
                    # width=1185,
                    expand=True,
                    bgcolor=RIGHT_COL_COLOR,
                    alignment=alignment.center,
                    padding=padding.only(left=50,),
                    content=Text(
                        value="Main student page",
                        size=100,
                    ),
                )
                # endregion
            ]
        )

        # self.content = Row(
        #     spacing=0,
        #     controls=[
        #         Container(
        #             width=200,
        #             bgcolor=BLUE,
        #             # using padding for correcting position of objects in container
        #             padding=padding.only(top=20, left=10, right=10),
        #             content=Column(
        #                 controls=[
        #                     Row(
        #                         spacing=10,
        #                         controls=[
        #                             Image(
        #                                 src=LOGO_PATH,
        #                                 height=50, width=50,
        #                             ),
        #                             Text(value="FoxHub", size=19, weight=FontWeight.BOLD)
        #                         ]
        #                     ),
        #
        #                     Container(height=30),
        #
        #                     Container(
        #                         height=40,
        #                         bgcolor=colors.with_opacity(0.1, color=colors.BLUE_300),
        #                         padding=padding.only(left=5, top=0, right=0, bottom=0),
        #                         content=Row(
        #                             vertical_alignment=CrossAxisAlignment.CENTER,
        #                             controls=[
        #                                 Icon(
        #                                     icons.PIE_CHART,
        #                                 ),
        #                                 Text(value='Домашняя страница', size=14, color='WHITE'),
        #                             ]
        #                         )
        #                     ),
        #
        #                     Divider(color='#9caede', height=0.5, thickness=0.5),
        #
        #                     Container(
        #                         content=Text(value='Utilities', size=14, color='WHITE')
        #                     ),
        #
        #                     Divider(color='#9caede', height=0.5, thickness=0.5),
        #
        #                     Row(
        #                         alignment=alignment.center,
        #                         controls=[
        #                             Container(
        #                                 alignment=alignment.center,
        #                                 height=35,
        #                                 width=35,
        #                                 bgcolor='9caede',
        #                                 border_radius=20,
        #                                 content=Icon(
        #                                     icons.ARROW_BACK_IOS,
        #                                     size=12,
        #                                 )
        #                             )
        #                         ]
        #                     )
        #                 ]
        #             )
        #         )
        #     ]
        # )
