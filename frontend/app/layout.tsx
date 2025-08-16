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
      <body className="bg-gray-50 text-gray-900 font-sans">
        <header className="p-4 border-b bg-white shadow-sm flex justify-between items-center">
          <h1 className="text-xl font-bold">📊 MacroAnalyser</h1>
          <nav className="space-x-4">
            <a href="/" className="hover:underline">Home</a>
            <a href="/dashboard" className="hover:underline">Dashboard</a>
          </nav>
        </header>

        <main className="p-6 max-w-5xl mx-auto">{children}</main>

        <footer className="p-4 border-t bg-white text-center text-sm text-gray-600">
          &copy; {new Date().getFullYear()} MacroAnalyser · All rights reserved
        </footer>
      </body>
    </html>
  );
}
