## Read CSV file (header assumed), then put that into "csv.data" data object (any name is ok).
library(ggmap)
#library(Rcpp)

#f <- file.choose()

alerts <- read.csv((file="C:/Waze/waze_alerts.csv"), header=TRUE, sep=",")

ProvidenceMap <- qmap("providence", zoom = 12, maptype = 'hybrid')

show(ProvidenceMap+
#geom_point(data = alerts, aes(x = Longitude, y = Latitude), color="red", size=30, alpha=0.5)
geom_point(aes(x = as.numeric(as.character(Longitude)), y = as.numeric(as.character(Latitude))), data = alerts, color="red", size=3))
