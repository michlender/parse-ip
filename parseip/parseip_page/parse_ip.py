
import re, ipaddress


address_catch_ipv4 = '((?:\d{1,3}\.){3}\d{1,3})'
delimiter = '(?:-|~|[Tt][Oo])'

def find_valid_ip(input):
    individual_ip = re.compile(address_catch_ipv4)
    all_ips = re.findall(individual_ip, input)
    ips_in_range = is_in_range(input)

    for ip in all_ips:
        if not validate_ip(ip):
            all_ips.remove(ip)

        # for ranges in ips_in_range:
        #     if not any(ip in range_ip for range_ip in ranges):
        #         print('cool')
        #     else:
        #         print('uncool')

    toReturn = ''
    print(ips_in_range)
    for ip in all_ips:
        for ranges in ips_in_range:
            if ip in ranges:
                range_index = all_ips.index(ip)
                toReturn += all_ips.pop(range_index) + '-' + all_ips.pop(range_index)
        if all_ips:
            toReturn += ' ' + all_ips.pop(0)
    print(toReturn)
    return toReturn


def validate_ip(address):
    try:
        ipaddress.IPv4Address(address)
        return True
    except ValueError:
        return False

def is_in_range(input):
    address_range = re.compile(address_catch_ipv4 + '\s*' + delimiter + '\s*' + address_catch_ipv4)
    address_ranges = re.findall(address_range, input)
    return address_ranges


find_valid_ip("127.0.0.9")
find_valid_ip('999.999.999.999')
find_valid_ip('127.0.0.3 999.999.999.999')
find_valid_ip('from 127.0.0.1 to 127.0.0.2')
find_valid_ip('from 127.0.0.1~ 127.0.0.2 127.0.0.3 999.999.999.999')
find_valid_ip('from 127.0.0.1~ 127.0.0.2 127.0.0.3 999.3.3.2-999.999.999.999')
