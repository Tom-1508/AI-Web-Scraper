```markdown
# 🕸️ AI Web Scraper with Gemini & Streamlit

This project is an **AI-powered web scraper** that extracts and parses website content using:
- **Selenium + BeautifulSoup** for scraping
- **Google Gemini Flash (via LangChain)** for intelligent parsing
- **Streamlit** for an interactive UI

It allows you to:
1. Enter any website URL and scrape its content.
2. View the extracted & cleaned DOM body.
3. Describe what you want to parse, and let Gemini return only the requested information.

---

## 🚀 Features
- ✅ Headless web scraping with **Selenium + SuperProxy**
- ✅ CAPTCHA handling with **Chromium CDP**
- ✅ Content cleaning (removes scripts/styles, keeps readable text)
- ✅ DOM chunking to handle large pages
- ✅ AI parsing with **Gemini 1.5 Flash** (fast & cost-efficient)
- ✅ Interactive interface with **Streamlit**

---

## 🛠️ Tech Stack
- **Python 3.9+**
- [Streamlit](https://streamlit.io/)
- [Selenium](https://www.selenium.dev/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
- [LangChain](https://www.langchain.com/)
- [Google Gemini API](https://ai.google.dev/)

---

## 📂 Project Structure
```

📦 AI-Web-Scraper
┣ 📜 main.py            # Streamlit UI
┣ 📜 scrape.py          # Scraping logic
┣ 📜 parse.py           # AI parsing with Gemini
┣ 📜 requirements.txt   # Dependencies
┣ 📜 .env               # API key & secrets (not tracked in git)
┗ 📂 **pycache**/       # Python cache (ignored)

````

---

## ⚡ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Tom-1508/AI-Web-Scraper.git
cd AI-Web-Scraper
````

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Google API Key

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_api_key_here
```

### 5. Run the Streamlit app

```bash
streamlit run main.py
```

---

## 💡 Usage

1. Launch the Streamlit app.
2. Enter a website URL and click **"Scrape Site"**.
3. View the extracted DOM content.
4. Enter a natural language query (e.g., *"Extract all prices from the page"*).
5. Click **"Parse Content"** → Gemini will return only the requested data.

---

## 📝 Example Use Cases

* Extract product prices from e-commerce sites.
* Get article text without ads/scripts.
* Collect structured data from messy HTML.

---

## 🔒 Security Note

* Your `.env` file containing the **Google API Key** is excluded from Git (`.gitignore`).
* Do **not** commit `.env` or sensitive credentials.

---

## 📜 License

This project is licensed under the **MIT License**.
Feel free to use and modify it for your own projects.

---

## ✨ Author

👨‍💻 Developed by [**Tamal Majumdar**](https://github.com/Tom-1508)
💡 Inspired by modern AI-driven web scraping techniques.

```

---