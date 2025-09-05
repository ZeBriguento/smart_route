import { Itinerary } from "@/types/itinerary";
import { ProvinceDay } from "@/types/provinceDay";
import { Spot } from "@/types/spot";
import { Activity } from "@/types/activity";
import { MapPin, Leaf, Calendar, Bus, Wallet } from "lucide-react";

type Props = {
  itinerary: Itinerary;
};

export default function SuggestedItinerary({ itinerary }: Props) {
  return (
    <div className="p-6 bg-white shadow-xl rounded-2xl space-y-6 max-h-[80vh] overflow-hidden">
      <h2 className="text-2xl font-bold text-gray-800 mb-2">
        ✨ Roteiro Sugerido
      </h2>

      {/* Conteúdo rolável */}
      <div className="overflow-y-auto pr-2 max-h-[55vh] space-y-6">
        {itinerary.itinerary.map((provinceDay: ProvinceDay, i: number) => (
          <div
            key={i}
            className="bg-gray-50 border border-gray-200 rounded-xl p-4"
          >
            <h3 className="font-semibold text-lg text-blue-600 flex items-center gap-2 mb-3">
              <MapPin className="w-5 h-5" />
              Província: {provinceDay.province}
            </h3>

            {provinceDay.spots.map((spot: Spot, j: number) => (
              <div
                key={j}
                className="grid grid-cols-2 gap-4 items-center bg-white rounded-lg shadow-sm border p-3 mb-4"
              >
                {/* Esquerda → Texto */}
                <div className="space-y-2">
                  <h4 className="font-medium text-gray-700">
                    📍 {spot.name}
                  </h4>
                  <div className="flex flex-wrap gap-2">
                    {spot.activities.map((activity: Activity, k: number) => (
                      <span
                        key={k}
                        className="px-3 py-1 bg-blue-100 text-blue-700 text-sm rounded-full"
                      >
                        {activity.name}
                      </span>
                    ))}
                  </div>
                </div>

                {/* Direita → Imagem */}
                <div className="flex justify-center">
                  <img
                    src={"conceito-de-viagens-com-pontos-de-referencia.jpg"}
                    alt={spot.name}
                    className="w-full h-32 object-cover rounded-xl shadow"
                  />
                </div>
              </div>
            ))}
          </div>
        ))}
      </div>

      {/* Resumo */}
      <div className="bg-gray-100 rounded-xl p-4 grid grid-cols-2 gap-4 text-gray-700">
        <p className="flex items-center gap-2">
          <Leaf className="w-5 h-5 text-green-600" />
          <strong>CO₂ total:</strong> {itinerary.total_co2} kg
        </p>
        <p className="flex items-center gap-2">
          <Wallet className="w-5 h-5 text-yellow-600" />
          <strong>Orçamento:</strong> {itinerary.budget} Kz
        </p>
        <p className="flex items-center gap-2">
          <Calendar className="w-5 h-5 text-purple-600" />
          <strong>Dias:</strong> {itinerary.days}
        </p>
        <p className="flex items-center gap-2">
          <Bus className="w-5 h-5 text-red-600" />
          <strong>Transporte:</strong> {itinerary.transport_type}
        </p>
      {/*   <p className="col-span-2">
          <strong>Preferências:</strong> {itinerary.preferences.join(", ")}
        </p> */}
        <p className="col-span-2">
          <strong>Sugestões:</strong> {itinerary.suggestions.join(", ")}
        </p>
      </div>
    </div>
  );
}
