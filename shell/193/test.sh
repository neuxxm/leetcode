# Read from the file file.txt and output all valid phone numbers to stdout.
#22:14-22:33
grep -E "^\([0-9]{3}\)\s[0-9]{3}\-[0-9]{4}$|^[0-9]{3}\-[0-9]{3}\-[0-9]{4}$" file.txt
