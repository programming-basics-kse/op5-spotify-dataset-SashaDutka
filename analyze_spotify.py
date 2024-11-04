import csv
# lines = []

# with open('top_50_2023.csv', 'r') as file:
#     colums = next(file)
#     print(colums)
#     for line in file:
#         line = line[:-1].split(',')
#         lines.append(line)
#     print(lines)
# ARTIST_NAME = 0
# for line in lines:
#     print(line[ARTIST_NAME])
# rows = []
# with open('top_50_2023.csv', 'r') as file:
#     csv_reader = csv.reader(file, delimiter=',')
#     header = next(csv_reader)
#     for row in csv_reader:
#         rows.append(row)
#     # print(rows[0])
#
#
# dansebility = header.index('dansebility')
# sum_dance = 0
# for row in rows:
#     sum_dance += float(row[dansebility])
#
# print(sum_dance / len(rows))




import csv
import ast
rows = []
with open('top_50_2023.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    header = next(csv_reader)
    for row in csv_reader:
        rows.append(row)

danceability = header.index('danceability')

# def is_float(value):
#     try:
#         float(value)
#         return True
#     except ValueError:
#         return False
#
# sum_dance = 0
# counter = 0
# for row in rows:
#     if is_float(row[danceability]):
#         sum_dance += float(row[danceability])
#         counter +=1
# print(sum_dance / counter)





# print(is_float('12.3'))
print(rows)
for row in rows:
    row[4] = ast.literal_eval(row[4])
print(rows)

GENRES = 4
genres_dict = {}
for row in rows:
    for genre in row[GENRES]:
        if genre in genres_dict:
            genres_dict[genre] += 1
        else:
            genres_dict[genre] = 1

# x = (key, value)
top_three = sorted(genres_dict.items(), key = lambda x: x[1], reverse=True)
print(top_three)

def sum_1(a, b):
    return a + b

sum_2 = lambda x, y: x + y
print(sum_2(1, 4))










