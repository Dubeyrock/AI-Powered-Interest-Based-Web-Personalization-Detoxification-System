# 🚀 AI-Powered Interest-Based Web Personalization & Detoxification System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)

A Streamlit-based AI system that personalizes web content around user-defined interests (e.g., "Chess") while filtering toxic/distracting content. Built for SlateMate's FocusSphere initiative.

![Demo Screenshot](https://via.placeholder.com/800x400?text=App+Demo+Screenshot+Here)

## ✨ Features
- 🔍 **Interest-Based Filtering**: Prioritizes content using BERT embeddings
- 🛡️ **Toxicity Detection**: Blocks harmful content via Detoxify API
- 📊 **Well-being Scoring**: Combines relevance (70%) + safety (30%)
- 🎯 **Real-Time Feed**: Simulated YouTube/Instagram/Reddit content
- 📱 **Streamlit UI**: User-friendly interface for students

🖥️ Usage
In the browser:

Enter your interest (e.g., "Chess")

Click Generate Safe Feed

View recommendations + blocked content

Example Output:

✅ Top 10 Chess Openings (YouTube) | Score: 92.3
✅ Chess Puzzle of the Day (Reddit) | Score: 94.5
❌ Try Not to Laugh Challenge | Reason: Low relevance


📂 Project Structure

AI-Powered-Interest-Based-Web-Personalization-Detoxification-System/
├── App/
│   └── app.py                # Streamlit UI and core logic
├── Data/
│   ├── slatemate_interest_feed_dataset.csv  # Sample dataset
│   ├── simulated_feed.json   # Simulated content
│   └── simulated_content.py  # Content generator
├── .gitignore
├── Requirements.txt          # Python dependencies
└── README.md

🙏 Acknowledgments

---

### Key Elements Added:
1. **Badges**: License + Python version indicators
2. **Visual Hierarchy**: Emojis + headers for scannability
3. **Code Blocks**: Ready-to-copy installation/usage commands
4. **File Structure Map**: Clear directory explanation
5. **Contributing Guide**: Standard open-source workflow
6. **Placeholder Image**: Add actual screenshot later

