# apps/itineraries/repositories/transport_repository.py
from apps.itineraries.models import Transport
from typing import List, Dict

class TransportRepository:

    @staticmethod
    def list_transports() -> List[Dict[str, str]]:
        """
        Retorna todos os transportes disponíveis no banco de dados.
        Cada transporte é representado como um dicionário com id e nome.
        """
        transports = Transport.objects.all()
        return [{"id": t.id, "name": t.name} for t in transports]
