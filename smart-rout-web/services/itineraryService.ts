import { apiFetch } from "./api";
import { Itinerary } from "@/types/itinerary";

type Params = {
  days: number;
  budget: number;
  preferences: string[];
  transport_type: string;
};

export async function generateItineraryService(params: Params): Promise<Itinerary> {
  return apiFetch<Itinerary>("/itineraries/generate/", {
    method: "POST",
    body: JSON.stringify(params),
  });
}
