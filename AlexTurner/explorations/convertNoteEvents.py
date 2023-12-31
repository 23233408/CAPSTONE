# https://github.com/Sapphirine/real-time-sepsis-prediction/blob/master/convertNoteEvents.py

import csv
import pandas as pd
with open('NOTEEVENTS.csv') as f, open('updated-NOTEEVENTS.txt', 'w+') as f1:
	i = 0
	for line in csv.reader(f, quotechar='"', delimiter=',',
                     quoting=csv.QUOTE_ALL, skipinitialspace=True):
		hadm_id = line[2]
		chart_time = line[4]
		category = line[6]
		text = line[10].replace('\n', ' ').replace('"', '').replace(',', '')
		line_to_write = hadm_id + "," + chart_time + "," + category + "," + '"' + text + '"\n'
		f1.write(line_to_write)
		i = i+1
		print(i)

# create new updated file
# load this into pandas via terminal
# save into a df