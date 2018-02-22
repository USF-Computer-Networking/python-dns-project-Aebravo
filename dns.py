import socket

#!/usr/bin/env python

"""dns.py: prints a proper dns query response."""

__author__      = "Angelo Bravo, 'HowCode': https://www.youtube.com/watch?v=HdrPWGZ3NRo&list=PLBOh8f9FoHHhvO5e5HF_6mYvtZegobYX2"




port = 53 #by default, DNS operates on port 53

ip = '127.0.0.1' #loopack IP address

#creating a socket object with a UDP connection
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, port)) #binding the socket to the ip address and port we want to utilize



def buildresponse(data) :

    TransactionID = data[:2] #get bytes from 0-2 index

    TID = ''
    for byte in TransactionID:
         TID += hex(byte)[2:]

    print('Transaction ID: ', TID)

    Flags = getflags(data[2:4]) #Passing in 3th and 4th bytes
    QDCOUNT = b'\x00\x01'

    getquestdomain(data[12:])


def getflags(flags) :

    byte1 = flags[:1]
    byte2 = flags[1:2]

    rflags = ''

    QR = '1'

    OPCODE = ''
    for bit in range(1,5):
        OPCODE += str(ord(byte1)&(1<<bit)) #Check each bit in first byte through a for loop  by using the & function which returns either 1 if both compared values are 1 or 0

    AA = '1'
    TC = '0'
    RD = '0'
    RA = '0'
    Z = '000'
    RCODE = '0000'

    flags = int(QR + OPCODE + AA + TC + RD, 2).to_bytes(1, byteorder = 'big') + int(RA + Z + RCODE, 2).to_bytes(1, byteorder = 'big')
    print('Flags: ', flags)

def getquestdomain(data) :
    checkedLength = False #Will change boolean to true after we get length of domain string name
    expectedlength = 0
    domainstring = ''
    domainparts = [] #This will hold both the domain name and the tld
    x = 0
    y = 0
    for byte in data:
        if checkedLength == True:
            domainstring += chr(byte) #convert byte to chars (These bytes contain the domain name)
            x += 1
            if x == expectedlength: # we break the loop once we reach the end of the domain name in order to use the same function to get the tld
                domainparts.append(domainstring)
                domainstring = ''
                checkedLength = False
                x = 0
            if byte == 0:
                domainparts.append(domainstring)
                break
        else:
            checkedLength = True
            expectedlength = byte


        y += 1 #we use this parameter which does not reset to the get the questiontype

        questiontype = data[y+1:y+3]

    print('Domain Parts: ', domainparts)
    print('Question Type: ', questiontype)


#infinite loop keep programming running forever, allowing for it to listen to requests
while 1:
    data, addr = sock.recvfrom(512) #returns tuple of data and address from 512 bytes or less
    response = buildresponse(data) #build a response
    response