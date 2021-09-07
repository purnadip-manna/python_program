import math
def deg_to_dms(deg, type='lat'):
    decimals, number = math.modf(deg)
    d = int(number)
    m = int(decimals * 60)
    s = (deg - d - m / 60) * 3600.00
    compass = {
        'lat': ('N','S'),
        'lon': ('E','W')
    }
    compass_str = compass[type][0 if d >= 0 else 1]
    return '{}º{}\'{:.2f}"{}'.format(abs(d), abs(m), abs(s), compass_str)

    
lat = float(input("Enter : "))
lon = float(input("Enter : "))
location_url = "https://www.google.com/maps/place/"+deg_to_dms(lat)+"+"+deg_to_dms(lon, 'lon')
print(location_url)
