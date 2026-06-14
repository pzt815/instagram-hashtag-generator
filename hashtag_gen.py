import openai

def generate_hashtags(category: str, lang: str = "ko") -> list:
    prompt = f"""
    Generate 30 SEO-optimized Instagram hashtags 
    for the category: {category}
    Language: {lang}
    Format: return only hashtags, one per line
    """
    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=prompt,
        max_tokens=300
    )
    hashtags = response.choices[0].text.strip().split("\n")
    return hashtags

if __name__ == "__main__":
    tags = generate_hashtags("fashion", "ko")
    for tag in tags:
        print(tag)
