from jinja2 import Environment, PackageLoader, select_autoescape

loader = Environment(
    loader=PackageLoader('renderer', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)
