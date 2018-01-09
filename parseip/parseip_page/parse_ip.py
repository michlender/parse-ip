
import re, ipaddress

IPV4_PATTERN = r'((?:\d{1,3}\.){3}\d{1,3})'
DELIMITER_PATTERN = r'(?:-|~|[Tt][Oo])'

def find_valid_ip(input):
    all_ips = re.findall(IPV4_PATTERN, input)
    ips_in_range = find_range_groups(input)
    individual_ips = []
    valid_ips = []
    invalid_ips = []
    valid_ranges = []
    invalid_ranges = []

    # Validate IP addresses
    for ip in all_ips:
        if is_valid_ip(ip):
            valid_ips.append(ip)
        else:
            invalid_ips.append(ip)

    # Build list of individual IP addresses
    for ip in valid_ips:
        is_individual = True
        for range_endpoints in ips_in_range:
            if ip in range_endpoints:
                is_individual = False
        if is_individual:
            individual_ips.append(ip)

    # Build lists of valid and invalid ranges
    for range_endpoints in ips_in_range:
        start = range_endpoints[0]
        end = range_endpoints[1]
        if not is_valid_ip(start) or not is_valid_ip(end):
            invalid_ranges.append(range_endpoints)
        else:
            valid_ranges.append(range_endpoints)

    print('All IPs')
    print(all_ips)
    print('Individuals')
    print(individual_ips)

    print('Valid')
    print(valid_ips)
    print('Invalid')
    print(invalid_ips)

    print('Ranges')
    print(ips_in_range)
    print('Valid Ranges')
    print(valid_ranges)
    print('Invalid Ranges')
    print(invalid_ranges)


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


# find_valid_ip("127.0.0.9")
# find_valid_ip('999.999.999.999')
# find_valid_ip('127.0.0.3 999.999.999.999')
# find_valid_ip('from 127.0.0.1 to 127.0.0.2')
# find_valid_ip('from 127.0.0.1~ 127.0.0.2 127.0.0.3 999.999.999.999')
find_valid_ip('from 127.0.0.1~ 127.0.0.2 127.0.0.3 999.3.3.2-999.999.999.999')
