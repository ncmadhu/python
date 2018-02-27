# Author: Madhu Chakravarthy
# Date: 09-01-2018

def decode(string):
    output = ""

    for char in string:
        asciiValue = ord(char)
        if asciiValue >= 97 and asciiValue <=122:
            newAsciiValue = asciiValue + 2
            if newAsciiValue >= 123:
                newAsciiValue = newAsciiValue - 122 + 96
            output += chr(newAsciiValue)
        else:
            output += char
    return output



if __name__ == "__main__":

    test = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

    print decode(test)
