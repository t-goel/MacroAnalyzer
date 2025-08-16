export default function HomePage() {
  return (
    <section className="space-y-6">
      <h2 className="text-3xl font-bold">Welcome to MacroAnalyser</h2>
      <p className="text-lg text-gray-700">
        Track, analyze, and visualize macroeconomic news & indicators — powered by AI.
      </p>

      <div className="grid md:grid-cols-2 gap-6 mt-8">
        <div className="p-6 border rounded-xl bg-white shadow-sm">
          <h3 className="font-semibold text-xl">📈 Market Trends</h3>
          <p className="text-gray-600">Live updates on key global indicators.</p>
        </div>

        <div className="p-6 border rounded-xl bg-white shadow-sm">
          <h3 className="font-semibold text-xl">📰 News Sentiment</h3>
          <p className="text-gray-600">
            See how central banks, governments, and markets are being covered.
          </p>
        </div>
      </div>
    </section>
  );
}
