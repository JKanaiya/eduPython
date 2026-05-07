import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample user-item rating data
data = {
    "User1": [5, 4, 0, 0, 1],
    "User2": [0, 0, 5, 4, 2],
    "User3": [3, 4, 0, 5, 0],
    "User4": [0, 2, 4, 0, 5],
    "User5": [1, 0, 3, 0, 4],
}

df = pd.DataFrame(data, index=["Item1", "Item2", "Item3", "Item4", "Item5"])

# Step 1: User Similarity Calculation (Cosine Similarity)
user_similarity = cosine_similarity(df)


# Step 2: Neighborhood Selection (Top similar users)
def get_similar_users(user_index, user_similarity=user_similarity, num_neighbors=2):

    similar_users = list(enumerate(user_similarity[user_index]))
    similar_users = sorted(similar_users, key=lambda x: x[1], reverse=True)
    neighbors = similar_users[1 : (num_neighbors + 1)]  # Exclude the user itself
    return neighbors


# Step 3: Rating Aggregation (Weighted average of neighbors' ratings)
def predict_rating(user_index, item_index, df, user_similarity=user_similarity):
    neighbors = get_similar_users(user_index)
    numerator = 0
    denominator = 0

    for neighbor_index, similarity_score in neighbors:
        neighbor_rating = df.iloc[neighbor_index][item_index]
        if neighbor_rating != 0:  # Consider only rated items
            numerator += similarity_score * neighbor_rating
            denominator += abs(similarity_score)

    if denominator == 0:
        return 0  # Avoid division by zero

    predicted_rating = numerator / denominator
    return predicted_rating


# Step 4: Recommendation Generation (Recommend items with high predicted ratings)
def recommend_items(user_index, df):
    unrated_items = df.columns[df.iloc[user_index] == 0]
    recommendations = []

    for item in unrated_items:
        predicted_rating = predict_rating(user_index, item, df)
        recommendations.append((item, predicted_rating))

    recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)
    return recommendations


# Example: Recommend items for 'User1'
user_index = 0
recommendations = recommend_items(user_index, df)
print(f"Recommended items for User{user_index + 1}:")
print(recommendations)
