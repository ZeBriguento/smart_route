from django.core.management.base import BaseCommand
from apps.itineraries.models import Province, TouristSpot, Activity, Transport, Preference

class Command(BaseCommand):
    help = "Popula o banco SQLite com dados completos para itinerários"

    def handle(self, *args, **kwargs):
        # --- Provinces ---
        provinces = [
            {"province_id": 1, "name": "Luanda", "description": "Capital de Angola, mistura de cultura e modernidade"},
            {"province_id": 2, "name": "Benguela", "description": "Cidade costeira famosa pelas praias"},
            {"province_id": 3, "name": "Lubango", "description": "Região de natureza e aventura"},
            {"province_id": 4, "name": "Cabinda", "description": "Praias e natureza exuberante"},
            {"province_id": 5, "name": "Huambo", "description": "Cultura e natureza"},
            {"province_id": 6, "name": "Namibe", "description": "Praias e deserto"},
            {"province_id": 7, "name": "Malanje", "description": "Natureza e cachoeiras"},
        ]
        for p in provinces:
            Province.objects.get_or_create(province_id=p["province_id"], defaults=p)

        # --- Transport ---
        transports = [
            {"id": 1, "name": "Autocarro", "co2_emissions": 20.0},
            {"id": 2, "name": "Carro", "co2_emissions": 50.0},
            {"id": 3, "name": "Avião", "co2_emissions": 200.0},
        ]
        for t in transports:
            Transport.objects.get_or_create(id=t["id"], defaults=t)

        # --- Tourist Spots ---
        spots = [
            # Luanda
            {"spot_id": 1, "name": "Museu Nacional", "description": "Museu de história e cultura", "average_daily_cost": 50.0, "province_id": 1},
            {"spot_id": 2, "name": "Ilha do Cabo", "description": "Praia e lazer", "average_daily_cost": 70.0, "province_id": 1},
            {"spot_id": 3, "name": "Fortaleza de São Miguel", "description": "Patrimônio histórico", "average_daily_cost": 60.0, "province_id": 1},
            # Benguela
            {"spot_id": 4, "name": "Praia do Lobito", "description": "Praia para banho e esportes aquáticos", "average_daily_cost": 60.0, "province_id": 2},
            {"spot_id": 5, "name": "Mercado de Benguela", "description": "Experiência gastronômica e cultural", "average_daily_cost": 40.0, "province_id": 2},
            # Lubango
            {"spot_id": 6, "name": "Serra da Leba", "description": "Trilhas e aventura", "average_daily_cost": 45.0, "province_id": 3},
            {"spot_id": 7, "name": "Museu do Sangro", "description": "Museu histórico e cultural", "average_daily_cost": 35.0, "province_id": 3},
            # Cabinda
            {"spot_id": 8, "name": "Parque Nacional de Cabinda", "description": "Natureza e fauna", "average_daily_cost": 70.0, "province_id": 4},
            {"spot_id": 9, "name": "Praia de Tchiowa", "description": "Praia e lazer", "average_daily_cost": 60.0, "province_id": 4},
            # Huambo
            {"spot_id": 10, "name": "Igreja São José", "description": "Patrimônio cultural", "average_daily_cost": 30.0, "province_id": 5},
            {"spot_id": 11, "name": "Lagoa do Mussende", "description": "Natureza e lazer", "average_daily_cost": 40.0, "province_id": 5},
            # Namibe
            {"spot_id": 12, "name": "Deserto do Namibe", "description": "Aventura no deserto", "average_daily_cost": 80.0, "province_id": 6},
            {"spot_id": 13, "name": "Praia do Ponto do Tal", "description": "Praia e descanso", "average_daily_cost": 60.0, "province_id": 6},
            # Malanje
            {"spot_id": 14, "name": "Cachoeiras Kalandula", "description": "Cachoeiras famosas", "average_daily_cost": 45.0, "province_id": 7},
            {"spot_id": 15, "name": "Parque Natural Morro de Cal", "description": "Natureza e trilhas", "average_daily_cost": 50.0, "province_id": 7},
        ]
        for s in spots:
            province = Province.objects.get(province_id=s["province_id"])
            TouristSpot.objects.get_or_create(
                spot_id=s["spot_id"],
                defaults={
                    "name": s["name"],
                    "description": s["description"],
                    "average_daily_cost": s["average_daily_cost"],
                    "province": province
                }
            )

        # --- Activities ---
        activities = [
            {"activity_id": 1, "name": "Visita guiada", "description": "Tour pelo museu", "spot_id": 1, "transport_id": 1},
            {"activity_id": 2, "name": "Banho de mar", "description": "Praia relaxante", "spot_id": 2, "transport_id": 2},
            {"activity_id": 3, "name": "Fotografia histórica", "description": "Fotos da fortaleza", "spot_id": 3, "transport_id": 1},
            {"activity_id": 4, "name": "Esportes aquáticos", "description": "Surf e stand-up", "spot_id": 4, "transport_id": 2},
            {"activity_id": 5, "name": "Compras locais", "description": "Experiência cultural e gastronômica", "spot_id": 5, "transport_id": 2},
            {"activity_id": 6, "name": "Trilha e aventura", "description": "Exploração da Serra da Leba", "spot_id": 6, "transport_id": 1},
            {"activity_id": 7, "name": "Museu histórico", "description": "Visita ao Museu do Sangro", "spot_id": 7, "transport_id": 1},
            {"activity_id": 8, "name": "Safari ecológico", "description": "Observação de animais", "spot_id": 8, "transport_id": 3},
            {"activity_id": 9, "name": "Relaxar na praia", "description": "Banho e descanso", "spot_id": 9, "transport_id": 2},
            {"activity_id": 10, "name": "Visita cultural", "description": "Igreja histórica", "spot_id": 10, "transport_id": 2},
            {"activity_id": 11, "name": "Passeio na lagoa", "description": "Passeio e lazer", "spot_id": 11, "transport_id": 1},
            {"activity_id": 12, "name": "Passeio de buggy", "description": "Exploração do deserto", "spot_id": 12, "transport_id": 3},
            {"activity_id": 13, "name": "Banho de sol", "description": "Praia e descanso", "spot_id": 13, "transport_id": 2},
            {"activity_id": 14, "name": "Fotografia das cachoeiras", "description": "Fotos da natureza", "spot_id": 14, "transport_id": 1},
            {"activity_id": 15, "name": "Trilhas ecológicas", "description": "Exploração do Parque Morro de Cal", "spot_id": 15, "transport_id": 1},
        ]
        for a in activities:
            spot = TouristSpot.objects.get(spot_id=a["spot_id"])
            transport = Transport.objects.get(id=a["transport_id"])
            Activity.objects.get_or_create(
                activity_id=a["activity_id"],
                defaults={
                    "name": a["name"],
                    "description": a["description"],
                    "spot": spot,
                    "transport": transport
                }
            )

        # --- Preferences ---
        preferences = [
            {"preference_id": 1, "spot_id": 1, "preference_type": "Cultural"},
            {"preference_id": 2, "spot_id": 2, "preference_type": "Praia"},
            {"preference_id": 3, "spot_id": 3, "preference_type": "Cultural"},
            {"preference_id": 4, "spot_id": 4, "preference_type": "Praia"},
            {"preference_id": 5, "spot_id": 5, "preference_type": "Gastronomia"},
            {"preference_id": 6, "spot_id": 6, "preference_type": "Aventura"},
            {"preference_id": 7, "spot_id": 7, "preference_type": "Cultural"},
            {"preference_id": 8, "spot_id": 8, "preference_type": "Natureza"},
            {"preference_id": 9, "spot_id": 9, "preference_type": "Praia"},
            {"preference_id": 10, "spot_id": 10, "preference_type": "Cultural"},
            {"preference_id": 11, "spot_id": 11, "preference_type": "Natureza"},
            {"preference_id": 12, "spot_id": 12, "preference_type": "Aventura"},
            {"preference_id": 13, "spot_id": 13, "preference_type": "Praia"},
            {"preference_id": 14, "spot_id": 14, "preference_type": "Natureza"},
            {"preference_id": 15, "spot_id": 15, "preference_type": "Natureza"},
        ]
        for p in preferences:
            spot = TouristSpot.objects.get(spot_id=p["spot_id"])
            Preference.objects.get_or_create(
                preference_id=p["preference_id"],
                defaults={
                    "spot": spot,
                    "preference_type": p["preference_type"]
                }
            )

        self.stdout.write(self.style.SUCCESS("✅ Banco populado com dados completos para itinerários!"))
