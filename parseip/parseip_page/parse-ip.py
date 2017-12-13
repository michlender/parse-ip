
import re

toReturn = ''
#address_catch_ipv4 = '((\d+\.*){4})'
address_catch_ipv4 = '((\d{1,3}\.){3}\d{1,3})'


def find_valid_ip(input):
    possible_ips = re.compile(address_catch_ipv4)
    found_ips = re.findall(possible_ips, input)

    for ips in found_ips:
        print(ips[0])
        if (validate_ip(ips[0])):
            return True
            #is_in_range

def validate_ip(ipaddress):
    segments = ipaddress.split('.')
    if (len(segments) != 4):
        return False
    for segment in segments:
        if int(segment) >= 256:
            return False
    return True

def is_in_range(input):
    delimiter = re.compile('-|~|[Tt][Oo]')



    #if found_ips != None:
        #toReturn += found_ips.group()
    #else:
        #toReturn = 'No IP addresses found.'

    #input = input[found_ip.end():]

    #print(toReturn)
    #if is_in_range(input):
    #    toReturn += '-'
    #else:
    #    toReturn += ' '



#def parse_ip(input):

find_valid_ip('from 127.0.0.1')
find_valid_ip("127.0.0.9")
