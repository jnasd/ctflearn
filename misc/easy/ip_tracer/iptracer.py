#!/usr/bin/python

# Method1: 1) https://chaipip.com/ip.php 2) input 159.167.16.5 3) shows in Englan London
# Method2: pip install geoip2

import geoip2.database

# download newest GeoLite2-City.mmdb from https://www.maxmind.com/en/geoip2-city
reader = geoip2.database.Reader('./GeoLite2-City.mmdb')
response = reader.city('159.167.16.5')

print(response.country.name)
print(response.city.name)
print(response.location.longitude)
print(response.location.latitude)


# The flag is: london
