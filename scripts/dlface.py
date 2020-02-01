# http://app.visgraf.impa.br/media/faces/thumbnails/s001/s001-01_img.jpg
# faces: s001 - s038
# 00 - neutral frontal
# 01 - joy
# 02 - sadness
# 03 - surprise
# 04 - anger
# 05 - disgust
# 06 - fear

import time
import wget

baseurl = "http://app.visgraf.impa.br/media/faces/thumbnails/"

# model < 10
for x in range(1,10):
    for y in range(1,4):
        url = baseurl + "s00" + str(x) + "/s00" + str(x) + "-0" + str(y) + "_img.jpg"
        wget.download(url, "/Users/sloh/workspace/facedb/" + "s00" + str(x) + "-0" + str(y) + "_img.jpg")
        time.sleep(0.1)

#model # >= 10
for x in range(10,39):
    for y in range(1,4):
        url = baseurl + "s0" + str(x) + "/s0" + str(x) + "-0" + str(y) + "_img.jpg"
        wget.download(url, "/Users/sloh/workspace/facedb/" + "s0" + str(x) + "-0" + str(y) + "_img.jpg")
        time.sleep(0.1)

