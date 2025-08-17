import Link from "next/link";
export default function Home() {
  return (
    <main className="flex-grow flex flex-col items-center justify-center -mt-16 px-6 space-y-12">
      {/* Welcome Section */}
      <div className="text-center space-y-6">
        <h2 className="text-5xl font-extrabold tracking-tight text-white drop-shadow-lg">
          Welcome to MacroAnalyzer
        </h2>
        <p className="text-xl text-gray-400">
          Analyze and track macroeconomic news with clarity.
        </p>
      </div>

      {/* Two Sections Side by Side */}
      <div className="flex flex-col md:flex-row gap-8 w-full max-w-6xl">
        {/* Market Trends */}
        <Link href="/trends">
          <div className="flex-1 bg-gradient-to-br from-blue-700 to-blue-500 rounded-xl p-6 shadow-lg">
            <h3 className="text-2xl font-bold text-white text-center">Market Trends</h3>
            <p className="text-gray-200 mb-4 text-center">
              Visualize S&P 500 and other market indices.
            </p>
          </div>
        </Link>

        {/* Macro Analysis */}
        <Link href="/analysis">
          <div className="flex-1 bg-gradient-to-br from-green-700 to-green-500 rounded-xl p-6 shadow-lg">
            <h3 className="text-2xl font-bold text-white mb-4 text-center">Macro-Analysis</h3>
            <p className="text-gray-200 mb-4 text-center">
              AI-powered macroeconomic insights based on headlines.
            </p>
          </div>
        </Link>
      </div>
    </main>
  );
}
