import { NextResponse } from "next/server";

export async function GET() {
  try {
    const apiKey = process.env.FMP_API_KEY;
    console.log("API key:", apiKey); // should now print your key

    const res = await fetch(`https://financialmodelingprep.com/api/v3/historical-price-full/VOO?apikey=${apiKey}`);
    if (!res.ok) throw new Error("Failed to fetch VOO data from FMP");

    const json = await res.json();

    // Return only the last 20 entries
    const last20 = json.historical.slice(0, 20).map((entry: any) => ({
      date: entry.date,
      close: entry.close,
    }));

    return NextResponse.json(last20);
  } catch (err) {
    console.error(err);
    return NextResponse.json({ error: "Failed to fetch" }, { status: 500 });
  }
}
