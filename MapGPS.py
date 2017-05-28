import math
import csv
import numpy
import matplotlib.pyplot
import matplotlib.patches as mpatches


# taking in csv of format:
# b_lat,b_long,b_accuracy,GPS_lat,GPS_long,GPS_accuracy,f_lat,f_long
linecount = 1
with open("BecGPSSensorFusionEastToWest") as Datafile:
    for line in Datafile:
        datalist= csv.reader(Datafile)
        datalist = list(datalist)

#setting up image to plot on

img = matplotlib.pyplot.imread("SensorFusionBusStopBackground.JPG")
fig, ax = matplotlib.pyplot.subplots()
figLongLow = -122.062545
figLongHigh = -122.061967
figLatLow = 36.999740
figLatHigh = 37.000180
ax.imshow(img, extent=[figLongLow, figLongHigh, figLatLow ,figLatHigh ])
#Bottomleft 36.999740,-122.062545
#TopRight  37.000180,-122.061967

ErrorHolder = []
w, h = 1000, len(datalist);
MagHold = [[] for i in range(3000)]
MagIndex = [0 for x in range(w)]
print (len(datalist))
StartLat = 37.000001     #Start position 37.000001, -122.062226
StartLong = -122.062226
StopLat = 36.999914      #End position 36.999914, -122.062424
StopLong = -122.062424
Velx = 0.47       #Velocity per unit time

actualoriginlong = -122.06234664
actualoriginlat = 36.9999456,

matplotlib.pyplot.plot( [StartLong, StopLong], [StartLat, StopLat], 'y-', lw=3)
#matplotlib.pyplot.plot( [-122.062390, -122.062398], [37.000014, 36.999920], 'y-', lw=3)
#36.999920, -122.062390 south actual
#37.000014, -122.062398 north actual

findstatLat = []
findstatLong = []
for n in range(0,len(datalist)):
    BecestimateLat = float(datalist[n][0])   #Enter index of predicted X here
    BecestimateLong= float(datalist[n][1])    #Enter index of predicted Y here
    Becestimateaccuracy = float(datalist[n][2]) #Index of BLE accuracy
    matplotlib.pyplot.plot(BecestimateLong,BecestimateLat , 'bo')
    GPSestimateLat = float(datalist[n][3])  # Enter index of predicted X here
    GPSestimateLong = float(datalist[n][4])  # Enter index of predicted Y here
    GPSestimateaccuracy = float(datalist[n][5])  # Index of BLE accuracy
    matplotlib.pyplot.plot(GPSestimateLong, GPSestimateLat, 'ro')
    FinalestimateLat = float(datalist[n][6])  # Enter index of predicted X here
    FinalestimateLong = float(datalist[n][7])  # Enter index of predicted Y here
    #Finalestimateaccuracy = float(datalist[n][8])  # Index of BLE accuracy
    if (FinalestimateLong == GPSestimateLong)and(FinalestimateLat == GPSestimateLat):
        matplotlib.pyplot.plot(FinalestimateLong, FinalestimateLat, 'wP')
    else: matplotlib.pyplot.plot(FinalestimateLong, FinalestimateLat, 'wo')

matplotlib.pyplot.plot(actualoriginlong, actualoriginlat, 'co')


GraphWhiteSpace = 0.00002
#matplotlib.pyplot.ylim(min(findstatLat) - GraphWhiteSpace ,max(findstatLat) + GraphWhiteSpace)
#matplotlib.pyplot.xlim(min(findstatLong) - GraphWhiteSpace,StartLong + GraphWhiteSpace)
#matplotlib.pyplot.ylim(min(findstatLat) - GraphWhiteSpace ,max(findstatLat) + GraphWhiteSpace)
matplotlib.pyplot.ylim(figLatLow ,figLatHigh)
matplotlib.pyplot.xlim(figLongLow ,figLongHigh)
red_patch = mpatches.Patch(color='red', label='GPS Measurements')
yellow_patch = mpatches.Patch(color='yellow', label='Actual Location')
blue_patch = mpatches.Patch(color='blue', label='BLE Location')
white_patch = mpatches.Patch(color='white', label='Final/Sensor Fused')
matplotlib.pyplot.legend(handles=[yellow_patch, red_patch, blue_patch, white_patch])

matplotlib.pyplot.show()
