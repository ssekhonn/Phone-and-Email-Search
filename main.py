'''
pseudocode:
1. import re and pyperclip
2. create regex for phone numbers and email addresses
3. get text from clipboard
4. extract phone numbers and email addresses from text
5. join extracted phone numbers and email addresses into a string with newlines in between
6. copy the extracted phone numbers and email addresses back to the clipboard
'''

import re
import pyperclip

# create regex for phone numbers
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)''', re.VERBOSE)

# create regex for email addresses
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # username
    @                               # @ symbol
    [a-zA-Z0-9.-]+                  # domain name
    (\.[a-zA-Z]{2,4})               # dot-something
)''', re.VERBOSE)

# get text from clipboard
text = pyperclip.paste()

# extract phone numbers and email addresses
extracted_phone_numbers = phone_regex.findall(text)
extracted_email_addresses = email_regex.findall(text)

# clean extracted phone numbers
extracted_phone_numbers = [phone[0] for phone in extracted_phone_numbers]

# clean extracted email addresses
extracted_email_addresses = [email[0] for email in extracted_email_addresses]

# combine results into one string
results = '\n'.join(
    extracted_phone_numbers + extracted_email_addresses
)

# copy results back to clipboard
pyperclip.copy(results)

# print results to screen
print("Copied to clipboard:")
print(results)
