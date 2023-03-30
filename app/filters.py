import babel

from app import app


@app.template_filter()
def format_datetime(value):
    format = 'dd.MM.y'
    date = babel.dates.format_datetime(value, format)
    return date
