# waze_data

## This is a system to analyze data from Waze application. 

### It is used to improve accuracy of Alerts, visualize and study Traffic data

#### To run the Python code:-

* Run "waze_data.py" to extract data from Waze application.
* Run "waze_big_data.py" to extract data for 30 minutes from Waze application.


#### To run the R code:-

#### For Alerts:-
* Run "analysis_alerts.R" to visualize all alerts in a Map.
* Run "analysis_alerts_new.R" to cluster the Geospatial data and improve accuracy of the location of alerts in a Map.
* Run "high_alerts_new.R" to visualize only High Alert Regions with minumum 5 points, cluster the Geospatial data and improve accuracy of the location of alerts in a Map.
* Run "alerts_type_new.R" to partition the data based on type and visualize the Geospatial data based on frequency of alert's type.

#### For Traffic Jams:-
* Run "analysis_jams_new.R" to visualize Traffic Jams routes on 3 different Map types.
* Run "heavy_jams_new.R" to visualize Heavy Traffic Jams routes with greater than 50 points on 3 different Map types.
