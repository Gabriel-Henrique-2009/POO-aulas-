entrada = input("digite a palavra: ")

alfabeto = {"a": "a",
"b": "bac",
"c": "cad",
"d": "def",
"e": "e",
"f": "feg",
"g": "geh",
"h": "hij",
"i": "i",
"j": "jik",
"k": "kil",
"l": "lim",
"m": "mon",
"n": "nop",
"o": "o",
"p": "poq",
"q": "qor",
"r": "ros",
"s": "sut",
"t": "tuv",
"u": "u",
"v": "vux",
"x": "xuz",
"z": "zuz"}

codigo = ""
letra = ""
for l in entrada:
    letra = alfabeto[l]
    codigo = codigo + "" + letra
print(codigo)
    
