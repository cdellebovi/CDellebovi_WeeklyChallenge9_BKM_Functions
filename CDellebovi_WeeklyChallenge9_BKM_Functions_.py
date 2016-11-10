#Charles Dellebovi
#Pratt LIS-664-01: Fall 2016
#Programming for Cultural Heritage: Weekly Challenge 9 - BKM Functions
#Complete List of the Brooklyn Museum's Historical Watercolor Exhibitions with Corrected Contemporary Watercolor Spelling (One Word) 

import requests, json

#from bs4 import BeautifulSoup

#all_exhibitions = []

#current_page = 0
#while current_page == 5:
#    pass
#while current_page <= 4:

#    url = "https://www.brooklynmuseum.org/opencollection/search?title=watercolor&type=exhibitions&limit=12&offset=" + str(current_page*12)
#    exhibitions_page = requests.get(url)
#    page_html = exhibitions_page.text

#    soup = BeautifulSoup(page_html, "html.parser")
#    exhibition_info = soup.find_all("span", attrs = {"class": "item-title"})
#    for an_exhibition in exhibition_info:
#            if an_exhibition not in all_exhibitions:
#                all_exhibitions.append(an_exhibition.text)
#    current_page = current_page + 1

#current_page = 0
#while current_page == 2:
#    pass
#while current_page <= 1:

#    url = "https://www.brooklynmuseum.org/opencollection/search?title=water+color&type=exhibitions&limit=12&offset=" + str(current_page*12)
#    exhibitions_page = requests.get(url)
#    page_html = exhibitions_page.text

#    soup = BeautifulSoup(page_html, "html.parser")
#    exhibition_info = soup.find_all("span", attrs = {"class": "item-title"})
#    for an_exhibition in exhibition_info:
#            if an_exhibition not in all_exhibitions:
#                all_exhibitions.append(an_exhibition.text)
#    current_page = current_page + 1

#print(sorted(set(all_exhibitions)))

#_____________________________________________________________________________________________________________
#commented-out code above this line used to populate 'all_exhibitions' list below.

def find_and_replace(a_list,look_for,replace_with):

    if look_for in a_list:
        pos = a_list.index(look_for)
        a_list[pos] = replace_with
        return a_list
    else:
        return False

all_exhibitions = ['American Watercolors', 'American Watercolors and Pastels from the Collection', 'American Watercolors and Winslow Homer', 'American Watercolors from the Museum Collection', 'Architectural Watercolors by American Architects', 'Brooklyn Watercolor Society', 'Brushed with Light: American Landscape Watercolors from the Collection', 'Cezanne Watercolors and Oils from the Collection of Mr. & Mrs. Henry Pearlman', 'Contemplating the American Watercolor: Selections from the Transco Energy Company Collection', "Curator's Choice: American Watercolor Masters: Winslow Homer and John Singer Sargent", "Curator's Choice: The American Watercolor Movement, 1860-1900", 'George Pearse Ennis & Paul Ludwig Gill: Memorial Exhibition of Water Colors', 'Homer & Sargent Watercolors from the Museum Collection', 'Homer and Sargent: Watercolors, Prints and Drawings', 'Homer, Sargent & the American Watercolor Tradition', 'International Watercolor Exhibition, 01st Biennial: Water Color Paintings by American Artists', 'International Watercolor Exhibition, 02nd Biennial', 'International Watercolor Exhibition, 03rd Biennial', 'International Watercolor Exhibition, 04th Biennial', 'International Watercolor Exhibition, 05th Biennial', 'International Watercolor Exhibition, 06th Biennial: Water Color Paintings, Pastels and Drawings by American and Foreign Artis...', 'International Watercolor Exhibition, 07th Biennial', 'International Watercolor Exhibition, 08th Biennial', 'International Watercolor Exhibition, 09th Biennial', 'International Watercolor Exhibition, 10th Biennial', 'International Watercolor Exhibition, 11th Biennial', 'International Watercolor Exhibition, 12th Biennial', 'International Watercolor Exhibition, 13th Biennial', 'International Watercolor Exhibition, 14th Biennial', 'International Watercolor Exhibition, 15th Biennial', 'International Watercolor Exhibition, 16th Biennial', 'International Watercolor Exhibition, 17th Biennial', 'International Watercolor Exhibition, 18th Biennial', 'International Watercolor Exhibition, 19th Biennial, Trends in Watercolor Today', 'International Watercolor Exhibition, 20th Biennial', 'International Watercolor Exhibition, 21st Biennial', 'International Watercolor Exhibition, 22nd Biennial', 'Island Peoples of the Pacific: Photographs of Hawaiian Island People and Watercolors of Tahiti by Stephen Haweis', 'J.M.W. Turner Watercolors from The British Museum', 'Jeannette McFadden: Watercolors', 'John Singer Sargent Watercolors', 'Luce Visible Storage/Study Center: Watercolors by the American Pre-Raphaelites', 'Luis Castillo: Oil Paintings, Pastels, Watercolors', 'Masters of Color and Light: Homer, Sargent and the American Watercolor Movement', 'Nineteenth-Century French Drawings and Watercolors from the Collection of The Brooklyn Museum', 'Oil Paintings and Water Colors by California Artists. The Post-Surrealists', 'Oil Paintings, Water Colors & Prints: WPA', 'Oil in Watercolor: Oil Industry at War (Standard Oil of New Jersey)', 'Paintings, Watercolors, Sculpture and Drawings from the Collection of Mr. and Mrs. Henry Pearlman', 'Physician as Potter: Ceramics & Watercolors by Kiyonobu Kato', 'Robin S. Chase: Watercolors', 'Student Invitational Watercolor Exhibition', 'Summer Show of Oil Paintings, Water Colors and Drawings by American and Foreign Artists', 'T. Cavallaro: Watercolors', 'Tigers of Wrath: Watercolors by Walton Ford', 'Twenty Water Color Paintings', 'Water Color and Crayon Pictures of Field Work in Yellowstone Park by H.B. Tschudy', 'Water Colors & Work in the Graphic Media by Abraham Walkowitz; Drawings of Isadora Duncan by Walkowitz', 'Water Colors and Drawings by Albert H. Sonn', 'Water Colors and Illuminated Manuscripts by Arthur Szyk', 'Water Colors by Brooklyn Artists', 'Water Colors by Winslow Homer', 'Water Colors of North American Birds by R.I. Brasher', 'Watercolors & Prints by Angelo Longo & Robert Chapman', 'Watercolors and English Drawings of the 90s', 'Watercolors by Charles Martin & Drawings by Walter Barker', 'Watercolors by Fred Gutzeit', 'Watercolors by Irene Aunio', 'William Zorach: Paintings, Watercolors and Drawings, 1911-1922', 'Winslow Homer: Watercolors, Prints and Drawings']

while 'George Pearse Ennis & Paul Ludwig Gill: Memorial Exhibition of Water Colors' in all_exhibitions:
    all_exhibitions = find_and_replace(all_exhibitions,'George Pearse Ennis & Paul Ludwig Gill: Memorial Exhibition of Water Colors','George Pearse Ennis & Paul Ludwig Gill: Memorial Exhibition of Watercolors')

while 'International Watercolor Exhibition, 01st Biennial: Water Color Paintings by American Artists' in all_exhibitions:
    all_exhibitions = find_and_replace(all_exhibitions,'International Watercolor Exhibition, 01st Biennial: Water Color Paintings by American Artists','International Watercolor Exhibition, 01st Biennial: Watercolor Paintings by American Artists')

while 'International Watercolor Exhibition, 06th Biennial: Water Color Paintings, Pastels and Drawings by American and Foreign Artis...' in all_exhibitions:
    all_exhibitions = find_and_replace(all_exhibitions,'International Watercolor Exhibition, 06th Biennial: Water Color Paintings, Pastels and Drawings by American and Foreign Artis...','International Watercolor Exhibition, 06th Biennial: Watercolor Paintings, Pastels and Drawings by American and Foreign Artis...')

while 'Oil Paintings and Water Colors by California Artists. The Post-Surrealists' in all_exhibitions:
    all_exhibitions = find_and_replace(all_exhibitions,'Oil Paintings and Water Colors by California Artists. The Post-Surrealists','Oil Paintings and Watercolors by California Artists. The Post-Surrealists')

while 'Oil Paintings, Water Colors & Prints: WPA' in all_exhibitions:
    all_exhibitions = find_and_replace(all_exhibitions,'Oil Paintings, Water Colors & Prints: WPA','Oil Paintings, Watercolors & Prints: WPA')

while 'Summer Show of Oil Paintings, Water Colors and Drawings by American and Foreign Artists' in all_exhibitions:
    all_exhibitions = find_and_replace(all_exhibitions,'Summer Show of Oil Paintings, Water Colors and Drawings by American and Foreign Artists','Summer Show of Oil Paintings, Watercolors and Drawings by American and Foreign Artists')

while 'Twenty Water Color Paintings' in all_exhibitions:
    all_exhibitions = find_and_replace(all_exhibitions,'Twenty Water Color Paintings','Twenty Watercolor Paintings')

while 'Water Color and Crayon Pictures of Field Work in Yellowstone Park by H.B. Tschudy' in all_exhibitions:
    all_exhibitions = find_and_replace(all_exhibitions,'Water Color and Crayon Pictures of Field Work in Yellowstone Park by H.B. Tschudy','Watercolor and Crayon Pictures of Field Work in Yellowstone Park by H.B. Tschudy')

while 'Water Colors & Work in the Graphic Media by Abraham Walkowitz; Drawings of Isadora Duncan by Walkowitz' in all_exhibitions:
    all_exhibitions = find_and_replace(all_exhibitions,'Water Colors & Work in the Graphic Media by Abraham Walkowitz; Drawings of Isadora Duncan by Walkowitz','Watercolors & Work in the Graphic Media by Abraham Walkowitz; Drawings of Isadora Duncan by Walkowitz')

while 'Water Colors and Drawings by Albert H. Sonn' in all_exhibitions:
    all_exhibitions = find_and_replace(all_exhibitions,'Water Colors and Drawings by Albert H. Sonn','Watercolors and Drawings by Albert H. Sonn')

while 'Water Colors and Illuminated Manuscripts by Arthur Szyk' in all_exhibitions:
    all_exhibitions = find_and_replace(all_exhibitions,'Water Colors and Illuminated Manuscripts by Arthur Szyk','Watercolors and Illuminated Manuscripts by Arthur Szyk')

while 'Water Colors by Brooklyn Artists' in all_exhibitions:
    all_exhibitions = find_and_replace(all_exhibitions,'Water Colors by Brooklyn Artists','Watercolors by Brooklyn Artists')

while 'Water Colors by Winslow Homer' in all_exhibitions:
    all_exhibitions = find_and_replace(all_exhibitions,'Water Colors by Winslow Homer','Watercolors by Winslow Homer')

while 'Water Colors of North American Birds by R.I. Brasher' in all_exhibitions:
    all_exhibitions = find_and_replace(all_exhibitions,'Water Colors of North American Birds by R.I. Brasher','Watercolors of North American Birds by R.I. Brasher')

print(all_exhibitions)

with open('CDellebovi_WeeklyChallenge9_BKM_Functions.json', 'w') as f:
    f.write(json.dumps(sorted(set(all_exhibitions)),indent=4))
