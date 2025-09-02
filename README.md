# Reflexion Agent

Reflexion Agent is an AI-powered research assistant that can answer questions, reflect critically on its own answers, and suggest follow-up research queries.  
It is built using [LangChain](https://www.langchain.com/), [OpenAI GPT-4 Turbo](https://platform.openai.com/), and Python.

## 🚀 Features
- Generates detailed (~250 word) answers to user questions.
- Reflects and critiques its own answers to identify weaknesses.
- Suggests follow-up search queries for deeper research.
- Modular design using **LangChain** and **Pydantic schemas**.

## 📂 Project Structure
```
ReflexionAgent/
│── .env                # Environment variables (contains API keys)
│── .env.example        # Example environment variables file
│── main.py             # Entry point of the project
│── chains.py           # Core logic for prompts, LLM, and agent chain
│── schemas.py          # Pydantic schemas for structured outputs
│── poetry.lock         # Poetry lock file
│── poetry.toml         # Poetry configuration
│── pyproject.toml      # Project metadata & dependencies
```

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/mouyse/Reflexion-Agent.git
cd ReflexionAgent
```

### 2️⃣ Setup Virtual Environment
Using **Poetry** (recommended):
```bash
poetry install
```

Or using pip:
```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables
Copy `.env.example` to `.env` and fill in your API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## ▶️ Usage

Run the Reflexion Agent:
```bash
python main.py
```

Example run from `chains.py`:
- The agent answers a question about **India Sensex predictions**, reflects on its response, and suggests search queries for further research.

## 🛠 Dependencies
- Python 3.10+
- [LangChain](https://pypi.org/project/langchain/)
- [LangChain-OpenAI](https://pypi.org/project/langchain-openai/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [pydantic](https://docs.pydantic.dev/)

## 📌 Example Output
```json
{
  "answer": "The Sensex is likely to show volatility in the upcoming weeks due to global economic tensions...",
  "reflection": {
    "missing": "Did not include specific stock suggestions.",
    "superfluous": "Too much emphasis on geopolitical risks without data support."
  },
  "search_queries": [
    "India Sensex forecast September 2025",
    "Top Indian stocks for short-term growth",
    "Impact of geopolitical tensions on Indian stock market"
  ]
}
```

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repo, open issues, and submit PRs.

## 📄 License
This project is licensed under the MIT License.
