import json
from django.core.files import File

print "starting data import"

#execfile('feeder/import_data.py')

with open('feeder/yelp_data.json') as data_file:    
    print data_file
    data = json.load(data_file)
    print data