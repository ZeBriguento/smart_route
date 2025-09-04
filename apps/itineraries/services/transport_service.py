# apps/itineraries/services/transport_service.py
from apps.itineraries.repositories.transport_repository import TransportRepository
from typing import List, Dict

class TransportService:

    @staticmethod
    def list_transports() -> List[Dict[str, str]]:
        """
        Retorna todos os tipos de transporte disponíveis.
        """
        return TransportRepository.list_transports()
