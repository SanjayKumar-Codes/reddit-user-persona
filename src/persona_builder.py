import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def build_prompt(posts, comments):
    content = "\n\n".join(posts + comments)
    return f"""
You're an AI that builds detailed user personas based on Reddit activity.

Given the following posts and comments by a Reddit user, generate a persona containing:

1. Personality traits
2. Writing tone
3. Hobbies & interests
4. Profession / background (if inferred)
5. Unique behaviors or beliefs
6. Citations (reference quotes from posts/comments)

Here is the Reddit content:

{content}
""".strip()

def generate_persona(posts, comments):
    prompt = build_prompt(posts, comments)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional persona profiler."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1500
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"❌ OpenAI API Error: {e}")
        return "Error generating persona."
