"""
Emails
Estimate: 40 minutes
Actual: 45 minutes
"""

def main():
    """Prompt user for emails, extract and confirm names, and display a sorted list of names and emails."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n): ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    #Decided to try reuse this formatting trick, sorts alphabetically and list in line
    width = max(len(name) for name in email_to_name.values())
    for email, name in sorted(email_to_name.items()):
        print(f"{name:{width}} ({email})")


def extract_name_from_email(email):
    """Split the email at @, split the names at '.' and returns a title cased name"""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = (" ".join(parts).title())
    return name

main()