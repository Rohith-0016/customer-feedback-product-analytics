import pandas as pd

def feedback_summary(df):
    print("Average Rating:", df['Rating'].mean())
    print("\nTop Complaint Categories:")
    print(df['Category'].value_counts())

if __name__ == "__main__":
    df = pd.read_csv("data/processed_feedback.csv")
    feedback_summary(df)
