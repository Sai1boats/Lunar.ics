# Lunar.ics
农历/阴历生日.ics文件生成器

## 0. 背景
之前所用的小米手机可以创建生日日程，生日日程可选择阴历生日还是阳历生日。后面换成Apple全家桶发现没有这个功能，同时小米已经创建的日程还无法导出。所以为了解决家里人阴历生日日程手动创建复杂的问题，故写了这个生成器
## 1.实现思路
- 首先感谢[200 年农历数据对照表](https://github.com/neten/Calendar--Lunar)提供的对应文档，简单暴力。*calendar1.csv*就是原始数据。本项目使用了[*ics*](https://pypi.org/project/ics/)这个模块
- 通过*process_time_format.py*将农历格式简化成不带年份的情况，同时将**闰月**标注了出来。生成的文件为*calendar_edited.csv*
- 通过*get_gregorian_time.py*将农历对应的阳历生日遍历出来
- 最后在*main.py*中调用*add_event.py*，生成ics文件
## 2.使用方法
将项目clone到本地后，直接在终端输入**python3 main.py**即可，生成的文件在result文件夹中
