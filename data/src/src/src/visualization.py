import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed_feedback.csv")

df['Category'].value_counts().plot(kind='bar')
plt.title("Complaint Category Distribution")
plt.show()
