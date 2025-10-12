import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity 


df = pd.read_csv("book_csv")
vecctorize = TfidfVectorizer(stop_words='english')
tfidf_matrix = vecctorize.fit_transform(df['description'])

cosine_mat = cosine_similarity(tfidf_matrix,tfidf_matrix)

indices = pd.Series(df.index,index = df['title'])

def get_recommendations(title,cosine_sim=cosine_mat):
    idx = indices[title] 
    sim_scores = list(enumerate(cosine_sim[idx]))
    sorted(sim_scores,key=lambda x: x[1], reverse=True )[1:6]
    boox_indices = [i[0] for i in sim_scores]
    return df['title','author'].iloc[boox_indices]

    
    