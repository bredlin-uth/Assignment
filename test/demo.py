import re


def split_string(input_string):
    # Use regular expression to split the string at the first apostrophe
    parts = re.split(r"[’']", input_string)

    # Strip leading and trailing spaces from each part
    parts = [part.strip() for part in parts]

    return parts

print(split_string("How will South India's first double-decker flyover in Bengaluru ease traffic?")[-1])