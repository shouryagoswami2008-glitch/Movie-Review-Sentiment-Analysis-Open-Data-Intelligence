# Movie-Review-Sentiment-Analysis-Open-Data-Intelligence
The Movie Review Sentiment Analysis project demonstrates how to extract and analyze audience sentiment from a completely free and open data source: The Movie Database (TMDB). By moving away from restrictive commercial APIs, this project showcases a commitment to using open-source resources to build powerful data analytics tools.
2. Data Acquisition via TMDB API

We utilized the TMDB API, a popular and developer-friendly platform that provides comprehensive data on movies, TV shows, and user reviews.

2.1 Why TMDB?

•
Truly Free Access: TMDB offers a generous free tier for developers, making it ideal for student and portfolio projects.

•
Rich Metadata: Beyond just text, TMDB provides user ratings, author details, and precise timestamps, allowing for multi-dimensional analysis.

•
Community-Driven: As a user-editable database, the data reflects real-world audience diversity.

2.2 Technical Implementation

The data pipeline (fetch_tmdb_reviews.py) is designed to:

•
Authenticate using a standard API key.

•
Target specific cinematic masterpieces (e.g., "Fight Club" or "Inception") to gather focused review data.

•
Extract the Content of the review, the numerical Rating, and the Created At timestamp.

3. Sentiment Analysis and NLP

Using the TextBlob library, we processed the unstructured review text to quantify audience emotions.

3.1 Polarity and Subjectivity

•
Polarity: Measures how positive or negative the review is.

•
Sentiment Mapping: We categorized reviews into Positive, Neutral, and Negative based on their polarity scores, providing a high-level view of audience reception.

4. Visual Insights

Our analysis produced three key visualizations that reveal the "pulse" of the audience:

4.1 Sentiment Distribution

The count plot (tmdb_sentiment_distribution.png) provides an immediate visual summary of the movie's reception. For our target film, 50% of the reviews were positive, reflecting its "cult classic" status.

4.2 Rating vs. Sentiment Correlation

The regression plot (tmdb_rating_vs_polarity.png) explores the relationship between a user's numerical rating and the sentiment of their written review. A strong positive correlation confirms that users' words generally align with their scores.

4.3 Sentiment Trends Over Time

The trend line (tmdb_sentiment_trend.png) tracks how audience sentiment has evolved since the movie's release. This allows us to see if a film's reputation has improved or declined over the years.

