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

# create regex for phone numbers and email addresses
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                          # first 3 digits
    (\s|-|\.)                        # separator
    (\d{4})                          # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)''', re.VERBOSE)
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # username
    @                               # @ symbol
    [a-zA-Z0-9.-]+                  # domain name
    (\.[a-zA-Z]{2,4})               # dot-something
)''', re.VERBOSE)

# get text from clipboard
text = pyperclip.paste()

# extract phone numbers and email addresses from text
extracted_phone_numbers = phone_regex.findall(text)
