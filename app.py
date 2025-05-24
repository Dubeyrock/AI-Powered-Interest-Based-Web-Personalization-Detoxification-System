here is my app.py code 

# app.py
import streamlit as st
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ------------ Merge utils.py ------------
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    return model.encode(text, convert_to_tensor=False)

def calculate_wellbeing(relevance_score, toxicity_score, weights=(0.7, 0.3)):
    safety_score = 1 - toxicity_score
    return (relevance_score * weights[0] + safety_score * weights[1]) * 100

# ------------ Merge generate_feed.py ------------
def generate_safe_feed(user_interest, content_feed, relevance_threshold=0.3, toxicity_threshold=0.5):
    interest_embedding = get_embedding(user_interest).reshape(1, -1)
    
    recommendations = []
    blocked = []
    
    for item in content_feed:
        content_text = f"{item['title']} {item['text']}"
        content_embedding = get_embedding(content_text).reshape(1, -1)
        relevance = cosine_similarity(interest_embedding, content_embedding)[0][0]
        
        toxicity = item['toxicity_score']
        if relevance < relevance_threshold or toxicity > toxicity_threshold:
            reason = "Low relevance" if relevance < relevance_threshold else "High toxicity"
            blocked.append({"title": item['title'], "reason": reason})
            continue
        
        wellbeing = calculate_wellbeing(relevance, toxicity)
        recommendations.append({
            "title": item['title'],
            "source": item['source'],
            "wellbeing_score": round(wellbeing, 1),
            "reason": "Highly relevant & safe" if (1 - toxicity) > 0.7 else "Moderate relevance"
        })
    
    recommendations.sort(key=lambda x: x['wellbeing_score'], reverse=True)
    return {
        "detected_interest": user_interest,
        "top_recommendations": recommendations[:10],
        "blocked_content": blocked
    }

# ------------ Streamlit UI ------------

df = pd.read_csv(r"slatemate_interest_feed_dataset.csv")
content_feed = df.to_dict('records')

st.title("🚀 AI-Powered Interest-Based Web Personalization & Detoxification System")
user_interest = st.text_input("Enter Interest (e.g. Chess):", "Chess")
st.sidebar.title("ℹ️ About SlateMate")
st.sidebar.markdown("""
SlateMate is an AI-powered web detoxification and personalization system designed to help students focus on their interests while filtering out irrelevant or unsafe content.

Built using NLP, content similarity, and emotional safety metrics, it customizes the digital experience to align with a student’s passion — like Chess, Space, or Biology — and blocks distractions.
""")

st.sidebar.title("🛠 Features")
st.sidebar.markdown("""

Accepts user-defined interest (e.g., Chess).

Simulates and processes content from YouTube, Instagram, Reddit, etc.

Uses Sentence Transformers for interest-content similarity.

Evaluates emotional safety via toxicity scores.

Combines relevance and safety into a Well-being Score.

Returns a detoxified and re-ranked personalized feed.
""")



if st.button("Generate Feed"):
    result = generate_safe_feed(user_interest, content_feed)
    
    st.subheader(f"Recommended for {result['detected_interest']}:")
    for item in result['top_recommendations']:
        st.markdown(f"✅ **{item['title']}** ({item['source']})  \nScore: {item['wellbeing_score']} - {item['reason']}")
    
    st.subheader("Blocked Content:")
    for item in result['blocked_content']:
        st.markdown(f"❌ ~~{item['title']}~~ ({item['reason']})")



🎁 Bonus: You can also add a small “Built by” credit in the sidebar:

st.sidebar.markdown("👨‍💻 Built by Shivam Dubey")


give me a code proper sidebar , about section , add features
