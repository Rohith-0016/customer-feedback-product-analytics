import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):
    df = df.dropna()
    df['Rating'] = df['Rating'].astype(int)
    return df

if __name__ == "__main__":
    data = load_data("data/raw_feedback.csv")
    clean_df = clean_data(data)
    clean_df.to_csv("data/processed_feedback.csv", index=False)
