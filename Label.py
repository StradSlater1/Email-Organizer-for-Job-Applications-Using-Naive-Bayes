import pandas as pd
import random

df = pd.read_csv('emails.csv')
print(len(df))
df = df.dropna()
print(len(df))

email_list = df['email'].to_list()
email_list_shorten = random.sample(email_list, 1000)

outcomes = []

for email in email_list_shorten:
    print(email)
    outcome = input('Job?: ')
    outcomes.append(outcome)

print(outcomes)

data = {'email' : email_list_shorten,
        'outcome' : outcomes}

new_df = pd.DataFrame(data)
new_df.to_csv('email_outcome.csv')

print(len(email_list_shorten))
print(len(outcomes))


