import pandas as pd
import matplotlib.pyplot as plt

file_path = "/content/sample_data/DATA1.csv"
df = pd.read_csv(file_path)

def clean_and_extract_number(value):
    if pd.isna(value):
        return 0
    elif '-' in value:
        # Extract the second number in fields like (601-650)
        return int(value.split('-')[1])
    elif '=' in value or '+' in value:
        # Ignore '=' and '+' signs and handle non-numeric characters
        cleaned_value = ''.join(char for char in value[1:] if char.isdigit())
        return int(cleaned_value) if cleaned_value else 0
    else:
        return int(value)

df['RANK 23'] = df['RANK 23'].apply(clean_and_extract_number)
df['RANK 24'] = df['RANK 24'].apply(clean_and_extract_number)

total_records = len(df)
print(f"Total number of records in the database: {total_records}")

arab_countries = [
    'Algeria', 'Bahrain', 'Comoros', 'Djibouti', 'Egypt', 'Iraq', 'Jordan', 'Kuwait',
    'Lebanon', 'Libya', 'Mauritania', 'Morocco', 'Oman', 'Palestinian Territory, Occupied', 'Qatar', 'Saudi Arabia',
    'Somalia', 'Sudan', 'Syrian Arab Republic', 'Tunisia', 'United Arab Emirates', 'Yemen'
]

arab_universities = df[df['Location'].isin(arab_countries)]
total_arab_universities = len(arab_universities)
print(f"Total number of universities in Arab countries: {total_arab_universities}")

table_columns = ['University', 'Location', 'RANK 24', 'RANK 23']
arab_universities_table = arab_universities[table_columns]

print("\nTable for Arab Universities:")
print(arab_universities_table.to_string(index=False))

filtered_universities_table = arab_universities_table[arab_universities_table['RANK 24'] < arab_universities_table['RANK 23']]

increasing_rate_table = filtered_universities_table.copy()
increasing_rate_table['Increasing Rate'] = increasing_rate_table['RANK 23'] - increasing_rate_table['RANK 24']

print("\nTable of Universities with Rank 24 < Rank 23:")
print(filtered_universities_table.to_string(index=False))

print("\nTable of Universities with Increasing Rate:")
print(increasing_rate_table[['University', 'Location', 'Increasing Rate']].to_string(index=False))

plt.figure(figsize=(12, 8))
for location, data in increasing_rate_table.groupby('Location'):
    plt.bar(data['University'], data['Increasing Rate'], label=location, alpha=0.7)

plt.xlabel('University')
plt.ylabel('Increasing Rate')
plt.title('Increasing Rate of Universities in Arab Countries by Location')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Location', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

research_table_columns = ['University', 'Location', 'RESEARCH']
arab_research_table = arab_universities[research_table_columns]

print("\nTable for Arab Universities (Research Data):")
print(arab_research_table.to_string(index=False))

research_categories = ['VH', 'HI', 'MD', 'LO']

percentage_dict = {}
for category in research_categories:
    count_category = arab_universities['RESEARCH'].eq(category).sum()
    percentage = (count_category / total_arab_universities) * 100
    percentage_dict[category] = percentage

print("\nPercentage of Research Categories in Arab Universities:")
for category, percentage in percentage_dict.items():
    print(f"{category}: {percentage:.2f}%")
