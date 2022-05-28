from operator import ne
import bs4

text = open('index.html', 'r', encoding='utf16').read()

soup = bs4.BeautifulSoup(text)

pre = "<b>"
post = "</b>"


def readContentsRecursive(content):
    for content2 in content.contents:
        if (type(content2) == bs4.element.Tag):
            readContentsRecursive(content2)
        elif (type(content2) == bs4.element.NavigableString):
            bionicWords = []
            new_tag = soup.new_tag("span")
            words = content2.split()
            for word in words:
                if len(word) != 1:
                    half = round(len(word)/2)
                    # bionicWord = pre + word[0:half] + post + word[half:len(word)]
                    # bionicWords.append(bionicWord)
                    btag = soup.new_tag('b')
                    btag.append(word[0:half])
                    new_tag.append(btag)
                    new_tag.append(word[half:len(word)])
                    # new_tag.append(word[0:half])
                else:
                    new_tag.append(word)
                new_tag.append(' ')
                # bionic = ' '.join(bionicWords)
            # new_tag.string = "example.net"
            content2.string.replace_with(new_tag)
            pass
    pass

for ptag in soup.find_all('p'):
    if (type(ptag.contents) == list):
        for content in ptag.contents:
            if (type(content) == bs4.element.Tag):
                # print ('ok2')
                readContentsRecursive(content)
            elif (type(content) == bs4.element.NavigableString):
                pass
                # content.string.replace_with('mkmkmk')
                # print ('ok')

open("output1.html", "w", encoding='utf16').write(str(soup))
pass