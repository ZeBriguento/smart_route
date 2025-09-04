export const API_URL = "http://localhost:8000/api"; // Backend Python

export async function apiFetch<T>(endpoint: string, options?: RequestInit): Promise<T> {
  const res = await fetch(`${API_URL}${endpoint}`, {
    headers: {
      "Content-Type": "application/json",
    },
    ...options,
  });

  if (!res.ok) {
    throw new Error(`Erro API: ${res.status}`);
  }

  return res.json();
}
