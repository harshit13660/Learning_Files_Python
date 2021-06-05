import pygeoip

geo=pygeoip.GeoIP("GeoLiteCity.dat")
rec= geo.record_by_addr("42.108.163.66")

for key, val in rec.items():
    print(f"{key} : {val}")