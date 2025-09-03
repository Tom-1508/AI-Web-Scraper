# 🕸️ AI Web Scraper with Gemini & Streamlit

An **AI-powered web scraper** that can **extract, clean, and parse website content intelligently** using **Google Gemini 1.5 Flash** 🚀.  
Built with **Selenium + BeautifulSoup** for scraping, **LangChain + Gemini** for parsing, and a **Streamlit UI** for interactivity.  

---

## ✨ Key Features

- ✅ **Headless Web Scraping** using Selenium + SuperProxy  
- ✅ **Smart CAPTCHA Handling** via Chromium CDP  
- ✅ **Content Cleaning** → removes ads, scripts, and clutter  
- ✅ **DOM Chunking** for large web pages  
- ✅ **AI-Powered Parsing** with Gemini 1.5 Flash (fast & cost-efficient)  
- ✅ **Interactive Streamlit UI** for real-time usage  

---

## 🛠️ Tech Stack

| Layer             | Technology                                                                 |
| ----------------- | --------------------------------------------------------------------------- |
| **Frontend UI**   | [Streamlit](https://streamlit.io/)                                          |
| **Web Scraping**  | [Selenium](https://www.selenium.dev/), [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) |
| **AI Parsing**    | [LangChain](https://www.langchain.com/), [Google Gemini API](https://ai.google.dev/) |
| **Language**      | Python 3.9+                                                                 |

---

## 📂 Project Structure

```bash
📦 AI-Web-Scraper
 ┣ 📜 main.py            # Streamlit app (UI)
 ┣ 📜 scrape.py          # Web scraping logic
 ┣ 📜 parse.py           # AI parsing with Gemini
 ┣ 📜 requirements.txt   # Dependencies
 ┣ 📜 .env               # API keys & secrets (excluded from Git)
 ┗ 📂 __pycache__/       # Python cache (ignored)
````

---

## ⚡ Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Tom-1508/AI-Web-Scraper.git
cd AI-Web-Scraper
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add your API Key

Create a `.env` file in the project root:

```ini
GOOGLE_API_KEY=your_api_key_here
```

### 5️⃣ Run the Streamlit app

```bash
streamlit run main.py
```

---

## 🎮 How to Use

1. Launch the Streamlit app.
2. Enter a website URL → click **Scrape Site**.
3. Inspect extracted DOM in the **Viewer Panel**.
4. Type a query (e.g., *"Extract all product prices"*).
5. Click **Parse Content** → AI delivers clean, structured results.

---

## 🎥 Demo Video

[![Watch the demo](https://img.youtube.com/vi/AU1AczEB4ds/0.jpg)](https://youtu.be/AU1AczEB4ds?si=8J_zgoqp2uoyt41-)

*(Click the thumbnail to watch on YouTube)*

---

## 📝 Example Use Cases

* 🛒 Extract product data from e-commerce websites
* 📰 Collect clean news articles without ads
* 📊 Convert messy HTML into structured datasets
* 📚 Summarize or extract insights for research

---

## 🔒 Security Notes

* The `.env` file (with API keys) is **gitignored**.
* Never expose API keys in commits or public repos.

---

## 📜 License

Licensed under the **MIT License**.
You are free to use, modify, and distribute this project. 🚀

---

## 👨‍💻 Author

Developed with ❤️ by [**Tamal Majumdar**](https://github.com/Tom-1508)
Inspired by modern **AI-driven web scraping techniques** 🌐🤖