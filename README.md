# Macroanalyser
1. Purpose
MacroFactor is an AI-powered web application that helps users understand and respond to macroeconomic news. This update adds financial sentiment analysis to enhance insights by quantifying the tone of macroeconomic events and news, providing predictive signals for market movements, and allowing users to visualize sentiment trends alongside market data.

2. Goals & Objectives
Ingest macroeconomic news headlines and descriptions in near real-time.

Analyze sentiment using FinBERT, assigning each news item a positive, negative, or neutral score.

Store sentiment scores with news articles in the database.

Visualize sentiment trends alongside historical SPY/QQQ market data.

Correlate sentiment shifts with historical price movements to create actionable insights.

Enhance forecasting by including sentiment data in market prediction models.

3. Key Features
News Ingestion

Pull from multiple RSS feeds (e.g., Federal Reserve, Financial Times, Wall Street Journal, Bloomberg).

Store article title, description, publication date, and source.

Deduplicate articles and remove items older than 7 days automatically.

Sentiment Analysis

Use FinBERT to score each headline/description for sentiment polarity and probability.

Output format:

json
Copy
Edit
{
  "sentiment": "positive",
  "positive_score": 0.85,
  "negative_score": 0.05,
  "neutral_score": 0.10
}
Store results in sentiment columns in the NewsItem table.

Historical Market Impact

Fetch SPY and QQQ price data for the past 12 months.

Compare sentiment shifts around macroeconomic events (e.g., CPI releases, Fed meetings).

Identify statistically significant sentiment-market correlations.

Interactive Visualizations

Frontend charts using D3.js:

Sentiment over time (line chart)

Price vs. sentiment correlation

Event-level sentiment breakdown

Filters: date range, event type, sentiment type, source.

Forecasting

Include sentiment data as features in a simple ML model (e.g., logistic regression or gradient boosting) predicting next-day SPY/QQQ direction.

Show model confidence and backtest results.

Alerts

Optional: Trigger a frontend alert or email when sentiment deviates significantly from historical norms before a macro event.

4. Non-Goals
Full-text semantic analysis of entire articles (titles and descriptions only for v1).

High-frequency trading integration.

Real-time sub-second streaming (5-10 minute updates are sufficient).

5. Success Metrics
Accuracy of sentiment classification vs. human-labeled benchmark (≥80%).

Correlation strength (Pearson/Spearman) between sentiment shifts and market returns.

User engagement: Time spent interacting with sentiment visualizations.

Data freshness: News available within ≤ 10 minutes of publication.

6. Technical Requirements
Backend
Python / FastAPI for API.

PostgreSQL (Supabase) for storage.

SQLAlchemy ORM.

APScheduler for periodic jobs.

FinBERT via Hugging Face Transformers.

yfinance for market data.

Frontend
Next.js + Tailwind CSS.

D3.js for interactive charts.

API integration for fetching processed sentiment and market data.

Deployment
Supabase for DB hosting.

Vercel for frontend hosting.

Railway/Render/AWS for backend.

7. Risks & Mitigation
RSS Feeds with Minimal Data → Use APIs or scrape full text for richer sentiment analysis.

Model Accuracy on Finance Data → Test FinBERT and compare with alternative models (Cohere, OpenAI).

API Limits / Latency → Cache results, schedule less frequent updates.

