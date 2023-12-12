import csv

# 读取CSV文件
with open('calendar1.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

# 处理数据
for row in rows:
    if row[0][5] != '1' or (row[0][5] == '1' and row[0][6] == '/'):
        row[0] = row[0].replace('/', '/0', 1)
        if row[0][-2] == '/':
            row[0] = row[0][0:8] + '0' + row[0][-1]
    if row[1][5] != '1' or (row[1][5] == '1' and row[1][6] == '/'):
        row[1] = row[1].replace('/', '/0', 1)
    if row[1][-2] == '/':
        row[1] = row[1][0:8] + '0' + row[1][-1]
    row[1] = row[1][5:]

# 保存结果
for i in range(len(rows)):
    if (rows[i][1][-2:] == '28' and rows[i+1][1][-2:] == '01'and rows[i][1][0:2] == rows[i + 1][1][0:2]) or (
            rows[i][1][-2:] == '29' and rows[i+1][1][-2:] == '01' and rows[i][1][0:2] == rows[i + 1][1][0:2]) or (
            rows[i][1][-2:] == '30' and rows[i+1][1][-2:] == '01' and rows[i][1][0:2] == rows[i + 1][1][0:2]) :
        rows[i + 1][1] = '闰' + rows[i + 1][1]
    if rows[i][1][0:1] == '闰' and rows[i][1][1:3] == rows[i+1][1][0:2]:
        rows[i + 1][1] = '闰' + rows[i + 1][1]
with open('calendar_edited.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
