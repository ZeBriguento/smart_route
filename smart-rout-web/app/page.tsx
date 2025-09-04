"use client";

import { useState } from "react";
import PlanningForm from "@/components/planningForm";
import SuggestedItinerary from "@/components/suggestedItinerary";
import { generateItineraryController } from "@/controllers/itineraryController";
import { Itinerary } from "@/types/itinerary";

export default function Home() {
  const [itinerary, setItinerary] = useState<Itinerary | null>(null);
  const [loading, setLoading] = useState(false);

  const handleGenerateItinerary = async (
    days: number,
    budget: number,
    preferences: string[],
    transport_type: string
  ) => {
    setLoading(true);
    try {
      const result = await generateItineraryController({
        days,
        budget,
        preferences,
        transport_type,
      });
      setItinerary(result);
    } catch (error) {
      console.error("Erro ao gerar itinerário:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="flex min-h-screen p-8 gap-8">
      <div className="w-1/3">
        <PlanningForm onSubmit={handleGenerateItinerary} />
      </div>
      <div className="w-2/3">
        {loading && <p>Gerando roteiro...</p>}
        {itinerary && <SuggestedItinerary itinerary={itinerary} />}
      </div>
    </main>
  );
}
