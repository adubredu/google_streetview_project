To download images for new region, simply change the values of the centerLat and centerLong
variables to the corresponding lattitude and longitude of the center of the region.

Also change the region variable to the name of the region and the total_radius_of_region variable
to the total radius of the region.

Script downloads 200 images each day and sleeps til the next day. This is because 
Google Streetview only allows 200 free downloads per day. You'd be charged for any
extra images downloaded.

Importantly: You'd have to replace the key field in the params dictionary with your 
own access key. You can create this key by setting up an account on Google Cloud.

