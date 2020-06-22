To download images for new region, simply change the values of the centerLat and centerLong
variables to the corresponding lattitude and longitude of the center of the region.

Also change the region variable to the name of the region and the total_radius_of_region variable
to the total radius of the region.

The current total_radius_of_region and start_radius are set to continue the data downloads from the point where I halted the downloads. 
The previously downloaded data can be found in Box through this link:  https://tufts.app.box.com/folder/114886356135

Script downloads 200 images each day and sleeps til the next day. This is because 
Google Streetview only allows 200 free downloads per day. You'd be charged for any
extra images downloaded.

Importantly: You'd have to replace the key field in the params dictionary with your 
own access key. You can create this key by setting up an account on Google Cloud.

To run the scripts, you would have to install the following python packages:
geopy
google_streetview
numpy

Contact me at alphonsusbq436@gmail.com with any questions

