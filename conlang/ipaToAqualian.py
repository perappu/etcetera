import re

IPAkey = {
'm':'m',
'p':'p',
'b':'b',
'f':'f',
'v':'v',
'θ':'th',
'ð':'dh',
's':'s',
'z':'z',
'k':'k',
'g':'g',
'x':'x',
'l':'l',
'n':'n',
'ʃ':'sh',
'ʒ':'zh',
'ɲ':'gn',
'i':'ī',
'j':'j',
'd':'d',
't':'t',
'a':'a',
'ä':'ā',
'e':'ē',
'ɛ':'e',
'ɪ':'i',
'o':'ō',
'ɔ':'o',
'u':'ū',
'ʊ':'u',
'ɹ':'r',
'˙':'-'
}

cleanUp = {
'ee':'ē',
'ēē':'ē',
'ēe':'ē',
'eē':'ē',
'ēū':'ē',
'ēī':'ē',
'ēe':'ē',
'ēō':'ē',
'ēā':'ē',
'uu':'ū',
'ūū':'ū',
'ūu':'ū',
'uū':'ū',
'ūē':'ū',
'ūī':'ū',
'ūō':'ū',
'ūā':'ū',
'ii':'ī',
'īi':'ī',
'iī':'ī',
'īī':'ī',
'īē':'ī',
'īū':'ī',
'īō':'ī',
'īā':'ī',
'oo':'ō',
'ōō':'ō',
'ōo':'ō',
'oō':'ō',
'ōī':'ō',
'ōē':'ō',
'ōū':'ō',
'ōī':'ō',
'ōā':'ō',
'aa':'ā',
'āā':'ā',
'āa':'ā',
'aā':'ā',
'āī':'ā',
'āē':'ā',
'āū':'ā',
'āī':'ā',
'āō':'ā',
'll':'dd',
'tt':'dd'
}

illegalList = ['bs','cs','dl','ds','ns','ls','rs','fs','vs','ps','ms','ts','js']

print(IPAkey)

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text
    
with open('output.txt', 'w', encoding='utf-8') as f1:
    for line in open('wordlist.txt',encoding='utf-8'):
        newWord = replace_all(line,IPAkey)
        newWord = replace_all(newWord,cleanUp)
        if not any(sub in newWord for sub in illegalList):
            f1.write(newWord)