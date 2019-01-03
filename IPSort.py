import struct
from socket import inet_aton, inet_ntoa


"""IP to Long"""
def ip2long(ip):
  packed = inet_aton(ip)
  lngi = struct.unpack("!L", packed)[0]
  return lngi


"""Long to IP"""
def long2ip(lng):
  packed = struct.pack("!L", lng)
  ip=inet_ntoa(packed)
  return ip


"""
Takes a comma seperated unsorted IP address, and prints them out in a list of sorted IP
"""

def main():
    fname = "input.txt"
    with open(fname) as f:
        for line in f:
          content= line.strip()
          content = content.replace(" ", "")
    # print (content)
    list_comma = content.split(",")

    # Expected input = ip/subnet, i.e 192.168.0.0/24
    ipNumberCleaned = []
    for i in list_comma:
      ab = i.find("/")
      modifiedIp = i[:i.find("/")] 
      ipNumberCleaned.append(modifiedIp)   
    
    longNumber = []
    for n in ipNumberCleaned:
      longNumber.append(ip2long(n))
    # print(longNumber)
    longNumber.sort()
    finalIp =[]
    for l in longNumber:
      finalIp.append(long2ip(l))

    
if __name__ == "__main__":
    main()
