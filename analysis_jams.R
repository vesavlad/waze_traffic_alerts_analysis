## Read CSV file (header assumed), then put that into "csv.data" data object (any name is ok).
library(ggmap)
library(Rcpp)

#f <- file.choose()

jams <- read.csv((file="C:/Waze/waze_jams.csv"), header=TRUE, sep=",")

ProvidenceMap <- qmap("providence", zoom = 12, maptype = 'hybrid')

show(ProvidenceMap+
#geom_point(data = alerts, aes(x = Longitude, y = Latitude), color="red", size=30, alpha=0.5)
geom_point(aes(x = as.numeric(as.character(Longitude)), y = as.numeric(as.character(Latitude))), data = alerts, color="red", size=3))

index <- c()
latitude <- c()
longitude <- c()

index <- c(index, jams$ID)
latitude <- c(latitude, jams$Latitude)
longitude <- c(longitude, jams$Longitude)

for(i in 1:nrow(jams)) {
 index <- c(index, jams$ID)
 latitude <- c(latitude, jams$Latitude)
 longitude <- c(longitude, jams$Longitude)
}

test <- read.csv((file="C:/Waze/test.csv"), header=TRUE, sep=",")

index <- c()
latitude <- c()
longitude <- c()


  index <- c(index, test$Jam_ID)
  latitude <- c(latitude, test$Latitude)
  longitude <- c(longitude, test$Longitude)

routes <- data.frame(cbind(index, latitude, longitude))




NewMap <- qmap('providence', zoom = 12, color = 'bw')

show(NewMap+
geom_path(aes(x = longitude, y = latitude, group = factor(index)), data = routes, colour="red", size=30))




index <- c()
latitude <- c()
longitude <- c()

index <- c(index, 10232331)
index <- c(index, 10232331)

latitude <- c(latitude, 41.816604, 41.816771)

longitude <-c(longitude, -71.409714, -71.409306)

index <- c(index, 10232334)
index <- c(index, 10232334)

latitude <- c(latitude, 41.824448, 41.8241)

longitude <-c(longitude, -71.410526,-71.411026)

routes <- data.frame(cbind(index, latitude, longitude))

NewMap <- qmap('providence', zoom = 12, color = 'bw')

show(NewMap+
       geom_path(aes(x = longitude, y = latitude, group = factor(index)), data = routes, colour="red", size=30))



for(i in jams[9]) {
 index1 <- c(index1, as.numeric(i))
}

latitude1<-c()
latitude1<-c(latitude1,jams$Latitude)

longitude1<-c()
longitude1<-c(longitude1,jams$Longitude)

routes1 <- data.frame(cbind(index1, latitude1, longitude1))

NewMap <- qmap('providence', zoom = 13, color = 'bw')

show(NewMap+
       geom_path(aes(x = longitude1, y = latitude1, group = factor(index1)), data = routes1, colour="red", size=1))
