import requests
import json
import csv
import time

## Start the clock
start_time = time.clock()

resp = requests.get("https://na-georss.waze.com/rtserver/web/TGeoRSS?tk=ccp_partner&ccp_partner_name=Providence&format=JSON&types=traffic,alerts,irregularities&polygon=-71.440487,41.866467;-71.374741,41.858029;-71.375427,41.828744;-71.395512,41.810450;-71.373367,41.785033;-71.405811,41.764486;-71.445465,41.786057;-71.446238,41.801095;-71.489410,41.817281;-71.440487,41.866467;-71.440487,41.866467")

#print(resp)

content = resp.content

decode=content.decode("utf-8")

all_data = json.loads(decode)

content1 = all_data['alerts']

final_list1 = [['Country', 'Magvar', 'Sub type', 'City', 'Street', 'Report Rating', 'Confidence', 'Reliability', 'Latitude', 'Longitude', 'Type', 'User ID', 'Publication Timestamp']]

#print(content1)

for ele in content1:

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
	user_id = ele.get('uuid')
	road_type = ele.get('roadType')
	publication_timestamp = ele.get('pubMillis')
	
	final_list1.append([country, magvar, sub_type, city, street, report_rating, confidence, reliability, latitude, longitude, Type, user_id, road_type, publication_timestamp])
	print(final_list1)

	## Skip lines which are already present
	with open("waze_alerts.csv", "a", encoding='utf-8', newline='') as f:
		writer = csv.writer(f)
		for element in final_list1:
			writer.writerow(element)

	final_list1=[]

final_list2 = [['Country', 'City', 'Level', 'Line', 'Length', 'Turn type', 'Type', 'User ID', 'End Node', 'Speed', 'Road type', 'Delay', 'Street', 'ID', 'Publication Timestamp']]

content2 = all_data['jams']

## Execution time
print("Total time taken: " + str(time.clock() - start_time) + " seconds")	