import { listPreferences } from "@/services/preferenceService";
import { Preference } from "@/types/preference";

export async function listPreferencesController(): Promise<Preference[]> {
  return listPreferences();
}
