import { ProvinceDay } from "@/types/provinceDay";

export interface Itinerary {
  itinerary: ProvinceDay[];
  total_co2: number;
  budget: number;
  days: number;
  transport_type: string;
  preferences: string[];
  suggestions: string[];
}