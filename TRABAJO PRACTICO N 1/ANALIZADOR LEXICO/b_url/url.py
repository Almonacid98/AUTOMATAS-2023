import re

url = re.compile("^(https?://)+(www\.)+([a-zA-Z0-9.-])+\.(com|es|ar|net|org|um\.edu\.ar|edu\.ar|edu\.com|edu\.org|cl|co|cn|ae|au|br|ca|nz)+\.(ar|cl|co|cn|ae|au|br|ca|nz|es)$")

print("VALIDACION DE URL, PUNTO B")
agregarurl = [input("INGRESE LA URL: " u'')]

for pagina in agregarurl:
    match = url.search(pagina)
    if match:
        print('{:<30}  {}'.format(pagina, 'URL INGRESADA CORRECTAMENTE'))
    else:
        url = re.compile("^(www\.)+([a-zA-Z0-9.-])+\.(com|es|ar|net|org|um\.edu\.ar|edu\.ar|edu\.com|edu\.org|cl|co|cn|ae|au|br|ca|nz)+\.(ar|cl|co|cn|ae|au|br|ca|nz|es)$")
        for pagina in agregarurl:
            match = url.search(pagina)
            if match:
                print('{:<30}  {}'.format(pagina, 'URL INGRESADA CORRECTAMENTE'))
            else:
                url = re.compile("^([a-zA-Z0-9.-])+\.(com|es|co|ar|net|org|edu\.ar|um\.edu\.ar|edu\.com|edu\.org|cl|co|cn|ae|au|br|ca|nz)+\.(ar|cl|co|cn|ae|au|br|ca|nz|es)$")
                for pagina in agregarurl:
                    match = url.search(pagina)
                    if match:
                        print('{:<30}  {}'.format(pagina, 'URL INGRESADA CORRECTAMENTE'))
                    else:
                        print('{:<30} {}'.format(pagina, 'URL INVALIDA'))