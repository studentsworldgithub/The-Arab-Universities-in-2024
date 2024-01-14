import pandas as pd
import matplotlib.pyplot as plt

dataset_path = '/content/sample_data/Computer Science and Information Systems 2023.csv'
df = pd.read_csv(dataset_path)

total_records = len(df)
print(f"Total number of records: {total_records}")

max_academic_reputation = df.loc[df['Academic_Reputation'].idxmax()]
print(f"Max Academic Reputation:\n{max_academic_reputation[['University', 'Location', 'Academic_Reputation']]}")

max_employer_reputation = df.loc[df['Employer_Reputation'].idxmax()]
print(f"Max Employer Reputation:\n{max_employer_reputation[['University', 'Location', 'Employer_Reputation']]}")

max_citations_per_paper = df.loc[df['Citations_per_Paper'].idxmax()]
print(f"Max Citations per Paper:\n{max_citations_per_paper[['University', 'Location', 'Citations_per_Paper']]}")

max_h_index_citations = df.loc[df['H-index_Citations'].idxmax()]
print(f"Max H-index Citations:\n{max_h_index_citations[['University', 'Location', 'H-index_Citations']]}")

max_international_research_network = df.loc[df['International Research Network'].idxmax()]
print(f"Max International Research Network:\n{max_international_research_network[['University', 'Location', 'International Research Network']]}")

max_university_score = df.loc[df['University_Score'].idxmax()]
print(f"Max University Score:\n{max_university_score[['University', 'Location', 'University_Score']]}")

max_qs_world_rank = df.loc[df['QS_World_Rank'].idxmax()]
print(f"Max QS World Rank:\n{max_qs_world_rank[['University', 'Location', 'QS_World_Rank']]}")

plt.scatter(df['Location'], df['University_Score'])
plt.xlabel('Location')
plt.ylabel('University Score')
plt.title('University Score by Location')
plt.show()

plt.scatter(df['Location'], df['QS_World_Rank'])
plt.xlabel('Location')
plt.ylabel('QS World Rank')
plt.title('QS World Rank by Location')
plt.show()

df.plot(kind='scatter', x='Location', y='University_Score', c='QS_World_Rank', colormap='viridis', title='University Score and QS World Rank')
plt.show()
