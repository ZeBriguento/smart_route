from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from apps.itineraries.services.itinerary_service import ItineraryService
from apps.itineraries.services.preference_service import PreferenceService
from apps.itineraries.services.transport_service import TransportService

from apps.itineraries.serializers.itinerary_serializer import ItinerarySerializer





@api_view(["POST"])
def generate_itinerary(request):
    """
    Recebe orçamento, dias, preferências e transporte.
    Retorna itinerário gerado dinamicamente.
    """
    data = request.data
    days = data.get("days")
    budget = data.get("budget")
    preferences = data.get("preferences", [])
    transport = data.get("transport_type")

    itinerary = ItineraryService.generate_itinerary(days, budget, preferences, transport)
    serializer = ItinerarySerializer(itinerary)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def list_provinces(request):
    """
    Lista todas as províncias disponíveis.
    """
    provinces = ItineraryService.list_itineraries()
    provinces_data = [{"province_id": p.province_id, "name": p.name} for p in provinces]
    return Response(provinces_data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_province(request, province_id: int):
    """
    Retorna detalhes de uma província específica.
    """
    province = ItineraryService.get_itinerary(province_id)
    if not province:
        return Response({"error": "Province not found"}, status=status.HTTP_404_NOT_FOUND)

    province_data = {
        "province_id": province.province_id,
        "name": province.name,
        "description": province.description
    }
    return Response(province_data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_itinerary(request, itinerary_id: int):
    """
    Não implementado para itinerários dinâmicos.
    """
    return Response({"message": "Delete not implemented for dynamic itineraries"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def list_preferences(request):
    """
    Retorna todas as preferências disponíveis no sistema.
    """
    preferences = PreferenceService.list_preferences()
    return Response(preferences, status=status.HTTP_200_OK)

@api_view(["GET"])
def list_transports(request):
    """
    Retorna todos os tipos de transporte disponíveis.
    """
    transports = TransportService.list_transports()
    return Response(transports, status=status.HTTP_200_OK)