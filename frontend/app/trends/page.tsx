"use client";

import { useEffect, useState } from "react";
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";
import { fetchLast20VOO } from "../analysis/getVOO";

export default function SP500Chart() {
  const [data, setData] = useState<{ date: string; close: number }[]>([]);

  useEffect(() => {
    fetchLast20VOO()
      .then(setData)
      .catch(console.error);
  }, []);
  
  return (
    <div className="w-full h-96 p-4 bg-white rounded-xl shadow pb-12">
      <h2 className="text-xl font-bold mb-2 text-red-300">
        S&P 500 trends over the past 20 days (VOO)
      </h2>
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={data}>
          <XAxis dataKey="date" tickMargin={12} />
          <YAxis domain={["auto", "auto"]} />
          <Tooltip />
          <Line type="monotone" dataKey="close" stroke="#2563eb" strokeWidth={2} dot={false} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
