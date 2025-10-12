import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity 
import streamlit as st


df = pd.read_csv("book_csv")  
df['title'] = df['title'].str.strip()
df['description'] = df['description'].fillna("")


# Create TF-IDF matrix
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['description'])

# Compute cosine similarity
cosine_mat = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Create index mapping
indices = pd.Series(df.index, index=df['title'].str.lower()).drop_duplicates()

# Recommendation function
def get_recommendations(title, cosine_sim, indices, df):
    if title not in indices:
        return pd.DataFrame({"Error": [f"'{title}' not found in book list."]})
    
    idx = indices.loc[title]
    if isinstance(idx,pd.Series):
        idx = idx.iloc[0]
        
    idx = indices.loc[title]     
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6] 
    book_indices = [i[0] for i in sim_scores]
    
    # Return relevant columns safely
    return df.loc[book_indices, ['title', 'author']]

# Streamlit UI
st.title(" Book Recommendation System")
st.write("Enter a book title and get similar book recommendations!")

select_book = st.text_input("Book Title")

if select_book:
    results = get_recommendations(select_book, cosine_mat, indices, df)
    st.table(results)
