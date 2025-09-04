# apps/itineraries/repositories/preference_repository.py
from apps.itineraries.models import Preference
from typing import List, Dict

""" class PreferenceRepository:

    @staticmethod
    def list_preferences() -> List[str]:
       
       # Retorna todas as preferências únicas cadastradas no banco de dados.
       
        prefs = Preference.objects.values("preference_id", "preference_type").distinct()
        return [{"id": p["preference_id"], "preference_type": p["preference_type"]} for p in prefs]
 
        # Ajusta o dict para padronizar chave como 'id'
         """
class PreferenceRepository:

    @staticmethod
    def list_preferences() -> List[Dict]:
        """
        Retorna lista de preferências únicas, com id e tipo.
        """
        # Agrupa por preference_type e pega o primeiro id disponível
        prefs = (
            Preference.objects
            .values("preference_type")
            .distinct()
        )

        result = []
        for p in prefs:
            # Pega o id da primeira ocorrência de cada tipo
            first_id = Preference.objects.filter(preference_type=p["preference_type"]).values_list("preference_id", flat=True).first()
            result.append({"id": first_id, "preference_type": p["preference_type"]})
        
        return result