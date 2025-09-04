from apps.itineraries.models import Province, TouristSpot, Activity, Transport
from typing import List, Dict, Any


class ItineraryRepository:

    @staticmethod
    def generate_itinerary(budget: float, days: int, preferences: List[str], transport_type: str) -> Dict[str, Any]:
        if days <= 0:
            return {"error": "Number of days must be greater than 0"}

        average_daily_cost = budget / days

        # 1. Selecionar províncias e pontos compatíveis
        provinces_data = ItineraryRepository._get_top_provinces(average_daily_cost, preferences)

        # 2. Calcular impacto ambiental
        total_co2 = ItineraryRepository._calculate_co2(transport_type, days)

        # 3. Gerar sugestões de sustentabilidade
        suggestions = ItineraryRepository._get_sustainability_suggestions(transport_type)

        # 4. Montar itinerário final
        return {
            "itinerary": provinces_data,
            "total_co2": total_co2,
            "budget": budget,
            "days": days,
            "transport_type": transport_type,
            "preferences": preferences,
            "suggestions": suggestions
        }

    @staticmethod
    def _get_top_provinces(average_daily_cost: float, preferences: List[str]) -> List[Dict[str, Any]]:
        provinces_data = []

        for province in Province.objects.all():
            spots_data = ItineraryRepository._get_spots_for_province(province, average_daily_cost, preferences)
            if spots_data:
                provinces_data.append({
                    "province": province.name,
                    "spots": spots_data
                })

        # Ordenar por quantidade de atividades e pegar até 3 províncias
        provinces_data.sort(key=lambda x: sum(len(spot["activities"]) for spot in x["spots"]), reverse=True)
        return provinces_data[:3]

    @staticmethod
    def _get_spots_for_province(province, average_daily_cost: float, preferences: List[str]) -> List[Dict[str, Any]]:
        spots_data = []

        spots = TouristSpot.objects.filter(province=province, average_daily_cost__lte=average_daily_cost)
        for spot in spots:
            activities = ItineraryRepository._get_activities_for_spot(spot, preferences)
            if activities:
                spots_data.append({
                    "name": spot.name,
                    "activities": activities
                })

        return spots_data

    @staticmethod
    def _get_activities_for_spot(spot, preferences: List[str]) -> List[str]:
        activities_qs = Activity.objects.filter(spot=spot)
        if preferences:
            activities_qs = activities_qs.filter(
                spot__preferences__preference_type__in=preferences
            ).distinct()

        return list(activities_qs.values_list("name", flat=True))

    @staticmethod
    def _calculate_co2(transport_type: str, days: int) -> float:
        try:
            transport = Transport.objects.get(name=transport_type)
            return transport.co2_emissions * days
        except Transport.DoesNotExist:
            return None

    @staticmethod
    def _get_sustainability_suggestions(transport_type: str) -> List[str]:
        suggestions = [
            "Troque o transporte por outro com menor CO2" if transport_type else None,
            "Use menos plástico durante as atividades",
            "Reduza consumo de água",
            "Escolha alimentação local"
        ]
        return [s for s in suggestions if s]
