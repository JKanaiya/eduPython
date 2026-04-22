# python file to demonstrate collaborative filtering to recommend similar items/products based on user interaction

# import the required modules
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------------------------------
# STEP 1. Create a sample dataset
# ---------------------------------------------------

# Each row represents a user interaction with a product ( interaction  = 1 means viewed/purchased )

data = {
    "user_id": [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5],
    "product": [
        "Laptop",
        "Mouse",
        "Keyboard",
        "Laptop",
        "Mouse",
        "Laptop",
        "Keyboard",
        "MonitorKeyboard",
        "Monitor",
        "Laptop",
        "Mouse",
        "Monitor",
        "Keyboard",
    ],
    "interaction": [1] * 13,
}

# convert the above dictionary into a pandas dataframe

df = pd.DataFrame(data)

# ---------------------------------------------------
# STEP 2. Create a user-item/product matrix
# ---------------------------------------------------

# rows = users, columns = products, values = interactions ( 0 or 1)

user_item_matrix = df.pivot_table(
    index="user_id", columns="product", values="interaction", fill_value=0
)

print(f"User-Item matrix: {user_item_matrix}")

# ---------------------------------------------------
# STEP 3. Compute the item similarity
# ---------------------------------------------------
# Transpose metrics to get item vectors
item_matrix = user_item_matrix.T

# compute cosine similarity between products/items
item_similarity = cosine_similarity(item_matrix)

# convert to dataframe for readability
item_similarity_df = pd.DataFrame(
    item_similarity, index=item_matrix.index, columns=item_matrix.index
)

# Display the similarity matrix
print(f"Item similarity matrix: \n{item_similarity_df}")

# ---------------------------------------------------
# STEP 4. Create a user-item/product matrix
# ---------------------------------------------------


def recommend_similar_products(product_name, top_n=3):
    """
    recommended products similar to the given product

    Args:
        product_name (str) : Product to find similarities for top_n (int) Number of recommendations to return

    Returns:
        List of recommended products
    """

    if product_name not in item_similarity_df.columns:
        return f"Product {product_name} not found"

    # get similarity scores
    similarity_scores = item_similarity_df[product_name]

    # sort b similarity (descending)
    similar_products = similarity_scores.sort_values()

    # remove the product itself
    similar_products = similar_products.drop(product_name)

    # return top n recommendations
    return similar_products.head(top_n)


# -----------------------------------------------------------------------------------------------------
# STEP 5. Test the collaborative product recommendation system
# -----------------------------------------------------------------------------------------------------

product_2_search = "Laptop"
recommendations = recommend_similar_products(product_2_search)

# Display recommendations
print(f"Products similar to {product_2_search}: \n{recommendations}")
