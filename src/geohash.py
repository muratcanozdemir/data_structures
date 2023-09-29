def geohash(latitude, longitude, precision=5):
    lat_interval = [-90.0, 90.0]
    lon_interval = [-180.0, 180.0]
    geohash = []
    even_bit = True
    bit = 0
    ch = 0
    base32 = '0123456789bcdefghjkmnpqrstuvwxyz'

    while len(geohash) < precision:
        if even_bit:
            mid = (lon_interval[0] + lon_interval[1]) / 2
            if longitude > mid:
                ch |= 1 << (4 - bit)
                lon_interval = (mid, lon_interval[1])
            else:
                lon_interval = (lon_interval[0], mid)
        else:
            mid = (lat_interval[0] + lat_interval[1]) / 2
            if latitude > mid:
                ch |= 1 << (4 - bit)
                lat_interval = (mid, lat_interval[1])
            else:
                lat_interval = (lat_interval[0], mid)
        
        even_bit = not even_bit
        
        if bit < 4:
            bit += 1
        else:
            geohash.append(base32[ch])
            bit = 0
            ch = 0
    
    return ''.join(geohash)

# Usage:
# latitude = 37.4219999
# longitude = -122.0840575
# precision = 5

# geohash_code = geohash(latitude, longitude, precision)
# print(geohash_code)  # Output: '9q9hv'
