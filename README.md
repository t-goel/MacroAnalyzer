# MacroAnalyzer
> **Quantifying the pulse of the market through AI-powered sentiment analysis of macroeconomic news.**

MacroAnalyzer is an intelligent web application designed to help users understand, visualize, and respond to macroeconomic events by quantifying the tone of financial news. By leveraging state-of-the-art NLP models, it provides actionable insights and predictive signals for market movements, enabling users to analyze sentiment trends alongside historical market data.

---

## 🚀 Features

- **Near Real-Time News Ingestion**: Automatically pulls from multiple top-tier RSS feeds (Federal Reserve, Financial Times, WSJ, Bloomberg) and filters deduplicated articles.
- **Advanced Sentiment Analysis**: Utilizes **FinBERT** (via Hugging Face Transformers) to score each headline and description for sentiment polarity (Positive, Negative, Neutral) and probability.
- **Historical Market Impact Tracking**: Fetches SPY and QQQ price data to compare sentiment shifts around major macroeconomic events (e.g., CPI releases, Fed meetings).
- **Interactive Visualizations**: Dynamic and filterable frontend charts built with **D3.js** displaying sentiment over time, price vs. sentiment correlation, and event-level breakdowns.
- **Data Deduplication & Cleanup**: Automated backend jobs manage database health by removing items older than a predefined threshold.

---

## 🛠️ Tech Stack

### **Backend**
- **Python 3.10+ / FastAPI**: Core API framework.
- **PostgreSQL (via Supabase)**: Database for storing news articles, sentiment scores, and events.
- **SQLAlchemy (ORM)**: Database interactions and modeling.
- **APScheduler**: Periodic cron jobs for RSS polling and sentiment scoring.
- **Transformers (Hugging Face)**: Running the local FinBERT models using PyTorch.
- **yfinance**: Fetching historical and current market data.

### **Frontend**
- **Next.js 15 (React 19)**: Frontend framework and React environment.
- **Tailwind CSS v4**: Utility-first styling for the modern UI.
- **D3.js & Recharts**: Interactive data visualizations.

---

## ⚙️ Prerequisites

- **Node.js**: v18 or newer
- **Python**: v3.10 or newer
- **PostgreSQL**: A Supabase instance or local PostgreSQL DB
- **Financial Modeling Prep API Key**: For fetching broader financial metrics (Optional but recommended)

---

## 🖥️ Local Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/t-goel/MacroAnalyzer.git
cd MacroAnalyzer
```

### 2. Backend Setup
Navigate to the backend directory and set up the Python environment:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: .\\venv\\Scripts\\activate
pip install -r requirements.txt
```

**Environment Variables (`backend/.env`)**
Create a `.env` file in the `backend/` directory:
```env
DATABASE_URL=postgresql://<user>:<password>@<host>:<port>/<dbname>
```

### 3. Frontend Setup
Navigate to the frontend directory and install dependencies:
```bash
cd ../frontend
npm install
```

**Environment Variables (`frontend/.env.local`)**
Create a `.env.local` file in the `frontend/` directory:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
FMP_API_KEY=your_fmp_api_key_here
```

---

## 🏃‍♂️ Running the Application

**1. Start the Backend API (and Schedulers)**
```bash
cd backend
source venv/bin/activate
uvicorn main:app --reload
```
The API will be available at `http://localhost:8000`.

**2. Start the Frontend Application**
Open a new terminal window:
```bash
cd frontend
npm run dev
```
The frontend will be available at `http://localhost:3000`.


