import os

fileList = os.listdir("docs/")
writeList = ""

with open("internal/listTemplate.html", "r") as f:
    template = f.read()

for i in fileList:
    writeList = writeList + f'<a href="docs/{i}"><h2>{i.removesuffix(".html")}</h2></a>\n'
    print(writeList)

with open("browser.html", "w") as f:
    template = template.replace("#CONTENT", writeList)
    f.write(template)