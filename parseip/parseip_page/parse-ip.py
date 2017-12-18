
import re, ipaddress

toReturn = ''
#address_catch_ipv4 = '((\d+\.*){4})'
address_catch_ipv4 = '((\d{1,3}\.){3}\d{1,3})'
delimiter = '(-|~|[Tt][Oo])'


def find_valid_ip(input):
    individual_ip = re.compile(address_catch_ipv4)
    all_ips = re.findall(individual_ip, input)
    ips_in_range = is_in_range(input)
    print(all_ips)


    for ips in all_ips:
        print(ips)
        #print('Caught the address: ' + ips[0])
        #if (validate_ip(ips[0])):
            #return True
            #is_in_range


def validate_ip(address):
    try:
        ipaddress.IPv4Address(address)
        print(address + ' is valid.')
        return True
    except ValueError:
        print('Invalid IP address.')
        return False

def is_in_range(input):
    address_range = re.compile(address_catch_ipv4 + '\s*' + delimiter + '\s*' + address_catch_ipv4)
    address_ranges = re.findall(address_range, input)

    for address in address_ranges:
        print(address)


# find_valid_ip('from 127.0.0.1')
# find_valid_ip("127.0.0.9")
# find_valid_ip('999.999.999.999')
# find_valid_ip('from 127.0.0.1 to 127.0.0.2')
find_valid_ip('from 127.0.0.1~ 127.0.0.2 127.0.0.3')
