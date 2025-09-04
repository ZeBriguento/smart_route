from apps.itineraries.repositories.itinerary_repository import ItineraryRepository
from typing import List, Dict, Any


class ItineraryService:

    @staticmethod
    def generate_itinerary(days: int, budget: float, preferences: List[str], transport: str) -> Dict[str, Any]:
        """
        Gera itinerário dinâmico usando o ItineraryRepository.
        Retorna JSON pronto para o frontend.
        """
        return ItineraryRepository.generate_itinerary(
            budget=budget,
            days=days,
            preferences=preferences,
            transport_type=transport
        )

    @staticmethod
    def list_itineraries():
        """
        Opcional: pode listar todas as províncias ou itinerários salvos,
        dependendo da implementação que você quiser manter.
        """
        # Como não há mais Itinerary fixo, podemos retornar apenas províncias
        from apps.itineraries.models import Province
        return Province.objects.all()

    @staticmethod
    def get_itinerary(itinerary_id: int):
        """
        Opcional: se quiser pegar um itinerário específico por província.
        """
        from apps.itineraries.models import Province
        return Province.objects.filter(province_id=itinerary_id).first()

    @staticmethod
    def delete_itinerary(itinerary_id: int):
        """
        Deletar itinerário não faz sentido se não há registro persistido,
        então podemos manter vazio ou remover.
        """
        return {"message": "Delete not implemented for dynamic itineraries"}
