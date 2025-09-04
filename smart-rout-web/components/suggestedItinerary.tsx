import { Itinerary } from "@/types/itinerary";
import { ProvinceDay } from "@/types/provinceDay";
import { Spot } from "@/types/spot";
import { Activity } from "@/types/activity"; 

type Props = {
  itinerary: Itinerary;
};

export default function SuggestedItinerary({ itinerary }: Props) {
  return (
    <div className="p-4 bg-white shadow rounded-lg">
      <h2 className="text-xl font-bold mb-4">Itinerário Sugerido</h2>

      {itinerary.itinerary.map((provinceDay: ProvinceDay, i: number) => (
        <div key={i} className="mb-6">
          <h3 className="font-semibold text-lg">Província: {provinceDay.province}</h3>

          {provinceDay.spots.map((spot: Spot, j: number) => (
            <div key={j} className="ml-4 mb-4">
              <h4 className="font-medium">Ponto turístico: {spot.name}</h4>
              <ul className="list-disc ml-6">
             {spot.activities.map((activity: Activity, k: number) => (
  <li key={k}>{activity.name}</li>
))}

              </ul>
            </div>
          ))}
        </div>
      ))}

      <div className="mt-4">
        <p><strong>CO2 total:</strong> {itinerary.total_co2} kg</p>
        <p><strong>Orçamento:</strong> Kz {itinerary.budget}</p>
        <p><strong>Dias:</strong> {itinerary.days}</p>
        <p><strong>Transporte:</strong> {itinerary.transport_type}</p>
        <p><strong>Preferências:</strong> {itinerary.preferences.join(", ")}</p>
        <p><strong>Sugestões:</strong> {itinerary.suggestions.join(", ")}</p>
      </div>
    </div>
  );
}
