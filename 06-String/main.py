# Import
import re

# Regex object
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

# Match object
match_object = phone_num_regex.search('My number is 415-555-4242.')

print(f'Complete match: {match_object.group()} or {match_object.group(0)}')
# Complete match: 415-555-4242 or 415-555-4242
print(f'Group matches: {match_object.group(1)} or {match_object.group(2)}')
# Group matches: 415 or 555-4242

print(f'group list: {match_object.groups()}')