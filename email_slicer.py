import re

def extract_emails(text):
    # Regular expression pattern for matching email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # Finding all occurrences of the pattern
    emails = re.findall(email_pattern, text)
    
    return emails

def main():
    # Asking for user input
    text = input("Enter a sentence or paragraph: ").strip()
    
    # Extracting emails
    emails = extract_emails(text)
    
    if emails:
        print("Found the following email addresses:")
        for email in emails:
            print(email)
    else:
        print("No email addresses found.")

if __name__ == "__main__":
    main()