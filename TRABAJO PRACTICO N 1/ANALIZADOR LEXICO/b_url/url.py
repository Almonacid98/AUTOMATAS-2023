import re
url = re.compile("^(https?://)+(www\.)+([a-zA-Z0-9.-])+\.(com|ar|net|org|edu\.ar|edu\.com|edu\.org)$")

print("VALIDACION DE URL, PUNTO B")
agregarurl = [input("INGRESE LA URL: " u'')]

for pagina in agregarurl:
    match = url.search(pagina)
    print('{:<30}  {}'.format(pagina, 'URL INGRESADA CORRECTAMENTE' if match else 'URL INVALIDA'))