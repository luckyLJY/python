from  pygal_maps_world.i18n import COUNTRIES
# pip install pygal_maps_world

for county_code in sorted(COUNTRIES.keys()):
    print(county_code,COUNTRIES[county_code])