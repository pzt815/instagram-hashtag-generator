import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_hashtags(category: str, lang: str = "ko") -> list:
    prompt = f"""
    Generate 30 SEO-optimized Instagram hashtags 
    for the category: {category}
    Language: {lang}
    Format: return only hashtags, one per line, no numbers
    """
    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text.strip().split("\n")

if __name__ == "__main__":
    categories = ["fashion", "beauty", "food", "luxury"]
    for cat in categories:
        print(f"\n=== {cat.upper()} ===")
        tags = generate_hashtags(cat, "ko")
        for tag in tags:
            print(tag)
