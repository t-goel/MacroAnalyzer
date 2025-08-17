import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "MacroAnalyser",
  description: "AI-powered insights on macroeconomic trends",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="flex flex-col min-h-screen">
        <header>
          <nav className="flex justify-between items-center px-6 py-4 bg-gray-100 dark:bg-gray-800 border-b">
            <div className="space-x-4">
              <a href="/" className="hover:text-blue-600">Home</a>
              <a href="/dashboard" className="hover:text-blue-600">Dashboard</a>
            </div>
            <h1 className="text-2xl font-bold text-blue-600">Macro Analyser</h1>
          </nav>
        </header>

        <main className="flex-1 flex items-center justify-center">{children}</main>

        <footer className="text-center py-4 border-t bg-gray-100 dark:bg-gray-800 text-sm text-gray-600 dark:text-gray-300">
          © {new Date().getFullYear()} All rights reserved.
        </footer>
      </body>
    </html>
  );
}
