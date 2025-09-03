# 🕸️ AI Web Scraper with Gemini & Streamlit

An **AI-powered web scraper** that can **extract, clean, and parse website content** intelligently using Google **Gemini 1.5 Flash** 🚀.
It combines **Selenium + BeautifulSoup** for scraping, **LangChain + Gemini** for parsing, and a **Streamlit UI** for an interactive experience.

---

## ✨ What It Can Do

1. 🔗 Enter any website URL → Scrape its content
2. 🧹 Extract and clean **readable DOM body**
3. 🤖 Describe what you want → Gemini returns **only the requested info**

---

## 🚀 Features

* ✅ **Headless Web Scraping** with Selenium + SuperProxy
* ✅ **Auto CAPTCHA Handling** via Chromium CDP
* ✅ **Content Cleaning** → removes scripts, ads, and clutter
* ✅ **DOM Chunking** → handles even large pages
* ✅ **AI-Powered Parsing** with Gemini 1.5 Flash (fast & cost-efficient)
* ✅ **Interactive UI** built in Streamlit

---

## 🛠️ Tech Stack

| Component       | Technology Used                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------- |
| **Frontend UI** | [Streamlit](https://streamlit.io/)                                                                      |
| **Scraping**    | [Selenium](https://www.selenium.dev/), [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) |
| **AI Parsing**  | [LangChain](https://www.langchain.com/), [Google Gemini API](https://ai.google.dev/)                    |
| **Language**    | Python 3.9+                                                                                             |

---

## 📂 Project Structure

```
📦 AI-Web-Scraper
 ┣ 📜 main.py            # Streamlit app (UI)
 ┣ 📜 scrape.py          # Web scraping logic
 ┣ 📜 parse.py           # AI parsing with Gemini
 ┣ 📜 requirements.txt   # Dependencies
 ┣ 📜 .env               # API key & secrets (excluded from git)
 ┗ 📂 __pycache__/       # Python cache (ignored)
```

---

## ⚡ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Tom-1508/AI-Web-Scraper.git
cd AI-Web-Scraper
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add your API Key

Create a `.env` file in the root directory:

```
GOOGLE_API_KEY=your_api_key_here
```

### 5️⃣ Run the app

```bash
streamlit run main.py
```

---

## 🎮 Usage Guide

1. Launch the Streamlit app.
2. Enter a website URL → click **"Scrape Site"**.
3. Expand the **DOM Viewer** to see extracted HTML content.
4. Enter your query (e.g., *"Extract all product prices"*).
5. Click **"Parse Content"** → AI will return clean, structured data.

---

## 🎥 Demo Video

[![Watch the demo](https://img.youtube.com/vi/AU1AczEB4ds/0.jpg)](https://youtu.be/AU1AczEB4ds?si=8J_zgoqp2uoyt41-)

*(Click the thumbnail above to watch the full demo on YouTube)*

---

## 📝 Example Use Cases

* 🛒 Extract product prices & details from e-commerce sites
* 📰 Scrape news articles without ads/scripts
* 📊 Collect structured data from messy HTML content
* 📚 Extract key insights for research or analysis

---

## 🔒 Security Notes

* `.env` file (with API key) is ignored via `.gitignore`.
* **Never** commit your API keys or credentials.

---

## 📜 License

This project is licensed under the **MIT License**.
Feel free to fork, use, and improve it. 🚀

---

## 👨‍💻 Author

Developed with ❤️ by [**Tamal Majumdar**](https://github.com/Tom-1508)
Inspired by **modern AI-driven web scraping techniques**.

---