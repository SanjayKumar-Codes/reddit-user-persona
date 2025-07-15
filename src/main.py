from src.scraper import init_reddit, fetch_user_activity

from src.persona_builder import generate_persona
import os

if __name__ == "__main__":
    reddit = init_reddit()
    username = "kojied"

    posts, comments = fetch_user_activity(reddit, username)
    persona = generate_persona(posts, comments)


    print("\n📄 Posts:")
    for post in posts[:3]:
        print(post)

    print("\n💬 Comments:")
    for comment in comments[:3]:
        print(comment)

    print("\n👤 Generated Persona:")
    output_path = os.path.join("data", f"{username}_persona.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(persona)

    print(f"✅ Persona written to {output_path}")
