import { apiFetch } from "./api";
import { Preference } from "@/types/preference";

export async function listPreferences(): Promise<Preference[]> {
  return apiFetch<Preference[]>("/itineraries/preferences/");
}
