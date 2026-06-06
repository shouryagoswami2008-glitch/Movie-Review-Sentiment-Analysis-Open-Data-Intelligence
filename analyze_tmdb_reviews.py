import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob

def analyze_sentiment(text):
    if not isinstance(text, str):
        return 0
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def categorize_sentiment(polarity):
    if polarity > 0.15:
        return 'Positive'
    elif polarity < -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def process_tmdb_reviews(file_path):
    df = pd.read_csv(file_path)
    
    # Perform Sentiment Analysis
    df['Polarity'] = df['Content'].apply(analyze_sentiment)
    df['Sentiment'] = df['Polarity'].apply(categorize_sentiment)
    
    # 1. Sentiment Distribution for Movie Reviews
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Sentiment', data=df, palette='magma', order=['Positive', 'Neutral', 'Negative'])
    plt.title('Movie Review Sentiment Distribution (TMDB Data)')
    plt.xlabel('Sentiment Category')
    plt.ylabel('Count')
    plt.savefig('tmdb_sentiment_distribution.png')
    
    # 2. Rating vs Sentiment Polarity
    plt.figure(figsize=(10, 6))
    # Filter out null ratings for this plot
    plot_df = df.dropna(subset=['Rating'])
    sns.regplot(x='Rating', y='Polarity', data=plot_df, scatter_kws={'s':100}, line_kws={'color':'red'})
    plt.title('User Rating vs. Text Sentiment Polarity')
    plt.xlabel('User Rating (out of 10)')
    plt.ylabel('Sentiment Polarity')
    plt.savefig('tmdb_rating_vs_polarity.png')
    
    # 3. Sentiment Over Time (Simplified)
    plt.figure(figsize=(12, 6))
    df['Created At'] = pd.to_datetime(df['Created At'])
    df_sorted = df.sort_values('Created At')
    plt.plot(df_sorted['Created At'], df_sorted['Polarity'].rolling(window=2).mean(), marker='o', linestyle='-', color='teal')
    plt.title('Sentiment Trend of Movie Reviews Over Time')
    plt.xlabel('Date')
    plt.ylabel('Rolling Average Polarity')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('tmdb_sentiment_trend.png')
    
    print("Visualizations saved: tmdb_sentiment_distribution.png, tmdb_rating_vs_polarity.png, tmdb_sentiment_trend.png")
    
    # Summary
    print("\nMovie Review Sentiment Summary:")
    print(df['Sentiment'].value_counts(normalize=True) * 100)

if __name__ == "__main__":
    process_tmdb_reviews('tmdb_reviews.csv')
