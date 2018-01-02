
import re, ipaddress

IPV4_PATTERN = r'((?:\d{1,3}\.){3}\d{1,3})'
DELIMITER_PATTERN = r'(?:-|~|[Tt][Oo])'

def find_valid_ip(input):
    all_ips = re.findall(IPV4_PATTERN, input)
    ips_in_range = find_range_groups(input)

    for ip in all_ips:
        if not is_valid_ip(ip):
            all_ips.remove(ip)

    toReturn = ''
    print(ips_in_range)
    for ip in all_ips:
        for range_endpoints in ips_in_range:
            if ip in range_endpoints:
                range_index = all_ips.index(ip)
                toReturn += all_ips.pop(range_index) + '-' + all_ips.pop(range_index)
        if all_ips:
            toReturn += ' ' + all_ips.pop(0)
    print(toReturn)
    return toReturn


def is_valid_ip(address):
    try:
        ipaddress.IPv4Address(address)
        return True
    except ValueError:
        return False

def find_range_groups(input):
    address_range = IPV4_PATTERN + '\s*' + DELIMITER_PATTERN + '\s*' + IPV4_PATTERN
    address_range_endpoints = re.findall(address_range, input)
    return address_range_endpoints


find_valid_ip("127.0.0.9")
find_valid_ip('999.999.999.999')
find_valid_ip('127.0.0.3 999.999.999.999')
find_valid_ip('from 127.0.0.1 to 127.0.0.2')
find_valid_ip('from 127.0.0.1~ 127.0.0.2 127.0.0.3 999.999.999.999')
find_valid_ip('from 127.0.0.1~ 127.0.0.2 127.0.0.3 999.3.3.2-999.999.999.999')
