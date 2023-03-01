
import sys
from os import path, remove

out_file_name = "anon_out.txt"
# create an anon_in.txt and dump in all emails
# python anonymiser.py anon_in.txt
# emp-website run -a web-backend-internal "django-admin anonymize_user --email <email_addresses>"

def check_and_delete_out_file():
    out_file = path.exists(out_file_name)
    print ("File exists:" + str(out_file))
    if out_file:
        print (f"Deleting old {out_file_name}...")
        remove(out_file_name)

def get_from_in_file():
    email_list =[]
    with open(sys.argv[1]) as f:
        for line in f:
            email_list.append(line.rstrip())
    email_list = list(dict.fromkeys(email_list))
    return email_list

def write_out_file(email_list):
    try:
        joined_string = " ".join(email_list)
        f = open(out_file_name, "a")
        f.write(joined_string)
        return True
    except:
        return False

def main():
    if len(sys.argv) != 2:
        print("No file given. Please specify an input file")
        return []
    check_and_delete_out_file()
    email_list = get_from_in_file()
    if len(email_list) > 0:
        if write_out_file(email_list):
            print(f"Success {out_file_name} generated with {len(email_list)} unique emails")
        else:
            print("error")


main()