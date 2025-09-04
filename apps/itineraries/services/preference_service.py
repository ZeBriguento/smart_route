# apps/itineraries/services/preference_service.py
from apps.itineraries.repositories.preference_repository import PreferenceRepository
from typing import List

class PreferenceService:

    @staticmethod
    def list_preferences() -> List[str]:
        """
        Retorna todas as preferências disponíveis para o frontend.
        """
        return PreferenceRepository.list_preferences()
