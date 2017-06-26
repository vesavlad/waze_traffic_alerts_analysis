## Read CSV file (header assumed), then put that into "csv.data" data object (any name is ok).
rm(list=ls(all=TRUE))

library(ggmap)

#f <- file.choose()

jams <- read.csv((file="C:/Waze/waze_jams.csv"), header=TRUE, sep=",")

index <- c()
latitude <- c()
longitude <- c()

for(id in jams[9]) {
  index <- c(index, as.numeric(id))
}

latitude<-c(latitude,jams$Latitude)

longitude<-c(longitude,jams$Longitude)

routes <- data.frame(cbind(index, latitude, longitude))

ProvidenceMap_Black_and_White <- qmap('providence', zoom = 13, color = 'bw')

show(ProvidenceMap_Black_and_White+
       geom_path(aes(x = longitude, y = latitude, group = factor(index)), data = routes, colour="red", size=1))

ProvidenceMap_Regular <- qmap('providence', zoom = 13)

show(ProvidenceMap_Regular+
       geom_path(aes(x = longitude, y = latitude, group = factor(index)), data = routes, colour="red", size=1))


ProvidenceMap_Satellite <- qmap('providence', zoom = 13, maptype = 'hybrid')

show(ProvidenceMap_Satellite+
       geom_path(aes(x = longitude, y = latitude, group = factor(index)), data = routes, colour="red", size=1))