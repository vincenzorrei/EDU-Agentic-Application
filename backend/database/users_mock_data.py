from typing import List, Dict, Any
from datetime import datetime, timedelta

def get_mock_conversations() -> List[Dict[str, Any]]:
    """
    Genera conversazioni mock per demo del sistema
    """
    base_date = datetime.now() - timedelta(days=30)
    
    return [
        {
            "user_id": "user001",
            "user_name": "Marco Rossi", 
            "date": (base_date + timedelta(days=1)).isoformat(),
            "preferences": [
                "thriller psicologici", 
                "fantascienza cerebrale", 
                "film con colpi di scena"
            ],
            "discussed_films": ["Inception", "The Dark Knight", "Interstellar"],
            "conversation_summary": """
            Marco ha mostrato forte interesse per i film di Christopher Nolan, 
            apprezzando particolarmente la complessità narrativa e i temi filosofici. 
            Ha definito Inception "un capolavoro che ti fa pensare per giorni" e 
            ha chiesto raccomandazioni simili. Preferisce film che richiedono 
            concentrazione e non ama le commedie leggere. Ha un abbonamento Premium.
            """,
            "preferred_moods": ["cerebrale", "intenso", "mind-bending", "complesso"],
            "liked_genres": ["Sci-Fi", "Thriller", "Mystery", "Drama"],
            "disliked_genres": ["Comedy", "Romance", "Horror"]
        },
        
        {
            "user_id": "user002", 
            "user_name": "Sofia Chen",
            "date": (base_date + timedelta(days=3)).isoformat(),
            "preferences": [
                "horror psicologico",
                "film d'atmosfera", 
                "thriller claustrofobici"
            ],
            "discussed_films": ["Get Out", "Hereditary", "The Conjuring"],
            "conversation_summary": """
            Sofia adora i film horror ma preferisce quelli psicologici a quelli splatter. 
            Ha elogiato Get Out come "perfetto equilibrio tra horror e critica sociale". 
            Cerca atmosfere inquietanti e tensione crescente piuttosto che jumpscare. 
            Ha mostrato interesse per il cinema di Jordan Peele e Ari Aster.
            """,
            "preferred_moods": ["inquietante", "teso", "atmospheric", "disturbante"],
            "liked_genres": ["Horror", "Thriller", "Mystery"],
            "disliked_genres": ["Action", "Comedy", "Romance"]
        },
        
        {
            "user_id": "user003",
            "user_name": "Alessandro Bianchi", 
            "date": (base_date + timedelta(days=7)).isoformat(),
            "preferences": [
                "film d'azione spettacolari",
                "blockbuster recenti",
                "superhero movies"
            ],
            "discussed_films": ["Top Gun: Maverick", "Spider-Man: No Way Home", "The Batman"],
            "conversation_summary": """
            Alessandro cerca principalmente intrattenimento puro e spettacolo. 
            Ha definito Top Gun: Maverick "adrenalina allo stato puro" e ama 
            gli effetti speciali di qualità. Preferisce film recenti con 
            budget elevati. Non disdegna film più vecchi se sono cult dell'azione.
            """,
            "preferred_moods": ["adrenalinico", "spettacolare", "epicpag", "energetic"],
            "liked_genres": ["Action", "Adventure", "Sci-Fi", "Superhero"],
            "disliked_genres": ["Drama", "Documentary", "Art House"]
        },
        
        {
            "user_id": "user004",
            "user_name": "Elena Martinelli",
            "date": (base_date + timedelta(days=12)).isoformat(), 
            "preferences": [
                "drammi toccanti",
                "storie di crescita personale",
                "film con messaggi profondi"
            ],
            "discussed_films": ["Parasite", "Marriage Story", "Little Women"],
            "conversation_summary": """
            Elena cerca film che la facciano riflettere e provare emozioni autentiche. 
            Ha pianto guardando Marriage Story e definito Parasite "un film che 
            cambia la prospettiva". Apprezza la cinematografia curata e le 
            performance attoriali intense. Evita violenza gratuita.
            """,
            "preferred_moods": ["emotivo", "riflessivo", "toccante", "profondo"],
            "liked_genres": ["Drama", "Romance", "Biography", "Art House"],
            "disliked_genres": ["Horror", "Action", "Sci-Fi"]
        },
        
        {
            "user_id": "user005",
            "user_name": "Luca Ferrari",
            "date": (base_date + timedelta(days=18)).isoformat(),
            "preferences": [
                "commedie intelligenti", 
                "film stravaganti",
                "regia autoriale"
            ],
            "discussed_films": ["The Grand Budapest Hotel", "Jojo Rabbit", "Knives Out"],
            "conversation_summary": """
            Luca ha un gusto molto particolare per commedie sofisticate e 
            film visivamente distintivi. Adora lo stile di Wes Anderson e 
            definisce The Grand Budapest Hotel "poesia visiva". Cerca 
            originalità e personalità autoriale forte nei film.
            """,
            "preferred_moods": ["whimsical", "stilizzato", "ironico", "colorato"],
            "liked_genres": ["Comedy", "Drama", "Mystery", "Art House"],
            "disliked_genres": ["Horror", "Thriller", "War"]
        },

                {
            "user_id": "vincenzo01",
            "user_name": "Vincenzo Romano", 
            "date": (base_date + timedelta(days=25)).isoformat(),
            "preferences": [
                "film d'azione adrenalinici",
                "thriller di spionaggio", 
                "film di guerra storici",
                "crime drama intensi"
            ],
            "discussed_films": ["Heat", "Casino Royale", "Saving Private Ryan", "The Departed", "Mad Max: Fury Road"],
            "conversation_summary": """
            Vincenzo è un appassionato di film d'azione sofisticati e thriller ben costruiti. 
            Ha definito Heat "il miglior film poliziesco mai realizzato" per la sua tensione 
            psicologica e le sequenze d'azione realistiche. Ama film con protagonisti 
            complessi e moralmente ambigui. Apprezza particolarmente Michael Mann, 
            Christopher Nolan e Denis Villeneuve. Cerca sempre film con ottime 
            coreografie d'azione e colonne sonore memorabili. Non ama commedie 
            leggere o film romantici, preferisce storie intense e cinematografia curata.
            """,
            "preferred_moods": ["intenso", "adrenalinico", "grintoso", "sophisticated", "noir"],
            "liked_genres": ["Action", "Thriller", "Crime", "War", "Spy", "Drama"],
            "disliked_genres": ["Comedy", "Romance", "Horror", "Fantasy", "Musical"]
        }
    ]
