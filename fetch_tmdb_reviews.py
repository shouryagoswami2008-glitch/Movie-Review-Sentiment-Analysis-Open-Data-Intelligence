import requests
import pandas as pd

# Replace with your actual TMDB API key
TMDB_API_KEY = "e0976710fee8192df4fa5ad8ab91f40d"

def fetch_movie_reviews(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews"

    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US",
        "page": 1
    }

    try:
        print("Fetching live reviews from TMDB...")

        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        results = data.get("results", [])

        review_list = []

        for review in results:
            review_list.append({
                "Author": review.get("author"),
                "Content": review.get("content"),
                "Rating": review.get("author_details", {}).get("rating"),
                "Created At": review.get("created_at")
            })

        if len(review_list) == 0:
            print("No reviews found for this movie.")
            return pd.DataFrame()

        return pd.DataFrame(review_list)

    except Exception as e:
        print(f"Error fetching TMDB reviews: {e}")
        return pd.DataFrame()

if __name__ == "__main__":

    # Movie IDs:
    # Fight Club = 550
    # Inception = 27205
    # The Dark Knight = 155
    # Interstellar = 157336

    movie_id = 550

    df = fetch_movie_reviews(movie_id)

    print("\nFirst 5 Reviews:")
    print(df.head())

    df.to_csv("tmdb_reviews.csv", index=False)

    print(f"\nSaved {len(df)} reviews to tmdb_reviews.csv")