badWords = {
    "shpx": "",
    "shx": "",
    "shpxvat": "",
    "shpxre": "",
    "ovgpu": "",
    "fuvg": "",
    "fuvggl": "",
    "qnza": "",
    "qnzzvg": "",
    "pbpx": "",
    "nff": "",
    "nffubyr": "",
    "phpx": "",
    "qvpx": "",
    "tbqqnza": "",
    "onfgneq": "",
    "uryy": "",
    "phag": "",
    "chffl": "",
    "snttbg": "",
    "avttre": "",
    "avttn": "",
    "tgsb": "",
    "zbgure shpxre": "",
    "jgs": "",
    "cravf": "",
    "obbo": "",
    "intvan": "",
}

decryptionKey = {
    "a":"n",
    "b":"o",
    "c":"p",
    "d":"q",
    "e":"r",
    "f":"s",
    "g":"t",
    "h":"u",
    "i":"v",
    "j":"w",
    "k":"x",
    "l":"y",
    "m":"z",
    "n":"a",
    "o":"b",
    "p":"c",
    "q":"d",
    "r":"e",
    "s":"f",
    "t":"g",
    "u":"h",
    "v":"i",
    "w":"j",
    "x":"k",
    "y":"l",
    "z":"m",
    " ":" "
}

encryptionKey = {v: k for k, v in decryptionKey.items()}

def decrypt(str):
    res = ""
    for c in str:
        res += decryptionKey[c]
    return res

def encrypt(str):
    res = ""
    for c in str:
        res += encryptionKey[c]
    return res

def add(str):
    encrypted = encrypt(str)
    badWords[encrypted] = ""

for entry in badWords.keys():
    print(decrypt(entry))

