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
centerLat = 43.7182355
centerLong = -79.377257
origin = geopy.Point(centerLat, centerLong)

distances = []
count = 0

#Distances in miles
radius_delta = 0.5
total_radius_of_region = 16.1557
start_radius = 0.5
mile_radius = start_radius
region = 'Toronto/'

#append all the radii into the 'distances' array
for i in np.arange(start_radius, total_radius_of_region, radius_delta):
        distances.append(i/0.62137119) #convert miles to kilometers

for i in distances:
        #Going a full 360 degrees and grabbing latitudes and longitudes of 
        #2000 points around the circle with radius i
        lat=[]
        long=[]
        bearing = 0
        while(bearing <= 360):
                destination = VincentyDistance(kilometers=i).destination(origin, bearing)
                lat.append(destination.latitude)
                long.append(destination.longitude)
                bearing = bearing + 0.18

        coordinates = tuple(zip(lat,long))

        params = [{
                'size': '600x300', # max 640x640 pixels
                'location': '46.414382,10.013988',
                'heading': '151.78',
                'pitch': '-0.76',
                'key': <<YOU WOULD HAVE TO FILL THIS PORTION WITH YOUR ACCESS KEY FROM GOOGLE CLOUD>>
                }]


        for coord in coordinates:
                thelat = coord[0]
                thelong = coord[1]
                params[0]['location']=str(thelat)+','+str(thelong)
                results = google_streetview.api.results(params)

                # Download images to directory 'downloads'
                results.download_links(region +str(mile_radius)+'_mile_radius/'+str(count))
                count = count+1

        mile_radius = mile_radius+0.5
        count = count+2000

        #sleep till next day
        time.sleep(100000)

