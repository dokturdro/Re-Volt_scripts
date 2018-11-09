import csv
import operator

scoreindex = {'01': 10, '02': 8, '03': 7, '04': 6, '05': 5, '06': 4, '07': 3,
              '08': 2, '09': 1, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0,
              '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0}
scoretotal = {}
scoretable = {}

# Get path to .csv file by shift + right click on .csv file and select 'Copy as path'
# Remember to keep the format as r"<path>" to avoid errors
# Paste path to .csv file here
with open(r"C:\Users\Administrator\Downloads\session_2018-05-17_21-00-50.csv", mode='r') as infile:
    reader = csv.reader(infile)
    for rows in reader:
        if rows[0].isdigit():
            if rows[1] not in scoretotal:
                scoretotal[rows[1]] = scoreindex[rows[0]]
                scoretable[rows[1]] = []
                scoretable[rows[1]].append(rows[0])
            else:
                scoretotal[rows[1]] += scoreindex[rows[0]]
                scoretable[rows[1]].append(rows[0])




finalscore = sorted(scoretotal.items(), key=operator.itemgetter(1), reverse = True)

for item in finalscore:
    print(item[1], item[0].ljust(12), "[", *(sorted(scoretable[item[0]])), "]")
