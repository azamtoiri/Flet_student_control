import flet.canvas as cv
from flet import *

from utils.customs import STAppBar


class State:
    x: float
    y: float


state = State()


class STProfileView(View):
    def __init__(self):
        super().__init__()
        self.route = '/student/profile'
        self.appbar = STAppBar()

        # canvas for drawing
        self.cp = cv.Canvas(
            [
                cv.Fill(
                    Paint(
                        gradient=PaintLinearGradient(
                            (0, 0), (600, 600), colors=[colors.CYAN, colors.CYAN_100]
                        )
                    )
                ),
            ],
            content=GestureDetector(
                on_pan_start=self.pan_start,
                on_pan_update=self.pan_update,
                drag_interval=10,
            ),
            expand=False,
        )

        self.controls = [
            Container(Stack([self.cp]), expand=True),
            Text("Profile Page")
        ]

    @staticmethod
    def pan_start(e: DragStartEvent):
        state.x = e.local_x
        state.y = e.local_y

    def pan_update(self, e: DragUpdateEvent):
        self.cp.shapes.append(
            cv.Line(
                state.x, state.y, e.local_x, e.local_y,
                paint=Paint(stroke_width=3)
            )
        )
        self.cp.update()
        state.x = e.local_x
        state.y = e.local_y
