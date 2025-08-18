export async function fetchLast20VOO(): Promise<{ date: string; close: number }[]> {
    const res = await fetch("/api/voo");
    if (!res.ok) throw new Error("Failed to fetch VOO data");
    return res.json();
  }
  