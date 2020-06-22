#! /usr/bin/env python

'''
Written by Alphonsus Adu-Bredu for the Urban Attitudes Lab, Tufts University
'''

import schedule
import time
import geopy
import numpy as np
from geopy.distance import VincentyDistance
import google_streetview.api


#latitude and longitude of center of region
centerLat = 42.933178
centerLong = -81.329544

bearing = 0
radii = []
count = 0

#Distances in miles
radius_delta = 0.1
total_radius_of_region = 25.25
start_radius = 11.
mile_radius = start_radius
region = 'London/'

#append all the radii into the 'distances' array
for i in np.arange(start_radius, total_radius_of_region, radius_delta):
        radii.append(i/0.62137119) #convert miles to kilometers
#print(radii)

#'''

for i in radii:
        #Going a full 360 degrees and grabbing latitudes and longitudes of 
        #500 points around the circle with radius i. so about 12,500 images in all
	
        lat=[]
        long=[]
        while(bearing <= 360):
                origin = geopy.Point(centerLat, centerLong)
                destination = VincentyDistance(kilometers=i).destination(origin, bearing)
                lat.append(destination.latitude)
                long.append(destination.longitude)
                bearing = bearing + 0.72
        
	bearing = 0
        coordinates = tuple(zip(lat,long))
        
        params = [{
                'size': '600x300', # max 640x640 pixels
                'location': '46.414382,10.013988',
                'heading': '151.78',
                'pitch': '-0.76',
                'key': '<<YOU WOULD HAVE TO FILL THIS PORTION WITH YOUR ACCESS KEY FROM GOOGLE CLOUD>>' 
                }]
        
        for coord in coordinates:
                thelat = coord[0]
                thelong = coord[1]
                params[0]['location']=str(thelat)+','+str(thelong)
                results = google_streetview.api.results(params)
                
                # Download images to directory 'downloads'
                results.download_links(region +str(mile_radius)+'_mile_radius/'+str(count))
		time.sleep(2)
                count = count+1
        
        mile_radius += 0.1

        #sleep till next day
        time.sleep(86400)
#'''                
#for i in radii:
#	print i


