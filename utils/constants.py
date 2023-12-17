from pathlib import Path
from flet import colors

BASE_DIR = Path().parent

LOGO_PATH = '../assets/Fox_Hub_logo.png'
BLUE = '9caede'
LEFT_COL_COLOR = '#363740'
RIGHT_COL_COLOR = '#F7F8FC'
SHEET = '#9FA2B4'

SHEET_BG_COLOR = colors.with_opacity(0.1, color=SHEET)
DB_NAME = BASE_DIR / 'db.sqlite3'

DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "admin"