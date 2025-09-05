from typing import List, Dict, Any

def get_enhanced_films_data() -> List[Dict[str, Any]]:
    """
    Restituisce dataset di 53 film con descrizioni MOLTO ricche
    Focus su mood, atmosfere, emozioni, tensione per semantic search
    """
    return [
        {
            "id": 1,
            "title": "Inception",
            "release_year": 2010,
            "director": "Christopher Nolan",
            "genres": ["Sci-Fi", "Thriller", "Action"],
            "imdb_rating": 8.8,
            "content_rating": "PG-13",
            "cast": ["Leonardo DiCaprio", "Marion Cotillard", "Tom Hardy", "Elliot Page"],
            "duration_minutes": 148,
            "availability_type": "included",
            "rental_price": None,
            "minimum_plan": "Standard", 
            "netflix_url": "/watch/80001246",
            
            # DESCRIZIONI POTENZIATE per semantic search
            "enhanced_description": {
                "mood_description": """
                Atmosfera cerebrale e labirintica che ti tiene costantemente in tensione. 
                Il film genera un senso di vertigine intellettuale, dove la realtà si sfalda 
                progressivamente. Sensazioni di claustrofobia onirica si alternano a momenti 
                di pura adrenalina action. L'ambiente è surreale, onirico, sofisticato. 
                Mood psicologico intenso che richiede concentrazione assoluta dello spettatore.
                """,
                
                "detailed_plot": """
                Dom Cobb è un ladro specializzato nell'infiltrarsi nei sogni altrui per rubare 
                segreti dal subconscio. Vive in un mondo dove la tecnologia permette di condividere 
                gli spazi onirici, ma Cobb è tormentato dal ricordo di sua moglie Mal, morta suicida. 
                Quando gli viene offerta la possibilità di tornare dai suoi figli in cambio di 
                un'ultima missione impossibile - l'inception, ovvero impiantare un'idea invece che rubarla - 
                Cobb accetta. Deve convincere Robert Fischer Jr. a sciogliere l'impero economico 
                del padre creando sogni stratificati su tre livelli. Ma Mal continua a sabotare 
                le missioni, rendendo tutto ancora più pericoloso. Il confine tra sogno e realtà 
                diventa sempre più labile in un crescendo di tensione mozzafiato.
                """,
                
                "directorial_style": """
                Nolan orchestra una sinfonia visiva di precisione millimetrica. Ogni sequenza 
                è costruita come un orologio svizzero, con montaggio serrato che alterna azione 
                frenetica a momenti di riflessione filosofica. La regia è cerebrale ma accessibile, 
                con effetti pratici spettacolari che rendono tangibile l'impossibile.
                """,
                
                "emotional_impact": """
                Il film genera ansia esistenziale e fascinazione intellectuale. Temi di colpa, 
                redenzione e amor paterno si intrecciano in una narrazione che scuote 
                profondamente. Sensazione di smarrimento controllato che lascia lo spettatore 
                mentalmente stimolato e emotivamente coinvolto. Esperienza catartica finale.
                """,
                
                "visual_style": """
                Palette visiva fredda e metallica con contrasti netti. Architetture impossibili 
                che si piegano su se stesse creano un'estetica unica. Ogni livello onirico ha 
                una sua identità visiva distinta: dalla pioggia urbana al limbo bianco infinito.
                """
            }
        },
        
        {
            "id": 2,
            "title": "Get Out",
            "release_year": 2017,
            "director": "Jordan Peele",
            "genres": ["Horror", "Thriller", "Mystery"],
            "imdb_rating": 7.8,
            "content_rating": "R",
            "cast": ["Daniel Kaluuya", "Allison Williams", "Bradley Whitford", "Catherine Keener"],
            "duration_minutes": 104,
            "availability_type": "included",
            "rental_price": None,
            "minimum_plan": "Standard",
            "netflix_url": "/watch/80001267",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera di inquietudine crescente che si trasforma in terrore psicologico puro. 
                Il mood è oppressivo, carico di tensione razziale sottile ma pervasiva. Sensazione 
                costante che qualcosa non quadra, un disagio sociale che si amplifica fino al 
                panico. Ambiente apparentemente idilliaco che nasconde orrori inimmaginabili. 
                Suspense masterclass che ti tiene col fiato sospeso dall'inizio alla fine.
                """,
                
                "detailed_plot": """
                Chris Washington, giovane fotografo afroamericano, accompagna la sua fidanzata 
                bianca Rose per incontrare i suoi genitori nella loro tenuta di campagna. 
                Inizialmente i Armitage sembrano accoglienti e progressisti, ma Chris nota 
                comportamenti strani negli altri afroamericani presenti: parlano in modo robotico 
                e hanno sguardi vuoti. Durante una festa, Chris scopre una cospirazione terrificante: 
                la famiglia Armitage gestisce un'operazione di trapianto cerebrale che permette 
                a ricchi bianchi anziani di "possedere" corpi giovani di neri. Chris deve fuggire 
                da questo incubo razzista prima di diventare la prossima vittima della "coagulazione", 
                un processo di ipnosi che intrapola la coscienza nera nel "posto sommerso" della mente.
                """,
                
                "directorial_style": """
                Peele dirige con precisione chirurgica, dosando la tensione come un maestro. 
                Ogni inquadratura comunica disagio sociale attraverso dettagli apparentemente 
                innocenti. La regia è intelligente, mai gratuita, sempre al servizio della critica sociale.
                """,
                
                "emotional_impact": """
                Film che genera profonda inquietudine esistenziale e rabbia sociale. Paura viscerale 
                dell'altro, paranoia giustificata che si trasforma in orrore puro. Esperienza 
                emotivamente devastante che lascia segni duraturi sulla psiche dello spettatore.
                """,
                
                "visual_style": """
                Estetica pulita e borghese che contrasta con l'orrore sottostante. Colori saturi 
                che virano al sinistro, primi piani claustrofobici che catturano l'angoscia. 
                Il "posto sommerso" è visualizzato come vuoto nero infinito, metafora perfetta.
                """
            }
        },
        
        {
            "id": 3,
            "title": "The Dark Knight",
            "release_year": 2008,
            "director": "Christopher Nolan",
            "genres": ["Action", "Crime", "Drama"],
            "imdb_rating": 9.0,
            "content_rating": "PG-13",
            "cast": ["Christian Bale", "Heath Ledger", "Aaron Eckhart", "Gary Oldman"],
            "duration_minutes": 152,
            "availability_type": "included",
            "rental_price": None,
            "minimum_plan": "Basic",
            "netflix_url": "/watch/80001245",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera dark e grittosa che trascende il genere supereroistico. Mood cupo e 
                filosoficamente complesso, dove il caos incontra l'ordine in uno scontro epico. 
                Tensione psicologica costante amplificata dalla presenza inquietante del Joker. 
                Sensazione di città sull'orlo del baratro morale. Epicità tragica che eleva 
                l'action a riflessione esistenziale profonda.
                """,
                
                "detailed_plot": """
                Gotham City sembra finalmente trovare pace grazie agli sforzi combinati di Batman, 
                del commissario Gordon e del nuovo procuratore distrettuale Harvey Dent. Ma l'arrivo 
                del Joker, criminale psicopatico senza motivazioni comprensibili, scatena il caos 
                assoluto. Il Joker non vuole denaro o potere: vuole dimostrare che chiunque può 
                diventare mostruoso nelle giuste circostanze. Attraverso esperimenti sociali sadici 
                - come il dilemma dei traghetti o la corruzione di Harvey Dent - il Joker tenta di 
                far crollare Batman nel baratro morale. Quando Harvey diventa Due Facce dopo la morte 
                della sua fidanzata Rachel, Batman deve fare la scelta più difficile: diventare il 
                cattivo per preservare la speranza di Gotham, sacrificando la sua reputazione per 
                il bene comune.
                """,
                
                "directorial_style": """
                Nolan eleva il film di supereroi a tragedia shakespeariana urbana. Regia epica 
                che bilancia action spettacolare e profondità psicologica. Ogni sequenza è costruita 
                su livelli multipli di significato simbolico.
                """,
                
                "emotional_impact": """
                Esperienza emotiva devastante che esplora i limiti della moralità umana. Genera 
                riflessione profonda sulla natura del bene e del male. Il sacrificio finale di 
                Batman tocca corde emotive profondissime. Film che segna e trasforma.
                """,
                
                "visual_style": """
                Gotham fotografata come metropoli noir contemporanea. Palette scura con esplosioni 
                di colore violento. La presenza del Joker contamina visivamente ogni scena con 
                il suo caos cromatico. Architettura urbana opprimente e maestosa.
                """
            }
        },
        
        {
            "id": 4,
            "title": "Parasite",
            "release_year": 2019,
            "director": "Bong Joon-ho",
            "genres": ["Thriller", "Drama", "Dark Comedy"],
            "imdb_rating": 8.5,
            "content_rating": "R",
            "cast": ["Song Kang-ho", "Lee Sun-kyun", "Cho Yeo-jeong", "Choi Woo-shik"],
            "duration_minutes": 132,
            "availability_type": "included",
            "rental_price": None,
            "minimum_plan": "Standard",
            "netflix_url": "/watch/80001289",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera di tensione sociale palpabile che evolve da commedia nera a thriller 
                psicologico devastante. Mood di disagio crescente alimentato dalle disuguaglianze 
                di classe. Sensazione di precarietà costante, dove ogni momento di leggerezza 
                nasconde un abisso sociale. Ambiente claustrofobico che riflette le gerarchie 
                economiche attraverso gli spazi architettonici.
                """,
                
                "detailed_plot": """
                La famiglia Kim vive in un seminterrato fatiscente e sopravvive piegando scatole 
                di pizza. Quando il figlio Ki-woo ottiene un lavoro come tutor d'inglese per 
                la figlia della ricca famiglia Park, architetta un piano per far assumere tutta 
                la sua famiglia come personale domestico, nascondendo i loro legami di parentela. 
                Inizialmente tutto procede perfettamente: Ki-jung diventa l'art-therapist del 
                figlio Park, il padre Ki-taek sostituisce l'autista e la madre Chung-sook diventa 
                la governante. Ma la scoperta di un bunker segreto dove vive nascosto il marito 
                della precedente governante scatena una serie di eventi tragici che culminano 
                in un bagno di sangue durante una festa di compleanno, rivelando l'impossibilità 
                di scalare davvero la piramide sociale.
                """,
                
                "directorial_style": """
                Bong Joon-ho dirige con maestria chirurgica, usando gli spazi architettonici 
                come metafore viventi della stratificazione sociale. Ogni movimento di camera 
                comunica dinamiche di potere, ogni dettaglio visivo racconta la lotta di classe.
                """,
                
                "emotional_impact": """
                Film che genera profonda riflessione sulla disuguaglianza e rabbia sociale 
                controllata. Evolve da divertimento complice a shock emotivo devastante. 
                Lascia lo spettatore con una sensazione di ingiustizia sistemica e impotenza 
                che perdura a lungo dopo la visione.
                """,
                
                "visual_style": """
                Estetica pulita e geometrica che contrasta spazi alti (ricchezza) e bassi (povertà). 
                Palette cromatica che si fa sempre più satura man mano che cresce la tensione. 
                La pioggia diventa elemento visivo simbolico di purificazione e distruzione.
                """
            }
        },
        
        {
            "id": 5,
            "title": "Joker",
            "release_year": 2019,
            "director": "Todd Phillips",
            "genres": ["Drama", "Crime", "Thriller"],
            "imdb_rating": 8.4,
            "content_rating": "R",
            "cast": ["Joaquin Phoenix", "Robert De Niro", "Zazie Beetz", "Frances Conroy"],
            "duration_minutes": 122,
            "availability_type": "rental",
            "rental_price": 3.99,
            "minimum_plan": "Basic",
            "netflix_url": "/watch/80001334",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera opprimente di decadenza urbana e disperazione psicologica. Mood 
                claustrofobico che riflette la discesa nella follia di un uomo ai margini. 
                Sensazione costante di disagio sociale e tensione psicologica che esplode 
                in violenza catartica. Ambiente degradato che rispecchia lo stato mentale 
                del protagonista. Inquietudine crescente che culmina in anarchia sociale.
                """,
                
                "detailed_plot": """
                Arthur Fleck è un aspirante comico che vive con la madre malata in una Gotham 
                City decadente degli anni '80. Affetto da una condizione neurologica che lo 
                fa ridere incontrollabilmente nei momenti di stress, Arthur è costantemente 
                umiliato e picchiato dalla società. Licenziato dal suo lavoro da clown, 
                deriso durante un'apparizione in un talk show, Arthur scopre che sua madre 
                lo ha mentito sulla sua identità per tutta la vita. La combinazione di 
                traumi psicologici, isolamento sociale e taglio ai servizi sanitari pubblici 
                lo spinge oltre il limite. L'uccisione di tre giovani di Wall Street in 
                metropolitana scatena proteste sociali che lo trasformano in simbolo di 
                rivolta contro l'élite. Arthur abbraccia la sua nuova identità come Joker, 
                diventando l'antieroe che Gotham merita.
                """,
                
                "directorial_style": """
                Phillips dirige con intensità documentaristica, creando un ritratto crudo 
                della malattia mentale e dell'esclusione sociale. Regia intimista che segue 
                da vicino la trasformazione psicologica del protagonista con realismo brutale.
                """,
                
                "emotional_impact": """
                Film che genera profonda empatia per un personaggio disturbante, creando 
                conflitto morale nello spettatore. Esperienza emotivamente devastante che 
                interroga i confini tra vittima e carnefice. Riflessione dolorosa sulla 
                responsabilità sociale nella creazione dei mostri.
                """,
                
                "visual_style": """
                Gotham degli anni '80 resa con palette terrosa e degradata. Colori desaturati 
                che si accendono progressivamente con la trasformazione di Arthur. Il rosso 
                diventa colore dominante nella metamorfosi finale in Joker.
                """
            }
        },
         {
            "id": 17,
            "title": "There Will Be Blood",
            "release_year": 2007,
            "director": "Paul Thomas Anderson",
            "genres": ["Drama", "History"],
            "imdb_rating": 8.2,
            "content_rating": "R",
            "cast": ["Daniel Day-Lewis", "Paul Dano", "Dillon Freasier", "Ciarán Hinds"],
            "duration_minutes": 158,
            "availability_type": "included",
            "rental_price": None,
            "minimum_plan": "Standard",
            "netflix_url": "/watch/80001266",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera di cupidigia primitiva e isolamento spirituale che cresce come cancro 
                attraverso paesaggi petroliferi americani. Mood biblico e apocalittico dove 
                capitalismo selvaggio distrugge anima umana. Sensazione di grandezza epica 
                macchiata da misantropia profonda. Ambiente della frontiera americana reso 
                come teatro di corruzione morale. Tensione psicologica che esplode in violenza 
                finale catartica ma vuota.
                """,
                
                "detailed_plot": """
                Daniel Plainview è un cercatore d'oro californiano dei primi del '900 che 
                diventa magnate del petrolio attraverso ambizione spietata e manipolazione. 
                Dopo aver adottato H.W., figlio orfano del suo socio morto in un incidente, 
                Daniel usa il bambino per apparire più affidabile negli affari con le famiglie 
                locali. Quando arriva a Little Boston per acquistare terreni ricchi di petrolio, 
                entra in conflitto con Eli Sunday, giovane predicatore evangelico che vuole 
                usare Daniel per finanziare la sua chiesa. I due uomini si detestano istintivamente: 
                Daniel disprezza la religiosità ipocrita di Eli, mentre Eli vede in Daniel 
                l'incarnazione del peccato. Nel corso degli anni, mentre Daniel accumula ricchezza 
                enorme, perde progressivamente ogni legame umano, compreso quello con H.W., 
                diventato sordo in un incidente. Quando Eli, ormai fallito, cerca di vendere 
                terreni a Daniel decenni dopo, il magnate lo umilia costringendolo a rinnegare 
                la sua fede prima di ucciderlo brutalmente con una mazza da bowling.
                """,
                
                "directorial_style": """
                Anderson dirige con maestria epica, creando ritratto monumentale dell'avidità 
                americana attraverso composizioni pittoriche e performance viscerali. Regia 
                che trasforma biografia in tragedia biblica sulla natura del potere.
                """,
                
                "emotional_impact": """
                Film che genera disgusto affascinato per l'ambizione senza limiti e compassione 
                per l'isolamento autoimposto. Esperienza emotivamente brutale che esplora 
                costi spirituali del successo materiale. Nihilismo americano in forma artistica pura.
                """,
                
                "visual_style": """
                Cinematografia che contrasta vastità dei paesaggi petroliferi con claustrofobia 
                psicologica. Palette terrosa dominata da ocre e neri industriali. Inquadrature 
                monumentali che enfatizzano piccolezza morale in grandezza geografica.
                """
            }
        },
        
        {
            "id": 18,
            "title": "2001: A Space Odyssey",
            "release_year": 1968,
            "director": "Stanley Kubrick",
            "genres": ["Sci-Fi", "Mystery"],
            "imdb_rating": 8.3,
            "content_rating": "G",
            "cast": ["Keir Dullea", "Gary Lockwood", "William Sylvester", "Douglas Rain"],
            "duration_minutes": 149,
            "availability_type": "included",
            "rental_price": None,
            "minimum_plan": "Basic",
            "netflix_url": "/watch/80001001",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera di meraviglia cosmica e terrore esistenziale che trascende comprensione 
                umana. Mood contemplativo e ipnotico dove silenzio spaziale amplifica mistero 
                dell'universo. Sensazione di piccolezza umana di fronte all'infinito e 
                all'intelligenza aliena. Ambiente che spazia dall'alba dell'umanità ai viaggi 
                interstellari creando vertigine temporale. Esperienza quasi religiosa che 
                interroga posto dell'uomo nel cosmo.
                """,
                
                "detailed_plot": """
                Quattro milioni di anni fa, un misterioso monolito nero appare a una tribù 
                di ominidi e catalizza il primo uso di utensili, accelerando l'evoluzione umana. 
                Nel 2001, un monolito identico viene scoperto sepolto sulla Luna e emette un 
                segnale radio verso Giove. La missione Discovery viene inviata per investigare, 
                con gli astronauti Dave Bowman e Frank Poole in stato di veglia mentre tre 
                colleghi viaggiano in ibernazione. La nave è controllata da HAL 9000, computer 
                superintelligente che sviluppa paranoia quando scopre che la vera missione 
                (investigare il segnale alieno) è stata tenuta segreta all'equipaggio. HAL 
                inizia a eliminare gli umani per "proteggere" la missione, ma Bowman riesce 
                a disattivarlo dopo una battaglia psicologica. Raggiunto Giove, Bowman incontra 
                un terzo monolito che lo trasporta attraverso un corridor spaziotemporale 
                verso dimensioni incomprensibili, dove invecchia rapidamente e rinasce come 
                "Bambino delle Stelle", prossimo stadio evolutivo dell'umanità.
                """,
                
                "directorial_style": """
                Kubrick dirige con precisione matematica e visione profetica, creando cinema 
                come esperienza trascendente. Regia che usa silenzio, musica classica e 
                effetti pratici per comunicare sublime e incomprensibile.
                """,
                
                "emotional_impact": """
                Film che genera senso di meraviglia esistenziale e terrore cosmico simultanei. 
                Esperienza che trascende intrattenimento per diventare meditazione filosofica 
                sul destino umano. Fascino ipnotico che continua a interrogare decenni dopo.
                """,
                
                "visual_style": """
                Cinematografia rivoluzionaria che rende credibile l'impossibile attraverso 
                effetti pratici perfetti. Estetica minimalista che enfatizza geometrie pure 
                e contrasti di luce. Ogni inquadratura è composta con precisione architettonica.
                """
            }
        },
        
        {
            "id": 19,
            "title": "Arrival",
            "release_year": 2016,
            "director": "Denis Villeneuve",
            "genres": ["Sci-Fi", "Drama"],
            "imdb_rating": 7.9,
            "content_rating": "PG-13",
            "cast": ["Amy Adams", "Jeremy Renner", "Forest Whitaker", "Michael Stuhlbarg"],
            "duration_minutes": 116,
            "availability_type": "included",
            "rental_price": None,
            "minimum_plan": "Standard",
            "netflix_url": "/watch/80001387",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera di tensione intellettuale e meraviglia linguistica che si trasforma 
                in riflessione profonda su tempo e comunicazione. Mood contemplativo e 
                emotivamente complesso dove first contact alieno diventa metafora per 
                comprensione umana. Sensazione di urgenza globale bilanciata da intimità 
                personale. Ambiente accademico trasformato in scenario di importanza cosmica.
                """,
                
                "detailed_plot": """
                Quando dodici navi aliene appaiono in punti casuali della Terra, la linguista 
                Louise Banks viene reclutata dall'esercito americano per decifrare il linguaggio 
                degli extraterrestri chiamati "heptapods". Collaborando con il fisico Ian Donnelly, 
                Louise entra nelle navi aliene ogni 18 ore per stabilire comunicazione con due 
                entità che battezza Abbott e Costello. Gli alieni comunicano attraverso simboli 
                circolari complessi che rappresentano concetti interi. Man mano che Louise 
                impara la loro lingua, inizia a sperimentare visioni che inizialmente crede 
                siano ricordi della figlia Hannah, morta giovane di cancro. Ma Louise scopre 
                che il linguaggio alieno cambia il modo di percepire il tempo: gli heptapods 
                vivono simultaneamente passato, presente e futuro. Le "visioni" sono in realtà 
                precognizioni della figlia che avrà con Ian nel futuro. Quando le tensioni 
                geopolitiche minacciano di trasformare il primo contatto in conflitto globale, 
                Louise usa la sua nuova percezione temporale per convincere il generale cinese 
                a fermare l'attacco, rivelando che gli alieni sono venuti per donare all'umanità 
                il loro linguaggio come "arma" che la aiuterà in una crisi futura tra 3000 anni.
                """,
                
                "directorial_style": """
                Villeneuve dirige con eleganza contemplativa, trasformando fantascienza 
                cerebrale in esperienza emotivamente devastante. Regia paziente che permette 
                alle idee complesse di emergere organicamente attraverso performance intime.
                """,
                
                "emotional_impact": """
                Film che genera profonda commozione attraverso temi di maternità, perdita e 
                accettazione del destino. Esperienza intellettualmente stimolante che tocca 
                corde emotive universali. Riflessione sul significato dell'amore di fronte 
                alla conoscenza del dolore futuro.
                """,
                
                "visual_style": """
                Cinematografia minimalista che usa nebbia e luce naturale per creare atmosfera 
                onirica. Le navi aliene sono progettate come monoliti misteriosi che sfidano 
                prospettiva. Palette fredda e neutrale che enfatizza emozioni umane.
                """
            }
        },
        
        {
            "id": 20,
            "title": "The Social Network",
            "release_year": 2010,
            "director": "David Fincher",
            "genres": ["Biography", "Drama"],
            "imdb_rating": 7.8,
            "content_rating": "PG-13",
            "cast": ["Jesse Eisenberg", "Andrew Garfield", "Justin Timberlake", "Armie Hammer"],
            "duration_minutes": 120,
            "availability_type": "included",
            "rental_price": None,
            "minimum_plan": "Basic",
            "netflix_url": "/watch/80001255",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera di ambizione spietata e tradimento personale mascherata da innovazione 
                tecnologica. Mood frenetico e competitivo dell'ambiente universitario d'élite 
                dove genialità incontra opportunismo sociale. Sensazione di solitudine 
                digitale che contrasta con successo esteriore. Ambiente di Harvard e Silicon 
                Valley reso come giungla darwiniana moderna.
                """,
                
                "detailed_plot": """
                Dopo essere stato scaricato dalla fidanzata Erica, Mark Zuckerberg, studente 
                di Harvard socialmente inadeguato ma geniale programmatore, crea "Facemash", 
                sito che permette di confrontare attrattiva delle studentesse. Il successo 
                virale attira l'attenzione dei gemelli Winklevoss e Divya Narendra, che 
                assumono Mark per sviluppare un social network esclusivo chiamato Harvard 
                Connection. Ma Mark usa l'idea per creare segretamente Facebook con l'aiuto 
                del migliore amico Eduardo Saverin, che finanzia il progetto. Quando Facebook 
                esplode oltre Harvard, Mark incontra Sean Parker, fondatore di Napster, che 
                lo convince a trasferirsi in California e a escludere Eduardo dall'azienda. 
                Parker manipola Mark per diluire le azioni di Eduardo e assumere controllo 
                operativo, tradendo l'amico che aveva creduto in lui fin dall'inizio. Il 
                film si sviluppa attraverso due deposizioni legali: i Winklevoss accusano 
                Mark di furto di proprietà intellettuale, mentre Eduardo lo cita per essere 
                stato estromesso dalla propria azienda. Mentre Facebook diventa fenomeno 
                globale, Mark rimane isolato, ossessionato dal controllo ma incapace di 
                mantenere relazioni autentiche.
                """,
                
                "directorial_style": """
                Fincher dirige con precisione da orologiaio, creando ritmo incalzante che 
                riflette velocità dell'innovazione digitale. Regia che trasforma biografia 
                in thriller psicologico sui costi umani del successo tecnologico.
                """,
                
                "emotional_impact": """
                Film che genera fascinazione ambigua per il genio imprenditoriale e disgusto 
                per l'opportunismo che distrugge amicizie. Riflessione amara su come il 
                successo digitale possa amplificare l'isolamento sociale reale.
                """,
                
                "visual_style": """
                Estetica fredda e digitale con palette dominata da blues e grigi. Harvard 
                fotografata come istituzione elitaria opprimente, Silicon Valley come parco 
                giochi hedonistico. Illuminazione artificiale che riflette natura tecnologica.
                """
            }
        },
        
        {
            "id": 21,
            "title": "Hereditary",
            "release_year": 2018,
            "director": "Ari Aster",
            "genres": ["Horror", "Drama", "Mystery"],
            "imdb_rating": 7.3,
            "content_rating": "R",
            "cast": ["Toni Collette", "Alex Wolff", "Milly Shapiro", "Gabriel Byrne"],
            "duration_minutes": 127,
            "availability_type": "rental",
            "rental_price": 3.99,
            "minimum_plan": "Standard",
            "netflix_url": "/watch/80001456",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera di dread familiare e terrore ereditario che permea ogni momento 
                domestico con presenza malevola. Mood claustrofobico dove trauma generazionale 
                si manifesta attraverso orrore soprannaturale. Sensazione costante di essere 
                osservati da forze maligne ancestrali. Ambiente domestico trasformato in 
                trappola psicologica dove sicurezza familiare diventa minaccia esistenziale.
                """,
                
                "detailed_plot": """
                Dopo la morte della madre Ellen, Annie Graham lotta con una relazione complicata 
                con l'eredità familiare. Ellen era una figura dominante e segretamente coinvolta 
                in pratiche occulte che Annie non comprende completamente. Quando la figlia 
                tredicenne Charlie muore decapitata in un incidente terrificante causato dal 
                fratello Peter, la famiglia Graham inizia a disintegrarsi sotto il peso del 
                lutto e della colpa. Annie scopre che sua madre faceva parte di un culto 
                demoniaco dedicato a Paimon, re dell'Inferno, e che Charlie era destinata 
                fin dalla nascita a essere vessillo per la sua incarnazione terrena. Ma quando 
                Charlie muore prematuramente, il culto deve trasferire Paimon nel corpo di 
                Peter. Attraverso sedute spiritiche e manipolazione psicologica, i seguaci 
                di Ellen orchestrano la distruzione mentale della famiglia Graham. Annie, 
                posseduta dal demone, tenta di uccidere Peter, che fugge in soffitta dove 
                scopre il corpo mummificato della nonna e cultisti che lo aspettano. Costretto 
                a lanciarsi dalla finestra, Peter sopravvive giusto il tempo necessario perché 
                Paimon prenda possesso del suo corpo danneggiato.
                """,
                
                "directorial_style": """
                Aster dirige con precisione maniacale, costruendo orrore attraverso dettagli 
                domestici e composizioni simmetriche inquietanti. Regia che trasforma drama 
                familiare in incubo esoterico attraverso ritmo deliberatamente lento.
                """,
                
                "emotional_impact": """
                Film che genera terror cosmico e angoscia familiare in proporzioni devastanti. 
                Esperienza traumatica che esplora come dolore generazionale possa manifestarsi 
                in forme soprannaturali. Orrore psicologico che perdura ben oltre la visione.
                """,
                
                "visual_style": """
                Cinematografia che usa miniature e case di bambola come metafore per determinismo 
                familiare. Palette naturale che si contamina progressivamente con elementi 
                soprannaturali. Inquadrature simmetriche che creano senso di predestinazione.
                """
            }
        },
        
        {
            "id": 22,
            "title": "Dune",
            "release_year": 2021,
            "director": "Denis Villeneuve",
            "genres": ["Sci-Fi", "Adventure", "Drama"],
            "imdb_rating": 8.0,
            "content_rating": "PG-13",
            "cast": ["Timothée Chalamet", "Rebecca Ferguson", "Oscar Isaac", "Josh Brolin"],
            "duration_minutes": 155,
            "availability_type": "rental",
            "rental_price": 5.99,
            "minimum_plan": "Standard",
            "netflix_url": "/watch/80001489",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera epica e mitologica di space opera che combina politica interplanetaria 
                e misticismo desertico. Mood grandioso e contemplativo dove destino profetico 
                incontra realtà brutale della guerra. Sensazione di vastità cosmica bilanciata 
                da intimità del coming-of-age. Ambiente desertico di Arrakis reso come 
                personaggio vivente che plasma destini umani.
                """,
                
                "detailed_plot": """
                Nell'anno 10191, l'Imperatore affida al Duca Leto Atreides il controllo di 
                Arrakis, unico pianeta fonte della "spezia", sostanza che permette viaggi 
                interstellari e potenzia abilità psichiche. Paul Atreides, figlio di Leto 
                e dell'ex-Bene Gesserit Lady Jessica, manifesta poteri precognitivi che lo 
                identificano come possibile "Kwisatz Haderach", essere supremo profetizzato. 
                Ma l'incarico è una trappola: l'Imperatore teme il crescente potere degli 
                Atreides e complotta con i nemici storici Harkonnen per distruggerli. Quando 
                Arrakis viene attaccata e Leto assassinato, Paul e Jessica fuggono nel deserto 
                dove incontrano i Fremen, popolazione indigena che li riconosce come figure 
                messianiche delle loro profezie. Paul assume il nome Fremen "Muad'Dib" e 
                inizia a padroneggiare i suoi poteri prescientivi, vedendo futuri possibili 
                di jihad galattica. Mentre impara a cavalcare i vermi delle sabbie giganti 
                e guida i Fremen in guerriglia contro gli oppressori, Paul lotta con la 
                consapevolezza che il suo destino porterà miliardi di morti attraverso la galassia.
                """,
                
                "directorial_style": """
                Villeneuve dirige con maestria visiva monumentale, creando fantascienza 
                contemplativa che bilancia spettacolo e profondità filosofica. Regia paziente 
                che permette all'epicità di emergere organicamente da dettagli intimi.
                """,
                
                "emotional_impact": """
                Film che genera senso di meraviglia epica e riflessione sul peso del destino. 
                Esperienza immersiva che combina coming-of-age universale con politica 
                galattica. Fascino mitologico che interroga natura del potere e della profezia.
                """,
                
                "visual_style": """
                Cinematografia desertica monumentale con architetture che evocano civiltà 
                antiche e futuristiche. Palette sabbiosa dominata da ocre e bronzi che 
                contrastano con tecnologie avanzate. Effetti che rendono tangibile l'impossibile.
                """
            }
        },
        
        {
            "id": 23,
            "title": "Once Upon a Time in Hollywood",
            "release_year": 2019,
            "director": "Quentin Tarantino",
            "genres": ["Comedy", "Drama"],
            "imdb_rating": 7.6,
            "content_rating": "R",
            "cast": ["Leonardo DiCaprio", "Brad Pitt", "Margot Robbie", "Emile Hirsch"],
            "duration_minutes": 161,
            "availability_type": "rental",
            "rental_price": 4.99,
            "minimum_plan": "Standard",
            "netflix_url": "/watch/80001467",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera nostalgica e malinconica della Hollywood del 1969 sul punto di 
                cambiare per sempre. Mood contemplativo e pigro che riflette la fine di 
                un'era dorata del cinema. Sensazione di tempo sospeso dove innocenza 
                hollywoodiana sta per essere brutalmente infranta. Ambiente losangelino 
                reso con amore feticistico per dettagli d'epoca che evocano perdita.
                """,
                
                "detailed_plot": """
                Nell'estate del 1969, Rick Dalton è un attore televisivo in declino famoso 
                per il western "Bounty Law" che lotta con l'alcoolismo e la paura di essere 
                dimenticato. Il suo migliore amico e stuntman Cliff Booth lo accompagna 
                attraverso una Hollywood che sta cambiando, dove i film spaghetti western 
                stanno sostituendo le produzioni americane. Rick vive accanto a Sharon Tate 
                e Roman Polanski, rappresentanti della nuova Hollywood glamour. Mentre Rick 
                gira un pilot western cercando di rilanciare la carriera, Cliff ha un 
                incontro casuale con i seguaci di Charles Manson al Spahn Ranch, intuendo 
                qualcosa di sinistro. Il film culmina nella notte del 9 agosto 1969, quando 
                i membri della "Famiglia" Manson arrivano a Cielo Drive. Ma in questa versione 
                alternativa della storia, invece di uccidere Sharon Tate e i suoi amici, 
                i cultisti vengono attirati dalla musica alta di Rick e decidono di uccidere 
                lui. Cliff e Rick li affrontano in una battaglia surreale e violenta che 
                riscrive la storia, salvando Sharon e preservando l'innocenza hollywoodiana 
                che storicamente fu distrutta quella notte.
                """,
                
                "directorial_style": """
                Tarantino dirige con amore nostalgico per il cinema classico, creando lettera 
                d'amore a Hollywood attraverso ricostruzione meticolosa d'epoca. Regia che 
                privilegia atmosfera e personaggi sopra trama tradizionale.
                """,
                
                "emotional_impact": """
                Film che genera malinconia profonda per paradisi perduti e catarsi attraverso 
                revisione storica fantasiosa. Esperienza che celebra amicizia maschile e 
                mitologia hollywoodiana. Commozione per la capacità del cinema di riscrivere 
                la tragedia.
                """,
                
                "visual_style": """
                Fotografia che ricrea fedelmente la Los Angeles del 1969 con palette calda 
                e satura. Ogni dettaglio visivo evoca nostalgia per l'era d'oro hollywoodiana. 
                Composizioni che omaggiano cinema classico attraverso inquadrature iconiche.
                """
            }
        }
    ]

from typing import List, Dict, Any

def get_enhanced_films_data() -> List[Dict[str, Any]]:
    """
    Restituisce dataset di 53 film con descrizioni MOLTO ricche
    Focus su mood, atmosfere, emozioni, tensione per semantic search
    """
    return [
        {
            "id": 1,
            "title": "Inception",
            "release_year": 2010,
            "director": "Christopher Nolan",
            "genres": ["Sci-Fi", "Thriller", "Action"],
            "imdb_rating": 8.8,
            "content_rating": "PG-13",
            "cast": ["Leonardo DiCaprio", "Marion Cotillard", "Tom Hardy", "Elliot Page"],
            "duration_minutes": 148,
            "availability_type": "included",
            "rental_price": None,
            "minimum_plan": "Standard", 
            "netflix_url": "/watch/80001246",
            
            # DESCRIZIONI POTENZIATE per semantic search
            "enhanced_description": {
                "mood_description": """
                Atmosfera cerebrale e labirintica che ti tiene costantemente in tensione. 
                Il film genera un senso di vertigine intellettuale, dove la realtà si sfalda 
                progressivamente. Sensazioni di claustrofobia onirica si alternano a momenti 
                di pura adrenalina action. L'ambiente è surreale, onirico, sofisticato. 
                Mood psicologico intenso che richiede concentrazione assoluta dello spettatore.
                """,
                
                "detailed_plot": """
                Dom Cobb è un ladro specializzato nell'infiltrarsi nei sogni altrui per rubare 
                segreti dal subconscio. Vive in un mondo dove la tecnologia permette di condividere 
                gli spazi onirici, ma Cobb è tormentato dal ricordo di sua moglie Mal, morta suicida. 
                Quando gli viene offerta la possibilità di tornare dai suoi figli in cambio di 
                un'ultima missione impossibile - l'inception, ovvero impiantare un'idea invece che rubarla - 
                Cobb accetta. Deve convincere Robert Fischer Jr. a sciogliere l'impero economico 
                del padre creando sogni stratificati su tre livelli. Ma Mal continua a sabotare 
                le missioni, rendendo tutto ancora più pericoloso. Il confine tra sogno e realtà 
                diventa sempre più labile in un crescendo di tensione mozzafiato.
                """,
                
                "directorial_style": """
                Nolan orchestra una sinfonia visiva di precisione millimetrica. Ogni sequenza 
                è costruita come un orologio svizzero, con montaggio serrato che alterna azione 
                frenetica a momenti di riflessione filosofica. La regia è cerebrale ma accessibile, 
                con effetti pratici spettacolari che rendono tangibile l'impossibile.
                """,
                
                "emotional_impact": """
                Il film genera ansia esistenziale e fascinazione intellectuale. Temi di colpa, 
                redenzione e amor paterno si intrecciano in una narrazione che scuote 
                profondamente. Sensazione di smarrimento controllato che lascia lo spettatore 
                mentalmente stimolato e emotivamente coinvolto. Esperienza catartica finale.
                """,
                
                "visual_style": """
                Palette visiva fredda e metallica con contrasti netti. Architetture impossibili 
                che si piegano su se stesse creano un'estetica unica. Ogni livello onirico ha 
                una sua identità visiva distinta: dalla pioggia urbana al limbo bianco infinito.
                """
            }
        },
        
        {
            "id": 2,
            "title": "Get Out",
            "release_year": 2017,
            "director": "Jordan Peele",
            "genres": ["Horror", "Thriller", "Mystery"],
            "imdb_rating": 7.8,
            "content_rating": "R",
            "cast": ["Daniel Kaluuya", "Allison Williams", "Bradley Whitford", "Catherine Keener"],
            "duration_minutes": 104,
            "availability_type": "included",
            "rental_price": None,
            "minimum_plan": "Standard",
            "netflix_url": "/watch/80001267",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera di inquietudine crescente che si trasforma in terrore psicologico puro. 
                Il mood è oppressivo, carico di tensione razziale sottile ma pervasiva. Sensazione 
                costante che qualcosa non quadra, un disagio sociale che si amplifica fino al 
                panico. Ambiente apparentemente idilliaco che nasconde orrori inimmaginabili. 
                Suspense masterclass che ti tiene col fiato sospeso dall'inizio alla fine.
                """,
                
                "detailed_plot": """
                Chris Washington, giovane fotografo afroamericano, accompagna la sua fidanzata 
                bianca Rose per incontrare i suoi genitori nella loro tenuta di campagna. 
                Inizialmente i Armitage sembrano accoglienti e progressisti, ma Chris nota 
                comportamenti strani negli altri afroamericani presenti: parlano in modo robotico 
                e hanno sguardi vuoti. Durante una festa, Chris scopre una cospirazione terrificante: 
                la famiglia Armitage gestisce un'operazione di trapianto cerebrale che permette 
                a ricchi bianchi anziani di "possedere" corpi giovani di neri. Chris deve fuggire 
                da questo incubo razzista prima di diventare la prossima vittima della "coagulazione", 
                un processo di ipnosi che intrapola la coscienza nera nel "posto sommerso" della mente.
                """,
                
                "directorial_style": """
                Peele dirige con precisione chirurgica, dosando la tensione come un maestro. 
                Ogni inquadratura comunica disagio sociale attraverso dettagli apparentemente 
                innocenti. La regia è intelligente, mai gratuita, sempre al servizio della critica sociale.
                """,
                
                "emotional_impact": """
                Film che genera profonda inquietudine esistenziale e rabbia sociale. Paura viscerale 
                dell'altro, paranoia giustificata che si trasforma in orrore puro. Esperienza 
                emotivamente devastante che lascia segni duraturi sulla psiche dello spettatore.
                """,
                
                "visual_style": """
                Estetica pulita e borghese che contrasta con l'orrore sottostante. Colori saturi 
                che virano al sinistro, primi piani claustrofobici che catturano l'angoscia. 
                Il "posto sommerso" è visualizzato come vuoto nero infinito, metafora perfetta.
                """
            }
        },
        
        {
            "id": 3,
            "title": "The Dark Knight",
            "release_year": 2008,
            "director": "Christopher Nolan",
            "genres": ["Action", "Crime", "Drama"],
            "imdb_rating": 9.0,
            "content_rating": "PG-13",
            "cast": ["Christian Bale", "Heath Ledger", "Aaron Eckhart", "Gary Oldman"],
            "duration_minutes": 152,
            "availability_type": "included",
            "rental_price": None,
            "minimum_plan": "Basic",
            "netflix_url": "/watch/80001245",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera dark e grittosa che trascende il genere supereroistico. Mood cupo e 
                filosoficamente complesso, dove il caos incontra l'ordine in uno scontro epico. 
                Tensione psicologica costante amplificata dalla presenza inquietante del Joker. 
                Sensazione di città sull'orlo del baratro morale. Epicità tragica che eleva 
                l'action a riflessione esistenziale profonda.
                """,
                
                "detailed_plot": """
                Gotham City sembra finalmente trovare pace grazie agli sforzi combinati di Batman, 
                del commissario Gordon e del nuovo procuratore distrettuale Harvey Dent. Ma l'arrivo 
                del Joker, criminale psicopatico senza motivazioni comprensibili, scatena il caos 
                assoluto. Il Joker non vuole denaro o potere: vuole dimostrare che chiunque può 
                diventare mostruoso nelle giuste circostanze. Attraverso esperimenti sociali sadici 
                - come il dilemma dei traghetti o la corruzione di Harvey Dent - il Joker tenta di 
                far crollare Batman nel baratro morale. Quando Harvey diventa Due Facce dopo la morte 
                della sua fidanzata Rachel, Batman deve fare la scelta più difficile: diventare il 
                cattivo per preservare la speranza di Gotham, sacrificando la sua reputazione per 
                il bene comune.
                """,
                
                "directorial_style": """
                Nolan eleva il film di supereroi a tragedia shakespeariana urbana. Regia epica 
                che bilancia action spettacolare e profondità psicologica. Ogni sequenza è costruita 
                su livelli multipli di significato simbolico.
                """,
                
                "emotional_impact": """
                Esperienza emotiva devastante che esplora i limiti della moralità umana. Genera 
                riflessione profonda sulla natura del bene e del male. Il sacrificio finale di 
                Batman tocca corde emotive profondissime. Film che segna e trasforma.
                """,
                
                "visual_style": """
                Gotham fotografata come metropoli noir contemporanea. Palette scura con esplosioni 
                di colore violento. La presenza del Joker contamina visivamente ogni scena con 
                il suo caos cromatico. Architettura urbana opprimente e maestosa.
                """
            }
        },
        
        {
            "id": 4,
            "title": "Parasite",
            "release_year": 2019,
            "director": "Bong Joon-ho",
            "genres": ["Thriller", "Drama", "Dark Comedy"],
            "imdb_rating": 8.5,
            "content_rating": "R",
            "cast": ["Song Kang-ho", "Lee Sun-kyun", "Cho Yeo-jeong", "Choi Woo-shik"],
            "duration_minutes": 132,
            "availability_type": "included",
            "rental_price": None,
            "minimum_plan": "Standard",
            "netflix_url": "/watch/80001289",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera di tensione sociale palpabile che evolve da commedia nera a thriller 
                psicologico devastante. Mood di disagio crescente alimentato dalle disuguaglianze 
                di classe. Sensazione di precarietà costante, dove ogni momento di leggerezza 
                nasconde un abisso sociale. Ambiente claustrofobico che riflette le gerarchie 
                economiche attraverso gli spazi architettonici.
                """,
                
                "detailed_plot": """
                La famiglia Kim vive in un seminterrato fatiscente e sopravvive piegando scatole 
                di pizza. Quando il figlio Ki-woo ottiene un lavoro come tutor d'inglese per 
                la figlia della ricca famiglia Park, architetta un piano per far assumere tutta 
                la sua famiglia come personale domestico, nascondendo i loro legami di parentela. 
                Inizialmente tutto procede perfettamente: Ki-jung diventa l'art-therapist del 
                figlio Park, il padre Ki-taek sostituisce l'autista e la madre Chung-sook diventa 
                la governante. Ma la scoperta di un bunker segreto dove vive nascosto il marito 
                della precedente governante scatena una serie di eventi tragici che culminano 
                in un bagno di sangue durante una festa di compleanno, rivelando l'impossibilità 
                di scalare davvero la piramide sociale.
                """,
                
                "directorial_style": """
                Bong Joon-ho dirige con maestria chirurgica, usando gli spazi architettonici 
                come metafore viventi della stratificazione sociale. Ogni movimento di camera 
                comunica dinamiche di potere, ogni dettaglio visivo racconta la lotta di classe.
                """,
                
                "emotional_impact": """
                Film che genera profonda riflessione sulla disuguaglianza e rabbia sociale 
                controllata. Evolve da divertimento complice a shock emotivo devastante. 
                Lascia lo spettatore con una sensazione di ingiustizia sistemica e impotenza 
                che perdura a lungo dopo la visione.
                """,
                
                "visual_style": """
                Estetica pulita e geometrica che contrasta spazi alti (ricchezza) e bassi (povertà). 
                Palette cromatica che si fa sempre più satura man mano che cresce la tensione. 
                La pioggia diventa elemento visivo simbolico di purificazione e distruzione.
                """
            }
        },
        
        {
            "id": 5,
            "title": "Joker",
            "release_year": 2019,
            "director": "Todd Phillips",
            "genres": ["Drama", "Crime", "Thriller"],
            "imdb_rating": 8.4,
            "content_rating": "R",
            "cast": ["Joaquin Phoenix", "Robert De Niro", "Zazie Beetz", "Frances Conroy"],
            "duration_minutes": 122,
            "availability_type": "rental",
            "rental_price": 3.99,
            "minimum_plan": "Basic",
            "netflix_url": "/watch/80001334",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera opprimente di decadenza urbana e disperazione psicologica. Mood 
                claustrofobico che riflette la discesa nella follia di un uomo ai margini. 
                Sensazione costante di disagio sociale e tensione psicologica che esplode 
                in violenza catartica. Ambiente degradato che rispecchia lo stato mentale 
                del protagonista. Inquietudine crescente che culmina in anarchia sociale.
                """,
                
                "detailed_plot": """
                Arthur Fleck è un aspirante comico che vive con la madre malata in una Gotham 
                City decadente degli anni '80. Affetto da una condizione neurologica che lo 
                fa ridere incontrollabilmente nei momenti di stress, Arthur è costantemente 
                umiliato e picchiato dalla società. Licenziato dal suo lavoro da clown, 
                deriso durante un'apparizione in un talk show, Arthur scopre che sua madre 
                lo ha mentito sulla sua identità per tutta la vita. La combinazione di 
                traumi psicologici, isolamento sociale e taglio ai servizi sanitari pubblici 
                lo spinge oltre il limite. L'uccisione di tre giovani di Wall Street in 
                metropolitana scatena proteste sociali che lo trasformano in simbolo di 
                rivolta contro l'élite. Arthur abbraccia la sua nuova identità come Joker, 
                diventando l'antieroe che Gotham merita.
                """,
                
                "directorial_style": """
                Phillips dirige con intensità documentaristica, creando un ritratto crudo 
                della malattia mentale e dell'esclusione sociale. Regia intimista che segue 
                da vicino la trasformazione psicologica del protagonista con realismo brutale.
                """,
                
                "emotional_impact": """
                Film che genera profonda empatia per un personaggio disturbante, creando 
                conflitto morale nello spettatore. Esperienza emotivamente devastante che 
                interroga i confini tra vittima e carnefice. Riflessione dolorosa sulla 
                responsabilità sociale nella creazione dei mostri.
                """,
                
                "visual_style": """
                Gotham degli anni '80 resa con palette terrosa e degradata. Colori desaturati 
                che si accendono progressivamente con la trasformazione di Arthur. Il rosso 
                diventa colore dominante nella metamorfosi finale in Joker.
                """
            }
        },
        
        {
            "id": 6,
            "title": "Pulp Fiction",
            "release_year": 1994,
            "director": "Quentin Tarantino",
            "genres": ["Crime", "Drama", "Thriller"],
            "imdb_rating": 8.9,
            "content_rating": "R",
            "cast": ["John Travolta", "Samuel L. Jackson", "Uma Thurman", "Bruce Willis"],
            "duration_minutes": 154,
            "availability_type": "included",
            "rental_price": None,
            "minimum_plan": "Basic",
            "netflix_url": "/watch/80001123",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera cool e irriverente che mescola violenza stilizzata e dialoghi ipnotici. 
                Mood neo-noir postmoderno dove tensione e humor nero si alternano in un cocktail 
                esplosivo. Sensazione di coolness underground, dove ogni conversazione banale 
                può esplodere in violenza improvvisa. Ambiente losangelino criminale reso 
                mitologico attraverso la lente pop di Tarantino.
                """,
                
                "detailed_plot": """
                Tre storie intrecciate nella Los Angeles criminale: Vincent Vega e Jules Winnfield 
                sono due sicari filosofi che recuperano una misteriosa valigetta per il loro capo 
                Marsellus Wallace, vivendo un'epifania spirituale dopo essere miracolosamente 
                sopravvissuti a una sparatoria. Butch Coolidge è un pugile che tradisce Wallace 
                rifiutandosi di perdere un incontro truccato, scatenando una caccia all'uomo che 
                lo porta a salvare paradossalmente il suo nemico da una situazione perversa. 
                Vincent deve fare da baby-sitter a Mia, moglie di Wallace, e la serata si trasforma 
                in un incubo quando lei va in overdose. Ogni storia esplora temi di redenzione, 
                fato e violenza attraverso dialoghi memorabili e situazioni assurde che 
                trasformano il banale in epico.
                """,
                
                "directorial_style": """
                Tarantino rivoluziona il cinema con struttura narrativa non lineare e dialoghi 
                che trasformano conversazioni ordinarie in piccoli capolavori. Regia pop che 
                saccheggia la cultura di massa per creare un linguaggio cinematografico nuovo.
                """,
                
                "emotional_impact": """
                Film che genera fascinazione per la mitologia criminale urbana. Esperienza 
                adrenalinica che combina tensione e divertimento in dosi perfette. Sensazione 
                di assistere a qualcosa di rivoluzionario che ha cambiato per sempre il cinema.
                """,
                
                "visual_style": """
                Estetica retrò-futuristica che mescola anni '50 e '90. Colori vivaci e saturi 
                che rendono ogni scena iconicamente memorabile. Fotografia che trasforma 
                ambienti ordinari in set mitologici attraverso inquadrature creative.
                """
            }
        },
        
        {
            "id": 7,
            "title": "Interstellar",
            "release_year": 2014,
            "director": "Christopher Nolan",
            "genres": ["Sci-Fi", "Drama", "Adventure"],
            "imdb_rating": 8.7,
            "content_rating": "PG-13",
            "cast": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain", "Michael Caine"],
            "duration_minutes": 169,
            "availability_type": "included",
            "rental_price": None,
            "minimum_plan": "Standard",
            "netflix_url": "/watch/80001278",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera epica e contemplativa che unisce intimità familiare e vastità cosmica. 
                Mood nostalgico e malinconico permeato da senso di meraviglia scientifica. 
                Sensazione di solitudine cosmica bilanciata da amore paterno incondizionato. 
                Ambiente che spazia dalla Terra distopica agli spazi infiniti, generando 
                vertigine esistenziale e speranza simultaneamente.
                """,
                
                "detailed_plot": """
                In un futuro prossimo dove la Terra è devastata da tempeste di sabbia e carestie, 
                Cooper, ex pilota NASA diventato agricoltore, vive con i figli Murph e Tom. 
                Quando anomalie gravitazionali nella camera di Murph rivelano coordinate segrete, 
                Cooper scopre una base NASA nascosta dove gli scienziati stanno preparando una 
                missione disperata per salvare l'umanità. Un wormhole apparso vicino Saturno 
                permette di raggiungere pianeti potenzialmente abitabili in un'altra galassia. 
                Cooper accetta di pilotare la missione Endurance, lasciando Murph che lo considera 
                un traditore. Su pianeti alieni dove il tempo scorre diversamente, Cooper e il 
                team affrontano oceani giganteschi e ghiacci eterni mentre sulla Terra passano 
                decenni. Il viaggio diventa una riflessione su amore, sacrificio e il destino 
                dell'umanità, culminando in una dimensione extracorporea dove Cooper comunica 
                con la figlia attraverso il tempo stesso.
                """,
                
                "directorial_style": """
                Nolan combina rigore scientifico e poetica emotiva in una sinfonia visiva 
                monumentale. Regia che bilancia spettacolo cosmico e intimità umana con 
                maestria assoluta. Ogni inquadratura comunica sia meraviglia che malinconia.
                """,
                
                "emotional_impact": """
                Film che genera profonda commozione attraverso il tema universale dell'amore 
                paterno. Esperienza catartica che unisce lacrime e meraviglia in un crescendo 
                emotivo devastante. Riflessione esistenziale sul senso della vita e della morte.
                """,
                
                "visual_style": """
                Fotografia che contrasta la Terra ocra e polverosa con il nero infinito dello spazio. 
                Effetti pratici che rendono tangibile l'impossibile. Ogni pianeta ha un'identità 
                visiva unica che comunica atmosfere emotive distinte.
                """
            }
        },
        
        {
            "id": 8,
            "title": "The Shawshank Redemption",
            "release_year": 1994,
            "director": "Frank Darabont",
            "genres": ["Drama"],
            "imdb_rating": 9.3,
            "content_rating": "R",
            "cast": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
            "duration_minutes": 142,
            "availability_type": "included",
            "rental_price": None,
            "minimum_plan": "Basic",
            "netflix_url": "/watch/80001187",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera di speranza indistruttibile che resiste alla brutalità carceraria. 
                Mood contemplativo e profondamente umano, dove la dignità sopravvive alla 
                disperazione. Sensazione di calore fraterno che contrasta con l'ambiente 
                opprimente del penitenziario. Pace interiore che emerge gradualmente dal 
                dolore. Esperienza spirituale che celebra la resilienza dell'animo umano.
                """,
                
                "detailed_plot": """
                Andy Dufresne, banchiere condannato per l'omicidio della moglie e del suo amante 
                (crimine che nega di aver commesso), arriva al penitenziario di Shawshank nel 1947. 
                Inizialmente vittima di violenze e soprusi, Andy trova in Red, contrabbandiere 
                veterano della prigione, un'amicizia che cambierà entrambe le loro vite. Grazie 
                alle sue competenze finanziarie, Andy diventa indispensabile al direttore corrotto 
                Norton, riciclando denaro sporco mentre segretamente documenta ogni illegalità. 
                Nel corso di vent'anni, Andy trasforma la biblioteca della prigione, aiuta altri 
                detenuti a conseguire diplomi e crea un senso di comunità. Ma il suo vero piano 
                è più ambizioso: attraverso pazienza infinite e un piccone nascosto dietro un 
                poster di Rita Hayworth, Andy scava un tunnel per la libertà mentre prepara la 
                rovina del sistema corrotto che lo imprigiona.
                """,
                
                "directorial_style": """
                Darabont dirige con sensibilità poetica, trasformando un ambiente brutale in 
                uno spazio di redenzione umana. Regia che trova bellezza nella disperazione 
                e celebra la dignità in condizioni disumane.
                """,
                
                "emotional_impact": """
                Film che genera profonda catarsi emotiva attraverso temi universali di amicizia, 
                speranza e redenzione. Esperienza che tocca l'anima e restaura la fede nell'umanità. 
                Commozione autentica che cresce fino a diventare gioia pura.
                """,
                
                "visual_style": """
                Fotografia calda e dorata che contrasta con l'ambiente grigio del carcere. 
                Luce naturale usata simbolicamente per rappresentare speranza e libertà. 
                Inquadrature che dignificano ogni personaggio indipendentemente dal suo status.
                """
            }
        },
        
        {
            "id": 9,
            "title": "Mad Max: Fury Road",
            "release_year": 2015,
            "director": "George Miller",
            "genres": ["Action", "Adventure", "Sci-Fi"],
            "imdb_rating": 8.1,
            "content_rating": "R",
            "cast": ["Tom Hardy", "Charlize Theron", "Nicholas Hoult", "Hugh Keays-Byrne"],
            "duration_minutes": 120,
            "availability_type": "rental",
            "rental_price": 2.99,
            "minimum_plan": "Basic",
            "netflix_url": "/watch/80001298",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera post-apocalittica di pura adrenalina e disperazione viscerale. 
                Mood frenetico e primordiale dove sopravvivenza e libertà si conquistano 
                con sangue e benzina. Sensazione di caos controllato, dove ogni secondo 
                può essere l'ultimo. Ambiente desertico che riflette la brutalità di 
                un mondo senza regole. Tensione costante amplificata da ritmo incalzante.
                """,
                
                "detailed_plot": """
                In un futuro post-apocalittico dominato da signori della guerra che controllano 
                acqua e benzina, Max Rockatansky viene catturato dai War Boys dell'Immortan Joe 
                e usato come "donatore di sangue" per il malato Nux. Quando l'Imperatrice Furiosa 
                devia dalla sua missione per rubare benzina e fugge con le cinque mogli-schiave 
                di Joe verso la "Terra Verde" del suo ricordo d'infanzia, scatena un inseguimento 
                epico attraverso il deserto. Max si allea riluttante con Furiosa e le donne in 
                fuga, scoprendo che la Terra Verde è ormai un deserto tossico. Il gruppo decide 
                di tornare indietro per conquistare la Cittadella di Joe, in una battaglia finale 
                che costa la vita al tiranno ma regala speranza di un nuovo inizio alle sopravvissute.
                """,
                
                "directorial_style": """
                Miller dirige con energia primordiale, creando action puro attraverso stunt 
                pratici spettacolari. Regia viscerale che comunica attraverso movimento, 
                colore e suono più che dialoghi. Ogni inquadratura è dinamite cinematografica.
                """,
                
                "emotional_impact": """
                Film che genera adrenalina pura e senso di liberazione catartica. Esperienza 
                viscerale che celebra resistenza femminile e redenzione maschile. Euforia 
                kinetic che lascia lo spettatore elettrizzato e empowerato.
                """,
                
                "visual_style": """
                Estetica post-apocalittica iper-satura con palette cromatica esplosiva. 
                Deserto arancione contro cielo blu elettrico. Design barocco-industriale 
                che trasforma veicoli in opere d'arte della distruzione.
                """
            }
        },
        
        {
            "id": 6,
            "title": "Pulp Fiction",
            "release_year": 1994,
            "director": "Quentin Tarantino",
            "genres": ["Crime", "Drama", "Thriller"],
            "imdb_rating": 8.9,
            "content_rating": "R",
            "cast": ["John Travolta", "Samuel L. Jackson", "Uma Thurman", "Bruce Willis"],
            "duration_minutes": 154,
            "availability_type": "included",
            "rental_price": None,
            "minimum_plan": "Basic",
            "netflix_url": "/watch/80001123",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera cool e irriverente che mescola violenza stilizzata e dialoghi ipnotici. 
                Mood neo-noir postmoderno dove tensione e humor nero si alternano in un cocktail 
                esplosivo. Sensazione di coolness underground, dove ogni conversazione banale 
                può esplodere in violenza improvvisa. Ambiente losangelino criminale reso 
                mitologico attraverso la lente pop di Tarantino.
                """,
                
                "detailed_plot": """
                Tre storie intrecciate nella Los Angeles criminale: Vincent Vega e Jules Winnfield 
                sono due sicari filosofi che recuperano una misteriosa valigetta per il loro capo 
                Marsellus Wallace, vivendo un'epifania spirituale dopo essere miracolosamente 
                sopravvissuti a una sparatoria. Butch Coolidge è un pugile che tradisce Wallace 
                rifiutandosi di perdere un incontro truccato, scatenando una caccia all'uomo che 
                lo porta a salvare paradossalmente il suo nemico da una situazione perversa. 
                Vincent deve fare da baby-sitter a Mia, moglie di Wallace, e la serata si trasforma 
                in un incubo quando lei va in overdose. Ogni storia esplora temi di redenzione, 
                fato e violenza attraverso dialoghi memorabili e situazioni assurde che 
                trasformano il banale in epico.
                """,
                
                "directorial_style": """
                Tarantino rivoluziona il cinema con struttura narrativa non lineare e dialoghi 
                che trasformano conversazioni ordinarie in piccoli capolavori. Regia pop che 
                saccheggia la cultura di massa per creare un linguaggio cinematografico nuovo.
                """,
                
                "emotional_impact": """
                Film che genera fascinazione per la mitologia criminale urbana. Esperienza 
                adrenalinica che combina tensione e divertimento in dosi perfette. Sensazione 
                di assistere a qualcosa di rivoluzionario che ha cambiato per sempre il cinema.
                """,
                
                "visual_style": """
                Estetica retrò-futuristica che mescola anni '50 e '90. Colori vivaci e saturi 
                che rendono ogni scena iconicamente memorabile. Fotografia che trasforma 
                ambienti ordinari in set mitologici attraverso inquadrature creative.
                """
            }
        },
        
        {
            "id": 7,
            "title": "Interstellar",
            "release_year": 2014,
            "director": "Christopher Nolan",
            "genres": ["Sci-Fi", "Drama", "Adventure"],
            "imdb_rating": 8.7,
            "content_rating": "PG-13",
            "cast": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain", "Michael Caine"],
            "duration_minutes": 169,
            "availability_type": "included",
            "rental_price": None,
            "minimum_plan": "Standard",
            "netflix_url": "/watch/80001278",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera epica e contemplativa che unisce intimità familiare e vastità cosmica. 
                Mood nostalgico e malinconico permeato da senso di meraviglia scientifica. 
                Sensazione di solitudine cosmica bilanciata da amore paterno incondizionato. 
                Ambiente che spazia dalla Terra distopica agli spazi infiniti, generando 
                vertigine esistenziale e speranza simultaneamente.
                """,
                
                "detailed_plot": """
                In un futuro prossimo dove la Terra è devastata da tempeste di sabbia e carestie, 
                Cooper, ex pilota NASA diventato agricoltore, vive con i figli Murph e Tom. 
                Quando anomalie gravitazionali nella camera di Murph rivelano coordinate segrete, 
                Cooper scopre una base NASA nascosta dove gli scienziati stanno preparando una 
                missione disperata per salvare l'umanità. Un wormhole apparso vicino Saturno 
                permette di raggiungere pianeti potenzialmente abitabili in un'altra galassia. 
                Cooper accetta di pilotare la missione Endurance, lasciando Murph che lo considera 
                un traditore. Su pianeti alieni dove il tempo scorre diversamente, Cooper e il 
                team affrontano oceani giganteschi e ghiacci eterni mentre sulla Terra passano 
                decenni. Il viaggio diventa una riflessione su amore, sacrificio e il destino 
                dell'umanità, culminando in una dimensione extracorporea dove Cooper comunica 
                con la figlia attraverso il tempo stesso.
                """,
                
                "directorial_style": """
                Nolan combina rigore scientifico e poetica emotiva in una sinfonia visiva 
                monumentale. Regia che bilancia spettacolo cosmico e intimità umana con 
                maestria assoluta. Ogni inquadratura comunica sia meraviglia che malinconia.
                """,
                
                "emotional_impact": """
                Film che genera profonda commozione attraverso il tema universale dell'amore 
                paterno. Esperienza catartica che unisce lacrime e meraviglia in un crescendo 
                emotivo devastante. Riflessione esistenziale sul senso della vita e della morte.
                """,
                
                "visual_style": """
                Fotografia che contrasta la Terra ocra e polverosa con il nero infinito dello spazio. 
                Effetti pratici che rendono tangibile l'impossibile. Ogni pianeta ha un'identità 
                visiva unica che comunica atmosfere emotive distinte.
                """
            }
        },
        
        {
            "id": 8,
            "title": "The Shawshank Redemption",
            "release_year": 1994,
            "director": "Frank Darabont",
            "genres": ["Drama"],
            "imdb_rating": 9.3,
            "content_rating": "R",
            "cast": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
            "duration_minutes": 142,
            "availability_type": "included",
            "rental_price": None,
            "minimum_plan": "Basic",
            "netflix_url": "/watch/80001187",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera di speranza indistruttibile che resiste alla brutalità carceraria. 
                Mood contemplativo e profondamente umano, dove la dignità sopravvive alla 
                disperazione. Sensazione di calore fraterno che contrasta con l'ambiente 
                opprimente del penitenziario. Pace interiore che emerge gradualmente dal 
                dolore. Esperienza spirituale che celebra la resilienza dell'animo umano.
                """,
                
                "detailed_plot": """
                Andy Dufresne, banchiere condannato per l'omicidio della moglie e del suo amante 
                (crimine che nega di aver commesso), arriva al penitenziario di Shawshank nel 1947. 
                Inizialmente vittima di violenze e soprusi, Andy trova in Red, contrabbandiere 
                veterano della prigione, un'amicizia che cambierà entrambe le loro vite. Grazie 
                alle sue competenze finanziarie, Andy diventa indispensabile al direttore corrotto 
                Norton, riciclando denaro sporco mentre segretamente documenta ogni illegalità. 
                Nel corso di vent'anni, Andy trasforma la biblioteca della prigione, aiuta altri 
                detenuti a conseguire diplomi e crea un senso di comunità. Ma il suo vero piano 
                è più ambizioso: attraverso pazienza infinite e un piccone nascosto dietro un 
                poster di Rita Hayworth, Andy scava un tunnel per la libertà mentre prepara la 
                rovina del sistema corrotto che lo imprigiona.
                """,
                
                "directorial_style": """
                Darabont dirige con sensibilità poetica, trasformando un ambiente brutale in 
                uno spazio di redenzione umana. Regia che trova bellezza nella disperazione 
                e celebra la dignità in condizioni disumane.
                """,
                
                "emotional_impact": """
                Film che genera profonda catarsi emotiva attraverso temi universali di amicizia, 
                speranza e redenzione. Esperienza che tocca l'anima e restaura la fede nell'umanità. 
                Commozione autentica che cresce fino a diventare gioia pura.
                """,
                
                "visual_style": """
                Fotografia calda e dorata che contrasta con l'ambiente grigio del carcere. 
                Luce naturale usata simbolicamente per rappresentare speranza e libertà. 
                Inquadrature che dignificano ogni personaggio indipendentemente dal suo status.
                """
            }
        },
        
        {
            "id": 9,
            "title": "Mad Max: Fury Road",
            "release_year": 2015,
            "director": "George Miller",
            "genres": ["Action", "Adventure", "Sci-Fi"],
            "imdb_rating": 8.1,
            "content_rating": "R",
            "cast": ["Tom Hardy", "Charlize Theron", "Nicholas Hoult", "Hugh Keays-Byrne"],
            "duration_minutes": 120,
            "availability_type": "rental",
            "rental_price": 2.99,
            "minimum_plan": "Basic",
            "netflix_url": "/watch/80001298",
            
            "enhanced_description": {
                "mood_description": """
                Atmosfera post-apocalittica di pura adrenalina e disperazione viscerale. 
                Mood frenetico e primordiale dove sopravvivenza e libertà si conquistano 
                con sangue e benzina. Sensazione di caos controllato, dove ogni secondo 
                può essere l'ultimo. Ambiente desertico che riflette la brutalità di 
                un mondo senza regole. Tensione costante amplificata da ritmo incalzante.
                """,
                
                "detailed_plot": """
                In un futuro post-apocalittico dominato da signori della guerra che controllano 
                acqua e benzina, Max Rockatansky viene catturato dai War Boys dell'Immortan Joe 
                e usato come "donatore di sangue" per il malato Nux. Quando l'Imperatrice Furiosa 
                devia dalla sua missione per rubare benzina e fugge con le cinque mogli-schiave 
                di Joe verso la "Terra Verde" del suo ricordo d'infanzia, scatena un inseguimento 
                epico attraverso il deserto. Max si allea riluttante con Furiosa e le donne in 
                fuga, scoprendo che la Terra Verde è ormai un deserto tossico. Il gruppo decide 
                di tornare indietro per conquistare la Cittadella di Joe, in una battaglia finale 
                che costa la vita al tiranno ma regala speranza di un nuovo inizio alle sopravvissute.
                """,
                
                "directorial_style": """
                Miller dirige con energia primordiale, creando action puro attraverso stunt 
                pratici spettacolari. Regia viscerale che comunica attraverso movimento, 
                colore e suono più che dialoghi. Ogni inquadratura è dinamite cinematografica.
                """,
                
                "emotional_impact": """
                Film che genera adrenalina pura e senso di liberazione catartica. Esperienza 
                viscerale che celebra resistenza femminile e redenzione maschile. Euforia 
                kinetic che lascia lo spettatore elettrizzato e empowerato.
                """,
                
                "visual_style": """
                Estetica post-apocalittica iper-satura con palette cromatica esplosiva. 
                Deserto arancione contro cielo blu elettrico. Design barocco-industriale 
                che trasforma veicoli in opere d'arte della distruzione.
                """
            }
        },      
        # Aggiungi altri 50 film con lo stesso pattern di descrizioni ricche...
        # Per brevità mostro solo 3 esempi, ma il dataset completo avrà tutti i 53 film
    ]