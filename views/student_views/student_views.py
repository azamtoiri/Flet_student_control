from flet import *

from utils.constants import RIGHT_COL_COLOR
from utils.customs import CustomContainer

from views.student_views.student_application import StudentView


class StudentHomeView(StudentView):
    """Окна студента которые будут отображаться при переключении в navbar"""
    def __init__(self):
        super().__init__()
        self.route = '/student/home'

        con_content = Column(
            alignment=MainAxisAlignment.CENTER, controls=
            [
                TextField(expand=True),
                Text('Home page', size=80),
                ElevatedButton("123")
            ]
        )

        # Container of right Main page
        self.con_ = CustomContainer()  # Container of
        self.con_.content = con_content
        self.con_.expand = True
        self.con_.bgcolor = RIGHT_COL_COLOR

        self.controls.append(self.con_)


class StudentStudentsView(StudentView):
    """Окна студента которые будут отображаться при переключении в navbar"""
    def __init__(self):
        super().__init__()
        self.route = '/students'

        con_content = Column(
            alignment=MainAxisAlignment.CENTER, controls=
            [
                TextField(expand=True),
                Text('Students', size=80, text_align=TextAlign.CENTER),
                ElevatedButton("123")
            ]
        )

        # Container of right Main page
        self.con_ = CustomContainer()  # Container of
        self.con_.content = con_content
        self.con_.expand = True
        self.con_.bgcolor = RIGHT_COL_COLOR

        self.controls.append(self.con_)


class StudentCoursesView(StudentView):
    """Окна студента которые будут отображаться при переключении в navbar"""
    def __init__(self):
        super().__init__()
        self.route = '/student/courses'

        con_content = Column(
            alignment=MainAxisAlignment.CENTER, controls=
            [
                TextField(expand=True),
                Text('Main student page', size=80),
                ElevatedButton("123", expand=True)
            ]
        )

        # Container of right Main page
        self.con_ = CustomContainer()  # Container of
        self.con_.content = con_content
        self.con_.expand = True
        self.con_.bgcolor = RIGHT_COL_COLOR

        self.controls.append(self.con_)


class StudentMaterialsView(StudentView):
    """Окна студента которые будут отображаться при переключении в navbar"""
    def __init__(self):
        super().__init__()
        self.route = '/student/material'

        con_content = Column(
            alignment=MainAxisAlignment.CENTER, controls=
            [
                TextField(expand=True),
                Text('Main student page', size=80),
                ElevatedButton("123", expand=True)
            ]
        )

        # Container of right Main page
        self.con_ = CustomContainer()  # Container of
        self.con_.content = con_content
        self.con_.expand = True
        self.con_.bgcolor = RIGHT_COL_COLOR

        self.controls.append(self.con_)