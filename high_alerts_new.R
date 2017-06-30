## Read CSV file (header assumed), then put that into "csv.data" data object (any name is ok).
library(ggmap)
library(dplyr)
library(dbscan)

#f <- file.choose()

alerts <- read.csv((file="C:/Waze/waze_alerts_big_data.csv"), header=TRUE, sep=",")

ProvidenceMap <- qmap("providence", zoom = 12, color = 'bw')

EPS1 <- 0.00452119
clusters <- dbscan(select(alerts, Longitude, Latitude), eps = EPS1, minPts = 5)
alerts$cluster <- clusters$cluster

groups  <- alerts %>% filter(cluster != 0)
noise  <- alerts %>% filter(cluster == 0)

show(ProvidenceMap+
       geom_point(aes(x = Longitude, y = Latitude), color="red", alerts) +
       geom_point(shape=1, aes(x = Longitude, y = Latitude, group = factor(groups$cluster)), data = groups, colour = as.factor(groups$cluster),
                  size = 3, stroke=2))
#Average
mean_lat<-aggregate( Latitude ~ cluster, groups, mean )
mean_lon<-aggregate( Longitude ~ cluster, groups, mean )
avg<-data.frame(cbind(mean_lat$cluster,mean_lon$Longitude,mean_lat$Latitude))

show(ProvidenceMap+
       geom_point(aes(x = Longitude, y = Latitude), color="brown", noise) +
       geom_point(shape=1, aes(x = avg$X2, y = avg$X3, group = factor(avg$X1)), colour=as.factor(avg$X1), data=avg, size = 2, stroke=2))

show(ProvidenceMap+
       geom_point(aes(x = Longitude, y = Latitude), color="brown", noise) +
       geom_point(aes(x = Longitude, y = Latitude, group = factor(groups$cluster)), data = groups, colour = as.factor(groups$cluster)) +
       geom_point(shape=1, aes(x = avg$X2, y = avg$X3, group = factor(avg$X1)), colour="yellow", data=avg, size = 2, stroke=2))
	   
# show(ProvidenceMap+
#        geom_point(aes(x = Longitude, y = Latitude), data = alerts, color="red", size=1) +
#        geom_point(aes(fill = "grey"), noise) +
#        geom_point(aes(colour = as.factor(alerts$cluster), x = Longitude, y = Latitude), groups,
#                   size = 3))