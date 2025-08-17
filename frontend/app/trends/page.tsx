"use client";

import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, Label} from "recharts";

const data = [
  { date: "2025-08-10", close: 520 },
  { date: "2025-08-11", close: 523 },
  { date: "2025-08-12", close: 518 },
];

export default function SP500Chart() {
  return (
    <div className="w-full h-96 p-4 bg-white rounded-xl shadow pb-12">
      <h2 className="text-xl font-bold mb-2 text-red-300">S&P 500 Trends over the past 20 days</h2>
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={data}>
          <XAxis dataKey="date" tickMargin={12}/>
          <YAxis domain={["auto", "auto"]}/>
          <Tooltip />
          <Line type="monotone" dataKey="close" stroke="#2563eb" strokeWidth={2} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}