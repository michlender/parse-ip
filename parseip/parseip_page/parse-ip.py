
import re, ipaddress

toReturn = ''
#address_catch_ipv4 = '((\d+\.*){4})'
address_catch_ipv4 = '((\d{1,3}\.){3}\d{1,3})'


def find_valid_ip(input):
    possible_ips = re.compile(address_catch_ipv4)
    found_ips = re.findall(possible_ips, input)

    for ips in found_ips:
        print('Caught the address: ' + ips[0])
        if (validate_ip(ips[0])):
            return True
            #is_in_range

def validate_ip(address):
    try:
        ipaddress.ip_address(address)
        print(address + ' is valid.')
        return True
    except ValueError:
        print('Invalid IP address.')
        return False

def is_in_range(input):
    # regular expression
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
find_valid_ip('999.999.999.999')
