from operator import ne
import bs4

text = open('index.html', 'r', encoding='utf16').read()

soup = bs4.BeautifulSoup(text)

def readContentsRecursive(content):
    for content2 in content.contents:
        if (type(content2) == bs4.element.Tag):
            readContentsRecursive(content2)
        elif (type(content2) == bs4.element.NavigableString):
            new_tag = soup.new_tag("span")
            words = content2.split()
            for word in words:
                if len(word) != 1:
                    half = round(len(word)/2)
                    btag = soup.new_tag('b')
                    btag.append(word[0:half])
                    new_tag.append(btag)
                    new_tag.append(word[half:len(word)])
                else:
                    new_tag.append(word)
                new_tag.append(' ')
            content2.string.replace_with(new_tag)
            pass
    pass

for ptag in soup.find_all('p'):
    if (type(ptag.contents) == list):
        for content in ptag.contents:
            if (type(content) == bs4.element.Tag):
                readContentsRecursive(content)
            elif (type(content) == bs4.element.NavigableString):
                pass

open("output1.html", "w", encoding='utf16').write(str(soup))
pass