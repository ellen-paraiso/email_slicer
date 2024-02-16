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
    # Convert to set to remove duplicates, then back to list
    unique_emails = list(set(emails))  
    
    if unique_emails:
        print("Found the following unique email addresses:")
        for email in unique_emails:
            print(email)
    else:
        print("No email addresses found.")


if __name__ == "__main__":
    main()