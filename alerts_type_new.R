## Read CSV file (header assumed), then put that into "csv.data" data object (any name is ok).
library(ggmap)
library(dplyr)
library(dbscan)
library(plyr)

#f <- file.choose()

alerts <- read.csv((file="waze_alerts_big_data.csv"), header=TRUE, sep=",")

ProvidenceMap <- qmap("providence", zoom = 12, color = 'bw', legend="topright")

EPS1 <- 0.00452119
clusters <- dbscan(select(alerts, Longitude, Latitude), eps = EPS1, minPts = 5)
alerts$cluster <- clusters$cluster

groups  <- alerts %>% filter(cluster != 0)
noise  <- alerts %>% filter(cluster == 0)

type_frequency_list<-ddply(alerts,.(Type),nrow)

show(ProvidenceMap+
       geom_point(aes(x = Longitude, y = Latitude), data=alerts, color=as.factor(as.numeric(alerts$Type))))


#Different Types
show(ProvidenceMap + geom_point(aes(x = Longitude, y = Latitude, 
                            colour = Type), 
                        data = alerts ))

df <- transform(alerts, freq= ave(seq(nrow(alerts)), Type, FUN=length))

alerts_freq <- df[order(-df$freq), ]

new_alerts_freq <- arrange(alerts_freq, desc(freq),  Type)

#new_alerts_freq <- merge(alerts, data.frame(table(Type = alerts$Type)), by = c("Type"))

#other_freq <- arrange(type_frequency_list, desc(V1),  Type)

other_freq <- arrange(type_frequency_list, V1,  Type)

new_alerts_freq$Type <- factor(new_alerts_freq$Type, levels = other_freq$Type)

#Relative Size
show(ProvidenceMap + geom_point(aes(x = Longitude, y = Latitude, size = Type,colour = Type), 
                                data = new_alerts_freq ))

#Relative Size with no fill (hollow)
show(ProvidenceMap + geom_point(shape=1, aes(x = Longitude, y = Latitude, size = Type,colour = Type), 
                                stroke=2,
                                data = new_alerts_freq ))
# 
# #Alternative
# alerts$Type <- factor(alerts$Type, levels = other_freq$Type)
# 
# #Relative Size
# show(ProvidenceMap + geom_point(aes(x = Longitude, y = Latitude, size = Type,colour = Type), 
#                                 data = alerts ))


# #Relative Size
# show(ProvidenceMap + geom_point(aes(x = Longitude, y = Latitude), 
#                             size = new_alerts_freq$freq,colour = as.factor(new_alerts_freq$freq), 
#                         data = new_alerts_freq ))
# 
# show(ProvidenceMap + geom_point(aes(x = Longitude, y = Latitude, 
#                                 size = as.factor(as.numeric(freq)),colour = Type),
#                                 data = new_alerts_freq ))

# show(ProvidenceMap+
#        geom_point(aes(x = Longitude, y = Latitude), color="red", alerts) +
#        geom_point(shape=1, aes(x = Longitude, y = Latitude, group = factor(groups$cluster)), data = groups, colour = as.factor(groups$cluster),
#                   size = 3, stroke=2))
# #Average
# mean_lat<-aggregate( Latitude ~ cluster, groups, mean )
# mean_lon<-aggregate( Longitude ~ cluster, groups, mean )
# avg<-data.frame(cbind(mean_lat$cluster,mean_lon$Longitude,mean_lat$Latitude))
# 
# show(ProvidenceMap+
#        geom_point(aes(x = Longitude, y = Latitude), color="brown", noise) +
#        geom_point(shape=1, aes(x = avg$X2, y = avg$X3, group = factor(avg$X1)), colour=as.factor(avg$X1), data=avg, size = 2, stroke=2))
# 
# show(ProvidenceMap+
#        geom_point(aes(x = Longitude, y = Latitude), color="brown", noise) +
#        geom_point(aes(x = Longitude, y = Latitude, group = factor(groups$cluster)), data = groups, colour = as.factor(groups$cluster)) +
#        geom_point(shape=1, aes(x = avg$X2, y = avg$X3, group = factor(avg$X1)), colour="yellow", data=avg, size = 2, stroke=2))