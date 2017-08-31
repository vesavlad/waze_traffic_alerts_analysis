import csv

with open("waze_jams_big_data.csv", "r", encoding="utf8") as f:

	reader = csv.reader(f)
	
	## If header exists then skip it
	next(reader, None)

	## If tasks (rows) are present after the header then keep a track of task_ids
	for row in reader:
		print(row[8])