import json
from pyecharts import Geo
import csv

city_name = []
with open('maoyan.csv',encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        city_name.append(row[3])

city_name.remove('所在城市')
city_name_list = list(set(city_name))
city_name_list.remove('')
city_name_dict = {city_name_list[i]:0 for i in range(len(city_name_list))}
for i in range(len(city_name_list)):
    city_name_dict[city_name_list[i]] = city_name.count(city_name_list[i])
city_name_dict = sorted(city_name_dict.items(),key=lambda k:k[1],reverse=True)
print(city_name_dict)

geo = Geo(
        '粉丝位置分布', '温家奇采集',
        title_color='#fff',
        title_pos='center',
        width=1200,
        height=600,
        background_color='#404a59'
)
attr, value = geo.cast(city_name_dict)
geo.add('', attr, value, visual_range=[0, 530],
        visual_text_color='#fff', symbol_size=15,
        is_visualmap=True, is_piecewise=True, visual_split_number=10)
geo.render('.\picture\粉丝位置分布-地理坐标图.html')