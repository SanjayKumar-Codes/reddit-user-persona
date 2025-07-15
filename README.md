
## 📄 `README.md`

````markdown
# 🧠 Reddit User Persona Generator

This is a Python-based tool to extract Reddit user activity and generate a persona profile using LLMs (OpenAI).  
It fetches a user's posts and comments, analyzes them, and outputs a `.txt` file describing the user's personality, interests, tone, and more — with proper citations.

---

## 🚀 Features

- 🔍 Scrapes Reddit user posts & comments (via PRAW)
- 🤖 Builds a detailed user persona using OpenAI LLMs
- 🧾 Outputs a citation-backed `.txt` persona file per user
- 📦 Easy to run via `main.py`

---

## 🔧 Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/reddit-user-persona.git
cd reddit-user-persona
````

### 2. Create and Configure `.env` File

Create a `.env` file in the root directory with the following:

```env
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_secret_key
REDDIT_USER_AGENT=your_reddit_user_agent
OPENAI_API_KEY=your_openai_api_key
```

> You can create Reddit API credentials from: [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
> Get an OpenAI key from: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

---

### 3. Install Dependencies

Make sure Python 3.8+ is installed.

```bash
pip install -r requirements.txt
```

---

## ⚙️ How to Run

```bash
python -m src.main
```

By default, this will fetch and generate a persona for the user hardcoded in `main.py`.

To use a different Reddit user:

1. Open `src/main.py`
2. Modify this line:

   ```python
   username = "desired_reddit_username"
   ```

---

## 📁 Output

A `.txt` file will be saved in the `data/` directory:

```
data/kojied_persona.txt
data/Hungry-Move-6603_persona.txt
```

Each file contains:

* Personality traits
* Writing tone
* Hobbies & interests
* Professional cues
* Unique behaviors
* Citations from Reddit activity

---

## 📚 Sample Files

This repo includes:

* ✅ `kojied_persona.txt`
* ✅ `Hungry-Move-6603_persona.txt`

---

## 📄 Folder Structure

```
reddit-user-persona/
├── data/
│   └── <user>_persona.txt
├── src/
│   ├── scraper.py
│   ├── persona_builder.py
│   └── main.py
├── requirements.txt
├── .env (not included in repo)
└── README.md
```

---

## 🛡 Disclaimer

This project is for educational/internship purposes only.
Your credentials remain local and are not collected or shared.

---

## 💡 Future Ideas

* Support multiple usernames via CLI
* Add GUI interface
* Use local LLMs or other APIs (Claude, Gemini)

---

👨‍💻 Author

**Sanjay Kumar M**  
📧 [Email Me](mailto:sanjaychitra9159@gmail.com)  
🌐 [LinkedIn](https://www.linkedin.com/in/sanjay-kumarai)  
💻 [GitHub](https://github.com/SanjayKumar-Codes)

