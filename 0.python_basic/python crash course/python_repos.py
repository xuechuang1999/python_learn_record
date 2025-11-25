import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
# from matplotlib import pyplot as plt


# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'
r = requests.get(url)
print("Status code:", r.status_code)    # 状态码为200表示成功

# 将API响应存储在一个变量中
response_dict = r.json()
print("Total respositories:", response_dict['total_count'])

# 处理结果
print(response_dict.keys())
# print(response_dict.values())

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# 研究第一个仓库
# repo_dict = repo_dicts[0]
# print("\n Keys: ", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key, ":", repo_dict[key])

# name, stars = [], []
name, plot_dicts = [], []
for repo_dict in repo_dicts:
    name.append(repo_dict['name'])
    # stars.append(repo_dict['stargazers_count'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'] or 'No description provided',
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)


# 可视化
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.barh(name, stars, color='blue')
# ax.set_title('Most-Starred Python Projects on GitHub')
# ax.set_xlabel('Stars')
# ax.set_ylabel('Repository Name')
# plt.tight_layout()
# plt.show()


my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(style=my_style, config=my_config)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = name

# chart.add('', stars)
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')