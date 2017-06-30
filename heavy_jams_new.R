## Read CSV file (header assumed), then put that into "csv.data" data object (any name is ok).
rm(list=ls(all=TRUE))

library(ggmap)
library(plyr)
library(dplyr)

#f <- file.choose()

jams <- read.csv((file="C:/Waze/waze_jams_big_data.csv"), header=TRUE, sep=",")

index <- c()
latitude <- c()
longitude <- c()

for(id in jams[9]) {
  index <- c(index, as.numeric(id))
}

latitude<-c(latitude,jams$Latitude)

longitude<-c(longitude,jams$Longitude)

routes <- data.frame(cbind(index, latitude, longitude))

ProvidenceMap_Black_and_White <- qmap('providence', zoom = 12, color = 'bw')

show(ProvidenceMap_Black_and_White+
       geom_path(aes(x = longitude, y = latitude, group = factor(index)), data = routes, colour="yellow", size=1))

ProvidenceMap_Regular <- qmap('providence', zoom = 12)

show(ProvidenceMap_Regular+
       geom_path(aes(x = longitude, y = latitude, group = factor(index)), data = routes, colour="yellow", size=1))


ProvidenceMap_Satellite <- qmap('providence', zoom = 12, maptype = 'hybrid')

show(ProvidenceMap_Satellite+
       geom_path(aes(x = longitude, y = latitude, group = factor(index)), data = routes, colour="yellow", size=1))

#Heavy Traffic Jams
index_list<-ddply(routes,.(index),nrow)

#Traffic lines with greater than 50 points
index_groups  <- index_list %>% filter(V1 > 50)

sub_routes <- subset(routes, index %in% index_groups$index)

show(ProvidenceMap_Black_and_White+
       geom_path(aes(x = longitude, y = latitude, group = factor(index)), data = sub_routes, colour="red", size=1))

show(ProvidenceMap_Regular+
       geom_path(aes(x = longitude, y = latitude, group = factor(index)), data = sub_routes, colour="red", size=1))

show(ProvidenceMap_Satellite+
       geom_path(aes(x = longitude, y = latitude, group = factor(index)), data = sub_routes, colour="red", size=1))