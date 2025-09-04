import { generateItineraryService } from "@/services/itineraryService";
import { Itinerary } from "@/types/itinerary";

type Params = {
  days: number;
  budget: number;
  preferences: string[];
  transport_type: string;
};

export async function generateItineraryController(params: Params): Promise<Itinerary> {
  if (params.days <= 0) throw new Error("Número de dias inválido");
  if (params.budget <= 0) throw new Error("Orçamento inválido");
  return generateItineraryService(params);
}
