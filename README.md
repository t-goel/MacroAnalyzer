# MacroAnalyzer 📈

**AI-Powered Macroeconomic News Sentiment Analysis & Market Forecasting**

MacroAnalyzer is a full-stack financial intelligence platform that quantifies the impact of global news on market behavior. By leveraging **Natural Language Processing (FinBERT)**, the system ingests real-time macroeconomic headlines, scores their sentiment, and correlates these signals with historical SPY/QQQ price movements to identify predictive market trends.

### 🛠 Tech Stack
* **Backend:** Python, FastAPI, SQLAlchemy, APScheduler
* **AI/ML:** PyTorch, Hugging Face Transformers (FinBERT), Scikit-learn
* **Frontend:** Next.js, React, Tailwind CSS, D3.js
* **Data:** PostgreSQL (Supabase), yfinance API, Docker

### 🚀 Key Features
* **Automated Data Pipeline:** Ingests and deduplicates real-time news from major financial RSS feeds (Fed, Reuters, WSJ).
* **NLP Sentiment Engine:** Utilizes FinBERT to assign probability scores (positive/negative/neutral) to financial headlines.
* **Market Correlation:** Overlays sentiment trends against historical stock data to visualize how news tone influences price action.
* **Interactive Visualization:** A responsive dashboard featuring time-series charts and sentiment heatmaps.
