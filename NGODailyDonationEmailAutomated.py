import yagmail
import pandas as pd
from datetime import datetime, timedelta
import time


#Load data into dataframe
def content_to_send():
    
    filename = 'random_transactions.csv'
    df = pd.read_csv(filename)

    
    #Date Initialization
    today = datetime.now().date()
    yesterday = today - timedelta(days=3)
    print(yesterday)
    current_month_start = today.replace(day=1)

    #extract date from datetime
    df['date'] = pd.to_datetime(df['DateTime']).dt.date
    
    # filter dataframe to yesterday
    mask = df['date'] == yesterday


    #yesterday total transaction data extraction 
    transaction = df.loc[mask]
    yesterday_transaction_statement = "The total transaction value yesterday was " + str(transaction['Amount'].sum()) + "  in " + str(len(transaction)) + "  transactions by " + str(transaction['Name'].nunique()) + " clients."
    print(yesterday_transaction_statement)
    

    #yesterday total donation data extration 
    status = ['Donation']
    donation = transaction[transaction.TransactionType.isin(status)]
    yesterday_donation_statement = "The total donation value yesterday was " + str(donation['Amount'].sum()) + "  in " + str(len(donation)) + "  transactions by " + str(donation['Name'].nunique()) + " clients."
    print(yesterday_donation_statement)

    #yesterday top 5 donation campaigns table
    top_donation_campaign = donation.groupby('Campaign')['Amount'].sum()
    top_donation_campaign =top_donation_campaign.nlargest(5)
    top_donation_campaign = pd.DataFrame(top_donation_campaign)
    print(top_donation_campaign)
    

    #yesterday total membership data extration
    status = ['Membership']
    membership = transaction[transaction.TransactionType.isin(status)]
    yesterday_membership_statement = "The total membership value yesterday was " + str(membership['Amount'].sum()) + "  in " + str(len(membership)) + "  transactions by " + str(membership['Name'].nunique()) + " clients."
    print(yesterday_membership_statement)
    
    #yesterday top 5 membership campaigns table
    top_membership_campaign = membership.groupby('Campaign')['Amount'].sum()
    top_membership_campaign =top_membership_campaign.nlargest(5)
    top_membership_campaign = pd.DataFrame(top_membership_campaign)
    print(top_membership_campaign)


    #Monthly total transaction data extraction 
    mask = df['date'] >= current_month_start
    transaction = df.loc[mask]
    month_transaction_statement = "The total transaction value this month was " + str(transaction['Amount'].sum()) + "  in " + str(len(transaction)) + "  transactions by " + str(transaction['Name'].nunique()) + " clients."
    print(month_transaction_statement)

    return yesterday_transaction_statement, yesterday_donation_statement, yesterday_membership_statement, top_donation_campaign, top_membership_campaign, month_transaction_statement




# Set up yagmail
yag = yagmail.SMTP(user={'xxxxxxxxxxxx@gmail.com' : "NGO Analytics"}, password='xxxxxxxxxxxxx')

# Function to send email with content generated from content_to_send() function
def send_email_with_content():
    # Call content_to_send() function to generate content
    yesterday_transaction_statement, yesterday_donation_statement, yesterday_membership_statement, top_donation_campaign, top_membership_campaign, month_transaction_statement = content_to_send()

    # Convert DataFrames to HTML and remove extra spaces
    top_donation_campaign_html = top_donation_campaign.to_html(index=True).replace("\n", "")
    top_membership_campaign_html = top_membership_campaign.to_html(index=True).replace("\n", "")



    # Compose email
    subject = 'NGO Donation Analytics'
    contents =     contents = [f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NGO Donation Analytics</title>

    </head>
    <body style="margin: 0; padding: 0; font-family: Arial, sans-serif;">
    <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
        <tr>
            <td align="center" bgcolor="#f8f8f8">
                <table role="presentation" width="600" cellspacing="0" cellpadding="0" border="0" class="container">
                    <!-- Header -->
                    <tr>
                       
                       <td style="text-align: center;">
                       
                        <img src="image.png" alt="Header Image" style="max-width: 100%; height: auto;">
                            <h1 style="margin: 0;">NGO Daily Analytics</h1>
                        </td>
                    </tr>
                    <!-- Content -->
                    <tr>
                        <td bgcolor="#ffffff" style="padding: 20px;">
                            <p>Hello,</p>
                            <h3>Our analytics team has compiled a comprehensive report detailing fundraising key insights and outcomes from yesterday:</h3>
                            <p>{yesterday_transaction_statement}</p><br><br></p>
        

                            <h3>Donations:</h3>
                            <p>{yesterday_donation_statement}</p>
                            <p style="text-align: center;">{top_donation_campaign_html}</p><br><br>

                            <h3>Memberships:</h3>
                            <p>{yesterday_membership_statement}</p>
                            <p style="text-align: center;">{top_membership_campaign_html}</p><br><br>
                            
                            <h3>The Month So Far:</h3>
                            <p>{month_transaction_statement}</p>

                            <br><br></p>
                            <p>Regards,<br>Ola</p>
                        </td>
                    </tr>
                    <!-- Footer -->
                    <tr>
                        <td bgcolor="#333333" style="padding: 20px; color: #ffffff; text-align: center;">
                        <img src="image.png" style="max-width: 200px; height: auto;">
                            <p>&copy; 2024 Ola's Portfolio. All rights reserved.</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
    </body>
    </html>



    '''
        ]
    f = open("NGODonationEmailLog.txt", "a")
    # Send email and document status
    try:
        yag.send('olajide@gmail.ca', subject, contents)
        f.write(f" {datetime.now()}- Auto Script Executed and Email Sent \n")
        f.close()
    except:
        f.write(f" {datetime.now()}- Email Error \n")
        f.close()

        
# Call the function to send email
send_email_with_content()

