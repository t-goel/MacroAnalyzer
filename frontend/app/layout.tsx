import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";

export const metadata: Metadata = {
  title: "MacroAnalyser",
  description: "AI-powered insights on macroeconomic trends",
  icons: '/favicon.ico',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="flex flex-col min-h-screen">
        
        {/* Navigation Bar */}
        <nav className="w-full bg-gray-100 dark:bg-gray-800 p-4 flex items-center justify-start">
          <Link href="/" className="text-red-400">
            Home
          </Link>
        </nav>

        <main className="flex-1 flex items-center justify-center">
          {children}
        </main>

        <footer className="text-center py-4 border-t bg-gray-100 dark:bg-gray-800 text-sm text-gray-600 dark:text-gray-300">
          © {new Date().getFullYear()} All rights reserved.
        </footer>
      </body>
    </html>
  );
}