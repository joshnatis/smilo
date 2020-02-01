import requests
import hashlib
import time
import os

def main():
    url = "https://thispersondoesnotexist.com/image"
    desired_amt = int(input("How many images would you like? "))

    n = 0
    while n < desired_amt:
        picture = requests.get(url, headers={'User-Agent': 'o3 User Agent v1.0'}).content

        filename = checksum(picture) + ".jpg"

        #checksum is unique, duplicate files won't be saved
        if os.path.exists(filename):
            continue

        with open(filename, "wb") as f:
            f.write(picture)
            n+=1

        #time.sleep(0.3) #don't spam their poor servers

    clean()


def checksum(picture):
    h = hashlib.new("md5")
    h.update(picture)
    return h.hexdigest()

def clean():
    dirname = "pics"
    if not os.path.isdir("./" + dirname):
        os.mkdir(dirname)

    n = len([file for file in os.listdir(dirname)])
    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".jpg"):
            os.system("mv " + filename + " ./" + dirname + "/img" + str(n) + ".jpg")
            n+=1

main()
