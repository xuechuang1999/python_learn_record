import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style = my_style, x_label_rotation=45, show_legend=False)

chart.title = "Python Projects on GitHub"
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 16100, 'label': 'A command line HTTP client'},
    {'value': 15000, 'label': 'A high-level Python web framework'},
    {'value': 12000, 'label': 'A lightweight WSGI web application framework'}
]

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')