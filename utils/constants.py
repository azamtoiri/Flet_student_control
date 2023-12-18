from pathlib import Path

from flet import colors

BASE_DIR = Path().parent

LOGO_PATH = '../assets/Fox_Hub_logo.png'
BLUE = '9caede'
LEFT_COL_COLOR = '#363740'
RIGHT_COL_COLOR = '#F7F8FC'
SHEET = '#9FA2B4'

SHEET_BG_COLOR = colors.with_opacity(0.1, color=SHEET)
DB_NAME_SQLITE = BASE_DIR / 'db.sqlite3'

DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "admin"

DB_HOST = "localhost"
DB_PORT = "5432"
DB_USER = "postgres"
DB_PASS = "1234"
DB_NAME = "postgres"


def DATABASE_URL_psycopg2():
    # DSN
    # postgresql+psycopg://postgres:postgres@localhost:5432/sa
    return f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
