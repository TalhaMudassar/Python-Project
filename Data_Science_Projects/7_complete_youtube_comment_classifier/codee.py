import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.model_selection import train_test_split 
import streamlit as st

@st.cache_resource
def load_model():
    """
    Loads the DataFrame and trains the classification pipeline.
    
    It first attempts to read the file path 'youtube_comments.csv'.
    If the file is not found, it falls back to the embedded data.
    """
    try:
        # 1. Attempt to read the local file path as requested
        df = pd.read_csv("youtube_comments.csv")
        st.sidebar.info("Model loaded successfully from local file: `youtube_comments.csv`")
    except FileNotFoundError:
        # 2. Fallback to using the embedded data if the file path fails
        st.sidebar.warning("Could not find 'youtube_comments.csv'. Using embedded fallback data.")
        data = io.StringIO(FALLBACK_CSV_CONTENT)
        df = pd.read_csv(data)
    except Exception as e:
        st.sidebar.error(f"Error loading data: {e}. Cannot proceed.")
        return None # Return None if data loading fails

    # Initialize the machine learning pipeline
    model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        # Increased max_iter for robust training, a common practice for Logistic Regression
        ('clf', LogisticRegression(max_iter=1000)),
    ])
    
    # Check if the DataFrame has the necessary columns before fitting
    if 'comment' in df.columns and 'label' in df.columns:
        model.fit(df['comment'], df['label'])
        return model
    else:
        st.sidebar.error("Data error: CSV must contain 'comment' and 'label' columns.")
        return None


# --- Streamlit Application Layout ---

# Load the trained model. This only runs once due to st.cache_resource.
model = load_model()


if model:
    st.title(" YouTube Comment Classifier")
    st.markdown("A simple model to predict if a comment is **Toxic** or **Supportive**.")
    
    user_input = st.text_area("Enter your YouTube comment below:")
    
    if user_input:
        
        prediction = model.predict([user_input])[0]
        
        st.markdown("---")
        st.subheader("Classification Result")

        # Display the result using Streamlit's error/success components for visual feedback
        if prediction == "toxic":
            st.error(f"Prediction: This comment is likely **Toxic** 😡")
        else:
            st.success(f"Prediction: This comment is **Supportive** 💖")

