import xlsxwriter

# put data to lists a and b
with open('mobile games.csv', 'r') as file:
    lines = file.readlines()

a = []
b = []

for i in range(1, len(lines)):
    x1, y1 = lines[i].split(sep=";")
    a.append(x1)
    b.append(float(y1))


# put sorted a into a1 and b into b1
a1 = []
b1 = []

# seeking for maximum
for i in range(len(a)):
    m = b.index(max(b))
    a1.append(a[m])
    b1.append(b[m])
    b[m] = 0

workbook = xlsxwriter.Workbook('mobile_games_sorted.xlsx')
worksheet = workbook.add_worksheet()
x1, y1 = lines[0].split(sep=";")
worksheet.write(0, 0, x1)
worksheet.write(0, 1, y1)
for i in range(len(a1)):
    worksheet.write(i+1, 0, a1[i])
    worksheet.write(i+1, 1, b1[i])
workbook.close()