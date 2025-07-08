url = '한글도메인.com'

url_to_punny = url.encode('idna').decode()
punny_to_url = url_to_punny.encode().decode('idna')

print(url_to_punny)
print(punny_to_url)