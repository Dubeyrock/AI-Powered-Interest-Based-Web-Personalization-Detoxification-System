import random
from typing import List, Dict

def generate_content_feed() -> List[Dict]:
    interests = ["Chess", "Biology", "Space", "Robotics"]
    sources = ["YouTube", "Instagram", "Reddit", "Blog"]
    templates = {
        "Chess": ["Chess strategies", "Grandmaster tips", "Tournament analysis"],
        "Generic": ["Funny memes", "Celebrity news", "Gaming highlights"]
    }
    
    feed = []
    for _ in range(100):
        if random.random() > 0.3:  # 70% relevant content
            category = random.choice(interests)
            template = random.choice(templates.get(category, []))
        else:
            category = "Generic"
            template = random.choice(templates["Generic"])
            
        feed.append({
            "title": f"{template} {random.randint(1, 100)}",
            "text": f"Learn about {template.lower()}",
            "source": random.choice(sources),
            "category": category,
            "toxicity_score": random.uniform(0, 0.4 if category != "Generic" else 0.6)
        })
    return feed