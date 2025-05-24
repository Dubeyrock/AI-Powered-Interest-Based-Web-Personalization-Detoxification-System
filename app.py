# app.py
import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ------------ Model Initialization ------------
model = SentenceTransformer('all-MiniLM-L6-v2')

# ------------ Helper Functions ------------
def get_embedding(text):
    return model.encode(text, convert_to_tensor=False)

def calculate_wellbeing(relevance_score, toxicity_score, weights=(0.7, 0.3)):
    safety_score = 1 - toxicity_score
    return (relevance_score * weights[0] + safety_score * weights[1]) * 100

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

# ------------ Streamlit UI Configuration ------------
st.set_page_config(
    page_title="SlateMate AI",
    page_icon="♟️",
    layout="centered"
)

# ------------ Sidebar Content ------------
with st.sidebar:
    st.title("♟️ SlateMate AI")
    st.markdown("---")
    
    # About Section
    with st.expander("📖 About SlateMate", expanded=True):
        st.markdown("""
        **SlateMate** is an AI-powered content curation system that:
        - 🔍 Focuses on educational content
        - 🛡️ Filters harmful/distracting material
        - 🎯 Personalizes feeds based on interests
        - 📈 Promotes healthy digital habits
        
        *Empowering students to explore their passions safely*""")
    
    # Features Section
    with st.expander("✨ Key Features", expanded=True):
        st.markdown("""
        - **Interest-Based Filtering**: Chess, Science, Biology, etc.
        - **Toxicity Detection**: AI-powered safety checks
        - **Multi-Platform Support**: YouTube, Instagram, Reddit
        - **Dynamic Ranking**: Combines relevance & safety
        - **Real-Time Processing**: Instant feed generation""")
    
    # Documentation Section
    with st.expander("📚 Documentation"):
        st.markdown("""
        - [System Architecture](https://your-docs-link.com)
        - [API Reference](https://your-api-docs.com)
        - [User Guide](https://user-guide-link.com)
        """)
    
    st.markdown("---")
    st.markdown("### 🛠️ Technical Stack")
    st.markdown("""
    - **NLP**: Sentence Transformers
    - **Safety**: Detoxify
    - **UI**: Streamlit
    - **ML**: Scikit-learn
    """)
    
    st.markdown("---")
    st.markdown("👨💻 **Built by** [Shivam Dubey](https://github.com/Dubeyrock)")
    st.markdown("🔗 [GitHub Repository](https://github.com/Dubeyrock/SlateMate-AI)")

# ------------ Main Content ------------
df = pd.read_csv("slatemate_interest_feed_dataset.csv")
content_feed = df.to_dict('records')

st.title("🚀 AI-Powered Content Personalization System")
st.markdown("### Safely Explore Your Interests in the Digital World 🌍")

# User Input Section
col1, col2 = st.columns([3, 1])
with col1:
    user_interest = st.text_input("Enter your primary interest:", "Chess")
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    generate_btn = st.button("🚀 Generate Feed")

if generate_btn:
    with st.spinner("🔍 Analyzing content and ensuring safety..."):
        result = generate_safe_feed(user_interest, content_feed)
    
    # Results Display
    st.success(f"✅ Successfully generated safe feed for **{result['detected_interest']}**")
    
    # Recommendations Section
    st.subheader("📚 Top Recommended Content")
    for item in result['top_recommendations']:
        with st.container():
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f"**{item['title']}**  \n*{item['source']}*")
            with col2:
                st.metric("Score", f"{item['wellbeing_score']}/100")
            st.progress(item['wellbeing_score']/100)
            st.caption(f"✔️ {item['reason']}")
            st.markdown("---")
    
    # Blocked Content Section
    if result['blocked_content']:
        st.subheader("🚫 Blocked Content")
        for item in result['blocked_content']:
            st.markdown(f"""
            <div style="color: #ff4b4b; padding: 10px; border-radius: 5px; margin: 5px 0;">
            ⚠️ ~~{item['title']}~~  
            *Reason: {item['reason']}*
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #777; font-size: 0.9em;">
    🛡️ Protected by SlateMate AI | 🔒 Data Privacy First | 🌐 Learn more at our website
</div>
""", unsafe_allow_html=True)
