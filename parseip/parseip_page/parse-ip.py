
import re

toReturn = ''
#address_range = '^(12[0-7]|1[01]\d|\d\d|\d|0?\d?\d)$'
#address_range = '^(0?\d?\d|1[01]\d|12[0-7])$'
#address_range = '^(\d?\d|1[01]\d|12[0-7])$'
#address_range = '^(\d|\d\d|1[01]\d|12[0-7])$'
#address_range = '^(\d?\d?\d|1[01]\d|12[0-7])$'
address_range = '^(0?[0-9]?[0-9]|1[01][0-9]|12[0-7])$'

def find_valid_ip(input):
    #valid_ip = re.compile('^[0-127].[0-127].[0-127].[0-127]$')
    #valid_ip = re.compile('^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$')
    #valid_ip = '^(\d|\d\d|1[01]\d|12[0-7].\d|\d\d|1[01]\d|12[0-7].\d|\d\d|1[01]\d|12[0-7].\d|\d\d|1[01]\d|12[0-7])$'
    valid_ip = re.compile('^(' + address_range + '.' + address_range + '.' + address_range + '.' + address_range + ')$')
    found_ip = valid_ip.search(input)

    if found_ip != None:
        toReturn += found_ips.group()
    else:
        toReturn = 'No IP addresses found.'

    #input = input[found_ip.end():]

    print(toReturn)
    #if is_in_range(input):
    #    toReturn += '-'
    #else:
    #    toReturn += ' '

def is_in_range(input):
    delimiter = re.compile('-|~|[Tt][Oo]')

#def parse_ip(input):

find_valid_ip("from 127.0.0.1")
find_valid_ip("127")
