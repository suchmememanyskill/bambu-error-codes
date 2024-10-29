import os, shutil, json

if os.path.exists("./_site"):
    shutil.rmtree("./_site")

os.mkdir("./_site")

with open("codes.json") as fp:
    data = json.load(fp)

for code in data:
    with open(f"./_site/{code}.html", "w") as fp:
        fp.write(data[code])

    with open(f"./_site/{code}", "w") as fp:
        fp.write(data[code])