import random

import plotly.graph_objs as go
from flet import *

from service.auth import load_token, get_name
from utils.colors import BLUE


class Dashboard(Container):
    def __init__(self, page: Page):
        super().__init__()

        fig = self.get_fig()
        page.padding = 0
        self.expand = True
        self.current_user_name = get_name(load_token())

        self.content = Row(
            spacing=0,
            controls=[
                Container(
                    width=200,
                    bgcolor=BLUE,
                    # using padding for correcting position of objects in container
                    padding=padding.only(top=20, left=10, right=10),
                    content=Column(
                        controls=[
                            Row(
                                controls=[
                                    Icon(
                                        icons.PERSON,
                                        size=50,
                                    )
                                ]
                            ),

                            Divider(color='#9caede', height=0.5, thickness=0.5),

                            Container(
                                content=Text(value='Dashboard', size=14, color='WHITE')
                            ),

                            Divider(color='#9caede', height=0.5, thickness=0.5),

                            Container(
                                content=Text(value='Utilities', size=14, color='WHITE')
                            ),

                            Divider(color='#9caede', height=0.5, thickness=0.5),

                            Row(
                                alignment=alignment.center,
                                controls=[
                                    Container(
                                        alignment=alignment.center,
                                        height=35,
                                        width=35,
                                        bgcolor='9caede',
                                        border_radius=20,
                                        content=Icon(
                                            icons.ARROW_BACK_IOS,
                                            size=12,
                                        )
                                    )
                                ]
                            )
                        ]
                    )
                )
            ]
        )

    def get_fig(self):
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        spendings = [random.randint(100, 1000) for _ in range(len(months))]

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=months,
            y=spendings,
            mode='lines+markers',
            line=dict(shape='spline', width=5,
                      color='rgba(78, 115, 223, 0.5)'),
            fill='tozeroy',
            fillcolor="rgba(78, 115, 223, 0.3)",
            marker=dict(size=9, color='rgba(78, 115, 223, 1)',
                        line=dict(width=1, color='rgba(78, 115, 223, 1)')),
            hovertemplate="""<b>%{x}</b><br>
        <span>Spendings: %{y}</span>"""
        ))

        fig.update_xaxes(showgrid=False, gridwidth=0.1, gridcolor='LightPink')
        fig.update_layout(
            title='Monthly Expenses',
            xaxis_title='Month',
            yaxis_title='Spending ($)',
            showlegend=False,
            # plot_bgcolor='rgba(0,0,0,0)',
            # paper_bgcolor='rgba(0,0,0,0)',
            # grid=dict(type='dot')
        )
        return fig
