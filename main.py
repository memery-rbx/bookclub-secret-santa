import pandas as pd
from math import isnan

def create_secret_santa_emails(df):
    emails = []

    for i in range(len(df)):
        current_participant = df.iloc[i]
        next_participant = df.iloc[(i + 1) % len(df)]  # Loop back to first for the last participant

        # Email content
        email_subject = "Book Club Secret Santa Information"
        email_body = f"""
Dear {current_participant['What is your name?']},

You have been selected to be the Secret Santa for {next_participant['What is your name?']}!

Here is some information to help you choose a gift:
- Book Preferences: {next_participant['Describe the types of books you would like to read']}
- Favorite Recent Read: {next_participant["What's your favorite recent read?"]}
- Preferred Book Format: {next_participant['How do you prefer to receive a gifted book?']}"""

        if isinstance(next_participant['[Optional]: If you have a GoodReads/StoryGraph URL. Post it here'], str):
            email_body = '\n'.join([email_body, f"- Optional Goodreads/StoryGraph URL: {next_participant['[Optional]: If you have a GoodReads/StoryGraph URL. Post it here']}"])

        if isinstance(next_participant['If requested something other than a hard copy book, what email should the book be sent to?'], str):
            email_body = '\n'.join([email_body, f"- Personal email for e-gifts: {next_participant['If requested something other than a hard copy book, what email should the book be sent to?']}"])

        final_message = """You should have a new Brex spending limit of $50 to purchase your gift.
        
Please note that the gift should be a surprise, so keep it secret!

Happy gifting,

Matt
        """

        email_body = '\n\n'.join([email_body, final_message])

        emails.append((current_participant['Company Email'], email_subject, email_body))

    return emails


if __name__ == '__main__':
    file_path = 'data/book-club-secret-santa2024.csv'
    bookclub_df = pd.read_csv(file_path)
    secret_santa_emails = create_secret_santa_emails(bookclub_df)

    for email in secret_santa_emails:
        print(email[0])
        print(email[1])
        print(email[2])
