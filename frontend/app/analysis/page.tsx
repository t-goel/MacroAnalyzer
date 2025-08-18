// app/sentiment/page.tsx
"use client";

import { useEffect, useState } from "react";

interface SentimentData {
  source: string;
  positive: number;
  negative: number;
  neutral: number;
}

export default function SentimentPage() {
  const [data, setData] = useState<SentimentData[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      try {
        const res = await fetch("/api/sentiment"); // your API route
        const json = await res.json();
        setData(json);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, []);

  if (loading) return <p className="text-center mt-10">Loading...</p>;

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold mb-6 text-center">Financial Sentiment From the Headlines</h1>
      <div className="grid gap-6 md:grid-cols-2">
        {data.map((sourceData) => {
          const total = sourceData.positive + sourceData.negative + sourceData.neutral;
          const posWidth = (sourceData.positive / total) * 100;
          const negWidth = (sourceData.negative / total) * 100;
          const neuWidth = (sourceData.neutral / total) * 100;

          return (
            <div key={sourceData.source} className="border rounded-lg p-4 shadow hover:shadow-lg transition">
              <h2 className="text-xl font-semibold mb-2">{sourceData.source}</h2>
              <div className="flex mb-2 h-6 w-full bg-gray-200 rounded overflow-hidden">
                <div style={{ width: `${posWidth}%` }} className="bg-green-500"></div>
                <div style={{ width: `${neuWidth}%` }} className="bg-gray-400"></div>
                <div style={{ width: `${negWidth}%` }} className="bg-red-500"></div>
              </div>
              <div className="flex justify-between text-sm mt-1">
                <span>👍 {sourceData.positive}</span>
                <span>😐 {sourceData.neutral}</span>
                <span>👎 {sourceData.negative}</span>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
