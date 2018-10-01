"""
This program gets Wildcard of the given ip address in CIDR notation
"""

import requests
import json

"""
Get the wildcard of the given IP adress
"""

def getWildcard(ip):
    link = "https://uploadbeta.com/api/ipcalc/?cached&s=" + ip
    response = requests.get(link)
    parsed_json = json.loads(response.text)
    print(parsed_json)
    s =""
    for i in range (149,170):
        s +=parsed_json[i]
    final = s.replace(" ", "")
    print(final)
    return final


"""
Makes a text file with output.txt and outputs wildcard
"""

def fileBuilder(ip):
    ab = ip.find("/")
    modifiedIp = ip[:ip.find("/")]
    finalString = "The wildcard for the IP " + modifiedIp + " is- " + getWildcard(ip) + "\n"
    f = open("output.txt", "a+")
    f.write(finalString)


"""
Takes input of a text file named input.txt with ip addresses in 
every new line
"""

def main():
    fname = "input.txt" # sample input ip/[1-32] i.g- 8.8.8.8/20
    with open(fname) as f:
        content = f.readlines()
    finalList = []
    for i in content:
        a = i.replace("\n", "")
        finalList.append(a)
    print(finalList)
    for b in finalList:
        fileBuilder(b)


main()
