from jinja2 import Environment, PackageLoader, select_autoescape

loader = Environment(
    loader=PackageLoader('templater', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)
