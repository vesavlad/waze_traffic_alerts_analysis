import requests
import json
import csv
import time
import os	

#Total time in minutes
cnt_sleep = 0

while True:
	
	## Start the clock
	start_time = time.clock()

	resp = requests.get("https://na-georss.waze.com/rtserver/web/TGeoRSS?tk=ccp_partner&ccp_partner_name=Providence&format=JSON&types=traffic,alerts,irregularities&polygon=-71.440487,41.866467;-71.374741,41.858029;-71.375427,41.828744;-71.395512,41.810450;-71.373367,41.785033;-71.405811,41.764486;-71.445465,41.786057;-71.446238,41.801095;-71.489410,41.817281;-71.440487,41.866467;-71.440487,41.866467")

	#print(resp)

	content = resp.content

	#print(content1)

	decode=content.decode("utf-8")

	all_data = json.loads(decode)

	content1 = all_data['alerts']

	if os.path.isfile("waze_alerts_big_data.csv"):

		with open("waze_alerts_big_data.csv", "r", encoding="utf8") as f:
		    reader = csv.reader(f)

		    check_reader = reader

		    len_reader = len(list(check_reader))

		with open("waze_alerts_big_data.csv", "r", encoding="utf8") as f:

			if len_reader>1:

				reader = csv.reader(f)
				
				## If header exists then skip it
				next(reader, None)

				output1 = []

				## If tasks (rows) are present after the header then keep a track of task_ids
				for row in reader:
					output1.append(str(row[11]))
				
				final_list1=[]

			else:
				output1 = []
				if len_reader==1:
					final_list1=[]
				else:
					final_list1 = [['Country', 'Magvar', 'Sub type', 'City', 'Street', 'Report Rating', 'Confidence', 'Reliability', 'Latitude', 'Longitude', 'Type', 'Unique Alert ID', 'Publication Timestamp']]
	else:
		output1 = []
		final_list1 = [['Country', 'Magvar', 'Sub type', 'City', 'Street', 'Report Rating', 'Confidence', 'Reliability', 'Latitude', 'Longitude', 'Type', 'Unique Alert ID', 'Road Type', 'Publication Timestamp']]


	for ele in content1:

		unique_alert_id = ele.get('uuid')

		if unique_alert_id not in output1:
			
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
			
			final_list1.append([country, magvar, sub_type, city, street, report_rating, confidence, reliability, longitude, latitude, Type, unique_alert_id, road_type, publication_timestamp])
			print(final_list1)

			## Skip lines which are already present
			with open("waze_alerts_big_data.csv", "a", encoding='utf-8', newline='') as f:
				writer = csv.writer(f)
				for element in final_list1:
					writer.writerow(element)

			final_list1=[]


	content2 = all_data['jams']

	#print(content2)

	if os.path.isfile("waze_jams_big_data.csv"):

		with open("waze_jams_big_data.csv", "r", encoding="utf8") as f:
		    reader = csv.reader(f)

		    check_reader = reader

		    len_reader = len(list(check_reader))

		with open("waze_jams_big_data.csv", "r", encoding="utf8") as f:

			if len_reader>1:

				reader = csv.reader(f)
				
				## If header exists then skip it
				next(reader, None)

				output2 = []

				## If tasks (rows) are present after the header then keep a track of task_ids
				for row in reader:
					output2.append(str(row[8]))
				
				final_list2=[]

			else:
				output2 = []
				if len_reader==1:
					final_list2=[]
				else:
					final_list2 = [['Country', 'City', 'Level', 'Latitude', 'Longitude', 'Length', 'Turn type', 'Type', 'Unique Jam ID', 'End Node', 'Speed', 'Blocking Alert ID', 'Road type', 'Delay', 'Street', 'ID', 'Publication Timestamp']]

	else:
		output2=[]
		final_list2 = [['Country', 'City', 'Level', 'Latitude', 'Longitude', 'Length', 'Turn type', 'Type', 'Unique Jam ID', 'End Node', 'Speed', 'Blocking Alert ID', 'Road type', 'Delay', 'Street', 'ID', 'Publication Timestamp']]


	for ele in content2:

		unique_jam_id = ele.get('uuid')

		if unique_jam_id not in output2:
			
			jam_line =  ele.get('line')

			for loc in jam_line:
				jam_country = ele.get('country')
				jam_city =  ele.get('city')
				jam_level =  ele.get('level')

				jam_latitude = loc.get('x')
				jam_longitude = loc.get('y')

				jam_length =  ele.get('length')
				jam_turn_Type = ele.get('turnType')
				jam_Type =  ele.get('type')
				unique_jam_id = ele.get('uuid')
				jam_end_Node = ele.get('endNode')
				jam_speed =  ele.get('speed')
				jam_blocking_Alert_ID = ele.get('blockingAlertUuid')
				jam_road_type = ele.get('roadType')
				jam_delay = ele.get('delay')
				jam_street = ele.get('street')
				jam_id = ele.get('id')
				jam_publication_timestamp = ele.get('pubMillis')
			
				final_list2.append([jam_country, jam_city, jam_level, jam_longitude, jam_latitude, jam_length, jam_turn_Type, jam_Type, unique_jam_id, jam_end_Node, jam_speed, jam_blocking_Alert_ID, jam_road_type, jam_delay, jam_street, jam_id, jam_publication_timestamp])
				print(final_list2)

				## Skip lines which are already present
				with open("waze_jams_big_data.csv", "a", encoding='utf-8', newline='') as f:
					writer = csv.writer(f)
					for element in final_list2:
						writer.writerow(element)

				final_list2=[]


	## Execution time
	print("\nTime taken: " + str(time.clock() - start_time) + " seconds\n")

	cnt_sleep+=1
	
	print("Total time elapsed for extracting data: " + str(cnt_sleep*2) + " minutes\n")

	print("Total time left for extracting data: " + str(total_time-cnt_sleep*2) + " minutes\n")
		
	if cnt_sleep*2>=total_time:
		break

	else:
		#Sleep for 2 minutes
		time.sleep(120)
