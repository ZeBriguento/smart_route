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
    <main className="flex min-h-screen p-8 gap-8 bg-cover bg-center bg-no-repeat" style={{ backgroundImage: "url('conceito-de-viagem-completo-com-pontos-de-referencia.jpg')" }}>
      <div className="w-1/3 pt-32">
        <PlanningForm onSubmit={handleGenerateItinerary} />
      </div>
     <div className="w-2/3 pt-16 flex flex-col items-center justify-center">
  {loading && (
    <div className="flex flex-col items-center space-y-4">
      <div className="flex space-x-1">
        <div className="w-2 h-6 bg-blue-500 animate-bounce"></div>
        <div className="w-2 h-6 bg-blue-500 animate-bounce [animation-delay:-0.2s]"></div>
        <div className="w-2 h-6 bg-blue-500 animate-bounce [animation-delay:-0.4s]"></div>
      </div>
      <p className="text-blue-200 text-lg font-medium animate-pulse">
        Gerando roteiro...
      </p>
    </div>
  )}

  {itinerary && <SuggestedItinerary itinerary={itinerary} />}
</div>

    </main>
  );
}
