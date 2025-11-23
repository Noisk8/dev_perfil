from django.shortcuts import render


def home(request):
    profile = {
        "name": "Noisk8",
        "tagline": "Livecoder, Pythonista, Node Operator y contribuidor Wikimedia.",
        "bio": (
            "Desarrolloador Multimedia y experiencias creativas con Python y javascript, automatizo tareas en Linux "
            "y despliego infra que prioriza privacidad. Contribuyo en el ecosistema Wikimedia "
            "(Wikidata/Toolforge) y experimento con frontend (Astro/NextJs/ReactJs/ TS) para dar forma a ideas rápidas."
        ),
        "location": "Medellín, Colombia",
        "links": {
            "github": "https://github.com/Noisk8",
            "website": "https://noisk8.github.io/noisk8/",
            "twitter": "https://x.com/noisk8",
        },
    }

    skills = [
        {
            "title": "Python y backend creativo",
            "items": ["Django", "Pygame", "OSC", "Automatización CLI", "Procesamiento de audio"],
        },
        {
            "title": "Sistemas y redes",
            "items": ["Linux", "Bash", "Raspberry Pi", "Servicios auto-hosteados", "Nodos Nym"],
        },
        {
            "title": "Frontend ligero",
            "items": ["Astro", "TypeScript", "HTML/CSS creativo", "Experimentos audiovisuales"],
        },
        {
            "title": "Ecosistema Wikimedia",
            "items": ["Wikidata (edición masiva)", "Toolforge (Python/Flask)", "Documentación de comunidad"],
        },
    ]

    wikimedia = {
        "contributions": [
            {
                "title": "Contribuidor Wikidata",
                "description": "Ediciones y curaduría de datos abiertos en Wikidata.",
                "link": "https://www.wikidata.org/wiki/Special:Contributions/Juan_Andres_Jaramillo_Silva",
                "tech": ["SPARQL", "Datos abiertos"],
            },
            {
                "title": "Código en Wikitech",
                "description": "Repos en GitLab de Wikimedia para herramientas y bots.",
                "link": "https://gitlab.wikimedia.org/noisk8",
                "tech": ["Python", "Toolforge"],
            },
        ],
        "tools": [
            {
                "name": "ecosdeunmural.toolforge.org",
                "description": "Recorrido web para documentar intervenciones urbanas.",
                "link": "https://ecosdeunmural.toolforge.org/",
                "tech": ["Toolforge", "Frontend"],
            },
            {
                "name": "memorial.toolforge.org",
                "description": "Memorial de datos en Wikimedia como sitio navegable.",
                "link": "https://memorial.toolforge.org/",
                "tech": ["Toolforge", "Python"],
            },
            {
                "name": "linea-de-tiempo-falsos-positivos.toolforge.org",
                "description": "Línea de tiempo interactiva basada en datos públicos.",
                "link": "https://linea-de-tiempo-falsos-positivos.toolforge.org/",
                "tech": ["Toolforge", "Frontend"],
            },
        ],
    }

    projects = [
        {
            "name": "Hidropoéticas",
            "description": "Sitio web performativo con narrativa audiovisual y exploración territorial.",
            "tech": ["Frontend", "Astro"],
            "link": "https://hidropoeticas-web.vercel.app/",
            "area": "Frontend",
        },
        {
            "name": "Yo quiero aprender",
            "description": "Plataforma educativa de Platohedro con contenidos y recursos interactivos.",
            "tech": ["Frontend", "Experiencias educativas"],
            "link": "https://yoquieroaprender.platohedro.org/",
            "area": "Frontend",
        },
        {
            "name": "Territorios de Gol",
            "description": "Sitio narrativo sobre fútbol, territorio y comunidad.",
            "tech": ["Frontend", "Storytelling"],
            "link": "https://territoriosdegol.motivandoalagyal.org/",
            "area": "Frontend",
        },
        {
            "name": "Instalando-Renardo-FoxDot-En-linux",
            "description": "Script Bash para dejar listo el entorno de livecoding Renardo/FoxDot en Linux.",
            "tech": ["Bash", "Linux"],
            "link": "https://github.com/Noisk8/Instalando-Renardo-FoxDot-En-linux",
            "area": "Sistemas / Automatización",
        },
        {
            "name": "renardo",
            "description": "Fork modernizado de FoxDot para livecoding musical en Python.",
            "tech": ["Python", "Audio", "Livecoding"],
            "link": "https://github.com/Noisk8/renardo",
            "area": "Python creativo",
        },
        {
            "name": "CampamentoRandomOriented",
            "description": "Material Python para toke RandomOriented, orientado a experimentación sonora.",
            "tech": ["Python", "OSC"],
            "link": "https://github.com/Noisk8/CampamentoRandomOriented",
            "area": "Python creativo",
        },
        {
            "name": "CHIRRILAND",
            "description": "Juego 2D con Pygame, pensado para acompañar sesiones de livecoding.",
            "tech": ["Python", "Pygame"],
            "link": "https://github.com/Noisk8/CHIRRILAND",
            "area": "Python / Juegos",
        },
        {
            "name": "convert-format",
            "description": "CLI para convertir audio de FLAC a WAV de forma rápida.",
            "tech": ["Python", "Audio", "CLI"],
            "link": "https://github.com/Noisk8/convert-format",
            "area": "Python / Automatización",
        },
        {
            "name": "PIR-Raspberrypi",
            "description": "Trigger de sonidos con sensor PIR en Raspberry Pi.",
            "tech": ["Python", "Raspberry Pi"],
            "link": "https://github.com/Noisk8/PIR-Raspberrypi",
            "area": "IoT / Creativo",
        },
        {
            "name": "opencv_chimbianding",
            "description": "Experimentos con OpenCV para manipulación visual.",
            "tech": ["Python", "OpenCV"],
            "link": "https://github.com/Noisk8/opencv_chimbianding",
            "area": "Visión",
        },
        {
            "name": "el_rincon_de_la_privacidad",
            "description": "Sitio informativo sobre privacidad construido con TypeScript/Parcel.",
            "tech": ["TypeScript", "Frontend"],
            "link": "https://github.com/Noisk8/el_rincon_de_la_privacidad",
            "area": "Frontend",
        },
        {
            "name": "esdup2023",
            "description": "Web astro para \"El sueño de una pensión\".",
            "tech": ["Astro", "Frontend"],
            "link": "https://github.com/Noisk8/esdup2023",
            "area": "Frontend",
        },
        {
            "name": "RadioKBalah",
            "description": "Sitio en Astro para la plataforma de radio experimental KBalah.",
            "tech": ["Astro", "Frontend"],
            "link": "https://github.com/Noisk8/RadioKBalah",
            "area": "Frontend",
        },
        {
            "name": "landing_harbour-master",
            "description": "Landing pages para gateways DAO orientadas a privacidad.",
            "tech": ["HTML", "CSS"],
            "link": "https://github.com/Noisk8/landing_harbour-master",
            "area": "Frontend",
        },
        {
            "name": "montando_nodo_nym",
            "description": "Notas para montar y operar nodos Nym.",
            "tech": ["Nym", "Infra"],
            "link": "https://github.com/Noisk8/montando_nodo_nym",
            "area": "Sistemas",
        },
    ]

    context = {
        "profile": profile,
        "skills": skills,
        "projects": projects,
        "wikimedia": wikimedia,
    }
    return render(request, "portfolio/home.html", context)

# Create your views here.
