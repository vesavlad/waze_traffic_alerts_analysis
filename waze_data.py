import requests
import json
import csv
import time
import os	

## Start the clock
start_time = time.clock()

resp = requests.get("https://na-georss.waze.com/rtserver/web/TGeoRSS?tk=ccp_partner&ccp_partner_name=Providence&format=JSON&types=traffic,alerts,irregularities&polygon=-71.440487,41.866467;-71.374741,41.858029;-71.375427,41.828744;-71.395512,41.810450;-71.373367,41.785033;-71.405811,41.764486;-71.445465,41.786057;-71.446238,41.801095;-71.489410,41.817281;-71.440487,41.866467;-71.440487,41.866467")

#print(resp)

content = resp.content

decode=content.decode("utf-8")

all_data = json.loads(decode)

content1 = all_data['alerts']

#print(content1)

if os.path.isfile("waze_alerts.csv"):

	with open("waze_alerts.csv", "r", encoding="utf8") as f:
	    reader = csv.reader(f)

	    check_reader = reader

	    len_reader = len(list(check_reader))

	with open("waze_alerts.csv", "r", encoding="utf8") as f:

		if len_reader>1:

			reader = csv.reader(f)
			
			## If header exists then skip it
			next(reader, None)

			output = []

			## If tasks (rows) are present after the header then keep a track of task_ids
			for row in reader:
				output.append(str(row[11]))
			
			final_list1=[]

		else:
			output = []
			if len_reader==1:
				final_list1=[]
			else:
				final_list1 = [['Country', 'Magvar', 'Sub type', 'City', 'Street', 'Report Rating', 'Confidence', 'Reliability', 'Latitude', 'Longitude', 'Type', 'Unique Alert ID', 'Publication Timestamp']]
else:
	output = []
	final_list1 = [['Country', 'Magvar', 'Sub type', 'City', 'Street', 'Report Rating', 'Confidence', 'Reliability', 'Latitude', 'Longitude', 'Type', 'Unique Alert ID', 'Publication Timestamp']]


for ele in content1:

	unique_alert_id = ele.get('uuid')

	if unique_alert_id not in output:
		
		country = ele.get('country')
		magvar =  ele.get('magvar')
		sub_type =  ele.get('subtype')
		city =  ele.get('city')
		street =  ele.get('street')
		report_rating = ele.get('reportRating')
		confidence =  ele.get('confidence')
		reliability =  ele.get('reliability')
		latitude =  ele.get('location',{}).get('x')
		longitude =  ele.get('location',{}).get('y')
		Type =  ele.get('type')
		unique_alert_id = ele.get('uuid')
		road_type = ele.get('roadType')
		publication_timestamp = ele.get('pubMillis')
		
		final_list1.append([country, magvar, sub_type, city, street, report_rating, confidence, reliability, latitude, longitude, Type, unique_alert_id, road_type, publication_timestamp])
		print(final_list1)

		## Skip lines which are already present
		with open("waze_alerts.csv", "a", encoding='utf-8', newline='') as f:
			writer = csv.writer(f)
			for element in final_list1:
				writer.writerow(element)

		final_list1=[]


content2 = all_data['jams']

#print(content2)

if os.path.isfile("waze_jams.csv"):

	with open("waze_jams.csv", "r", encoding="utf8") as f:
	    reader = csv.reader(f)

	    check_reader = reader

	    len_reader = len(list(check_reader))

	with open("waze_jams.csv", "r", encoding="utf8") as f:

		if len_reader>1:

			reader = csv.reader(f)
			
			## If header exists then skip it
			next(reader, None)

			output = []

			## If tasks (rows) are present after the header then keep a track of task_ids
			for row in reader:
				output.append(str(row[8]))
			
			final_list2=[]

		else:
			output = []
			if len_reader==1:
				final_list2=[]
			else:
				final_list2 = [['Country', 'City', 'Level', 'Latitude', 'Longitude', 'Length', 'Turn type', 'Type', 'Unique Jam ID', 'End Node', 'Speed', 'Blocking Alert ID', 'Road type', 'Delay', 'Street', 'ID', 'Publication Timestamp']]

else:
	output=[]
	final_list2 = [['Country', 'City', 'Level', 'Latitude', 'Longitude', 'Length', 'Turn type', 'Type', 'Unique Jam ID', 'End Node', 'Speed', 'Blocking Alert ID', 'Road type', 'Delay', 'Street', 'ID', 'Publication Timestamp']]


for ele in content2:

	unique_jam_id = ele.get('uuid')

	if unique_jam_id not in output:
		
		alert_line =  ele.get('line')

		for loc in alert_line:
			alert_country = ele.get('country')
			alert_city =  ele.get('city')
			alert_level =  ele.get('level')

			alert_latitude = loc.get('x')
			alert_longitude = loc.get('y')

			alert_length =  ele.get('length')
			alert_turn_Type = ele.get('turnType')
			alert_Type =  ele.get('type')
			alert_unique_jam_id = ele.get('uuid')
			alert_end_Node = ele.get('endNode')
			alert_speed =  ele.get('speed')
			alert_Type =  ele.get('type')
			alert_blocking_Alert_ID = ele.get('blockingAlertUuid')
			alert_road_type = ele.get('roadType')
			alert_delay = ele.get('delay')
			alert_street = ele.get('street')
			alert_id = ele.get('id')
			alert_publication_timestamp = ele.get('pubMillis')
		
			final_list2.append([alert_country, alert_city, alert_level, alert_latitude, alert_longitude, alert_length, alert_turn_Type, alert_Type, alert_unique_jam_id, alert_end_Node, alert_speed, alert_Type, alert_blocking_Alert_ID, alert_road_type, alert_delay, alert_street, alert_id, alert_publication_timestamp])
			print(final_list2)

			## Skip lines which are already present
			with open("waze_jams.csv", "a", encoding='utf-8', newline='') as f:
				writer = csv.writer(f)
				for element in final_list2:
					writer.writerow(element)

			final_list2=[]


## Execution time
print("Total time taken: " + str(time.clock() - start_time) + " seconds")