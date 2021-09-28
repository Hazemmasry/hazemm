import json
import urllib.request


def filterString(st):
    st = str.replace(st, "\u0101", "*")
    st = str.replace(st, "\u014d", "*")
    st = str.replace(st, "\xe1", "*")
    st = str.replace(st, "\xf3", "*")
    st = str.replace(st, "\xf1", "*")
    st = str.replace(st, "\xed", "*")
    st = str.replace(st, "\u012b", "*")
    st = str.replace(st, "\u0131", "*")
    st = str.replace(st, "\u012b", "*")
    st = str.replace(st, "\xfd", "*")
    return st


def printResults(data):
    theJSON = json.loads(data)
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])
        count = theJSON["metadata"]["count"]
        print(str(count) + " events recorded")

        for i in theJSON["features"]:
            x = filterString(str(i["properties"]["place"]))
            print(x)
    # if(i["properties"]["place"]):
    #     print(i["properties"]["place"])
    # else:
    #     print("****")


print("----------------\n")


def main():
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"
    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()))
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        # print(data)
        printResults(data)
    else:
        print("error")


if __name__ == '__main__':
    main()
