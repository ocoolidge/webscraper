from autoscraper import AutoScraper

url1 = 'https://www.discogs.com/search/?limit=250&style_exact=House&sort=have%2Cdesc&ev=gs_mc&page=1'
url2 = 'https://www.discogs.com/search/?limit=250&style_exact=House&sort=have%2Cdesc&ev=gs_mc&page=2'
url3 = 'https://www.discogs.com/search/?limit=250&style_exact=House&sort=have%2Cdesc&ev=gs_mc&page=3'
url4 = 'https://www.discogs.com/search/?limit=250&style_exact=House&sort=have%2Cdesc&ev=gs_mc&page=4'
url5 = 'https://www.discogs.com/search/?limit=250&style_exact=House&sort=have%2Cdesc&ev=gs_mc&page=5'
url6 = 'https://www.discogs.com/search/?limit=250&style_exact=House&sort=have%2Cdesc&ev=gs_mc&page=6'
url7 = 'https://www.discogs.com/search/?limit=250&style_exact=House&sort=have%2Cdesc&ev=gs_mc&page=7'
url8 = 'https://www.discogs.com/search/?limit=250&style_exact=House&sort=have%2Cdesc&ev=gs_mc&page=8'
url9 = 'https://www.discogs.com/search/?limit=250&style_exact=House&sort=have%2Cdesc&ev=gs_mc&page=9'
url10 = 'https://www.discogs.com/search/?limit=250&style_exact=House&sort=have%2Cdesc&ev=gs_mc&page=10'


wanted_list = ["Discovery"]

scraper = AutoScraper()
result = scraper.build(url1, wanted_list)
print(result)

with open("outputs/allTen.txt", "w") as txt_file:
    for line in result:
        txt_file.write("".join(line) + "\n") # works with any number of elements in a line


wanted_list = ["Dreamer"]

result = scraper.build(url2, wanted_list)
print(result)

with open("outputs/allTen.txt", "a") as txt_file:
    for line in result:
        txt_file.write("".join(line) + "\n") # works with any number of elements in a line


wanted_list = ["In Our Heads"]

result = scraper.build(url3, wanted_list)
print(result)

with open("outputs/allTen.txt", "a") as txt_file:
    for line in result:
        txt_file.write("".join(line) + "\n") # works with any number of elements in a line


wanted_list = ["La Mouche"]

result = scraper.build(url4, wanted_list)
print(result)

with open("outputs/allTen.txt", "a") as txt_file:
    for line in result:
        txt_file.write("".join(line) + "\n") # works with any number of elements in a line


wanted_list = ["Love Story [Vs Finally]"]

result = scraper.build(url5, wanted_list)
print(result)

with open("outputs/allTen.txt", "a") as txt_file:
    for line in result:
        txt_file.write("".join(line) + "\n") # works with any number of elements in a line


wanted_list = ["That Sound"]

result = scraper.build(url6, wanted_list)
print(result)

with open("outputs/allTen.txt", "a") as txt_file:
    for line in result:
        txt_file.write("".join(line) + "\n") # works with any number of elements in a line


wanted_list = ["Bamboogie"]

result = scraper.build(url7, wanted_list)
print(result)

with open("outputs/allTen.txt", "a") as txt_file:
    for line in result:
        txt_file.write("".join(line) + "\n") # works with any number of elements in a line


wanted_list = ["Sandwiches"]

result = scraper.build(url8, wanted_list)
print(result)

with open("outputs/allTen.txt", "a") as txt_file:
    for line in result:
        txt_file.write("".join(line) + "\n") # works with any number of elements in a line


wanted_list = ["Flash (Remixes)"]

result = scraper.build(url9, wanted_list)
print(result)

with open("outputs/allTen.txt", "a") as txt_file:
    for line in result:
        txt_file.write("".join(line) + "\n") # works with any number of elements in a line


wanted_list = ["Electric Avenue (Ringbang Remix)"]

result = scraper.build(url10, wanted_list)
print(result)

with open("outputs/allTen.txt", "a") as txt_file:
    for line in result:
        txt_file.write("".join(line) + "\n") # works with any number of elements in a line

