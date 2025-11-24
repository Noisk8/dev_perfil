try:
    from django.shortcuts import render  # type: ignore[import]
    from django.http import HttpResponse  # type: ignore[import]
    from django.template.loader import render_to_string  # type: ignore[import]
    from django.templatetags.static import static  # type: ignore[import]
    from django.utils.translation import gettext_lazy as _  # type: ignore[import]
except Exception:
    # Fallbacks for static analysis or environments sin Django instalado.
    def render(request, template_name, context=None):
        return {"template": template_name, "context": context}

    class HttpResponse(dict):  # type: ignore[misc]
        def __init__(self, content="", status=200, content_type=None):
            super().__init__(content=content, status=status, content_type=content_type)

    def render_to_string(template_name, context=None, request=None):
        return ""

    def static(path):
        return path

    def _(s):
        return s

try:
    from weasyprint import HTML, CSS  # type: ignore[import]
except Exception:
    HTML = None
    CSS = None


def _portfolio_context():
    profile = {
        "name": "Noisk8",
        "tagline": _("Livecoder, Pythonista, Node Operator y contribuidor Wikimedia."),
        "bio": _(
            "Desarrolloador Multimedia y experiencias creativas con Python y javascript, automatizo tareas en Linux "
            "y despliego infra que prioriza privacidad. Contribuyo en el ecosistema Wikimedia "
            "(Wikidata/Toolforge) y experimento con frontend (Astro/NextJs/ReactJs/ TS) para dar forma a ideas rápidas."
        ),
        "location": _("Medellín, Colombia"),
        "links": {
            "github": "https://github.com/Noisk8",
            "website": "www.noisk8.xyz",
            "twitter": "https://x.com/noisk8",
        },
    }

    skills = [
        {
            "title": _("Python  creativo"),
            "items": [
                _("Django"),
                _("Pygame"),
                _("OSC"),
                _("Livecoding (FoxDot/renardo)"),
                _("OpenCV"),
                _("Automatización CLI"),
                _("Procesamiento de audio"),
            ],
        },
        {
            "title": _("Sistemas y redes"),
            "items": [
                _("Linux"),
                _("Bash"),
                _("Raspberry Pi"),
                _("Servicios auto-hosteados"),
                _("Nodos Nym"),
            ],
        },
        {
            "title": _("Frontend ligero"),
            "items": [
                _("Astro"),
                _("ReactJs/NextJs"),
                _("TypeScript"),
                _("HTML/CSS creativo"),
                _("Experimentos audiovisuales"),
            ],
        },
        {
            "title": _("Ecosistema Wikimedia"),
            "items": [
                _("Wikidata (edición masiva)"),
                _("Toolforge (Python/nodejs)"),
                _("Documentación de comunidad"),
            ],
        },
    ]

    wikimedia = {
        "contributions": [
            {
                "title": _("Contribuidor Wikidata"),
                "description": _("Ediciones y curaduría de datos abiertos en Wikidata."),
                "link": "https://www.wikidata.org/wiki/Special:Contributions/Juan_Andres_Jaramillo_Silva",
                "tech": ["SPARQL", "Datos abiertos"],
            },
            {
                "title": _("Código en Wikitech"),
                "description": _("Repos en GitLab de Wikimedia para herramientas y bots."),
                "link": "https://gitlab.wikimedia.org/noisk8",
                "tech": ["Python", "Toolforge"],
            },
        ],
        "tools": [
            {
                "name": "ecosdeunmural.toolforge.org",
                "description": _("Recorrido web para documentar intervenciones urbanas."),
                "link": "https://ecosdeunmural.toolforge.org/",
                "tech": ["Toolforge", "Frontend"],
            },
            {
                "name": "memorial.toolforge.org",
                "description": _("Memorial de datos en Wikimedia como sitio navegable."),
                "link": "https://memorial.toolforge.org/",
                "tech": ["Toolforge", "Python"],
            },
            {
                "name": "linea-de-tiempo-falsos-positivos.toolforge.org",
                "description": _("Línea de tiempo interactiva basada en datos públicos."),
                "link": "https://linea-de-tiempo-falsos-positivos.toolforge.org/",
                "tech": ["Toolforge", "Frontend"],
            },
        ],
    }

    projects = [
        {
            "name": "Hidropoéticas",
            "description": _("Sitio web performativo con narrativa audiovisual y exploración territorial."),
            "tech": ["Frontend", "Astro"],
            "link": "https://hidropoeticas-web.vercel.app/",
            "area": _("Frontend"),
        },
        {
            "name": "Yo quiero aprender",
            "description": _("Plataforma educativa de Platohedro con contenidos y recursos interactivos."),
            "tech": ["Frontend", "Experiencias educativas"],
            "link": "https://yoquieroaprender.platohedro.org/",
            "area": _("Frontend"),
        },
        {
            "name": "Territorios de Gol",
            "description": _("Sitio narrativo sobre fútbol, territorio y comunidad."),
            "tech": ["Frontend", "Storytelling"],
            "link": "https://territoriosdegol.motivandoalagyal.org/",
            "area": _("Frontend"),
        },
        {
            "name": "Instalando-Renardo-FoxDot-En-linux",
            "description": _("Script Bash para dejar listo el entorno de livecoding Renardo/FoxDot en Linux."),
            "tech": ["Bash", "Linux"],
            "link": "https://github.com/Noisk8/Instalando-Renardo-FoxDot-En-linux",
            "area": _("Sistemas / Automatización"),
        },
        {
            "name": "renardo",
            "description": _("Fork modernizado de FoxDot para livecoding musical en Python."),
            "tech": ["Python", "Audio", "Livecoding"],
            "link": "https://github.com/Noisk8/renardo",
            "area": _("Python creativo"),
        },
        {
            "name": "CampamentoRandomOriented",
            "description": _("Material Python para toke RandomOriented, orientado a experimentación sonora."),
            "tech": ["Python", "OSC"],
            "link": "https://github.com/Noisk8/CampamentoRandomOriented",
            "area": _("Python creativo"),
        },
        {
            "name": "CHIRRILAND",
            "description": _("Juego 2D con Pygame, pensado para acompañar sesiones de livecoding."),
            "tech": ["Python", "Pygame"],
            "link": "https://github.com/Noisk8/CHIRRILAND",
            "area": _("Python / Juegos"),
        },
        {
            "name": "convert-format",
            "description": _("CLI para convertir audio de FLAC a WAV de forma rápida."),
            "tech": ["Python", "Audio", "CLI"],
            "link": "https://github.com/Noisk8/convert-format",
            "area": _("Python / Automatización"),
        },
        {
            "name": "PIR-Raspberrypi",
            "description": _("Trigger de sonidos con sensor PIR en Raspberry Pi."),
            "tech": ["Python", "Raspberry Pi"],
            "link": "https://github.com/Noisk8/PIR-Raspberrypi",
            "area": _("IoT / Creativo"),
        },
        {
            "name": "opencv_chimbianding",
            "description": _("Experimentos con OpenCV para manipulación visual."),
            "tech": ["Python", "OpenCV"],
            "link": "https://github.com/Noisk8/opencv_chimbianding",
            "area": _("Visión"),
        },
        {
            "name": "el_rincon_de_la_privacidad",
            "description": _("Sitio informativo sobre privacidad construido con TypeScript/Parcel."),
            "tech": ["TypeScript", "Frontend"],
            "link": "https://github.com/Noisk8/el_rincon_de_la_privacidad",
            "area": _("Frontend"),
        },
        {
            "name": "esdup2023",
            "description": _("Web astro para \"El sueño de una pensión\"."),
            "tech": ["Astro", "Frontend"],
            "link": "https://github.com/Noisk8/esdup2023",
            "area": _("Frontend"),
        },
        {
            "name": "RadioKBalah",
            "description": _("Sitio en Astro para la plataforma de radio experimental KBalah."),
            "tech": ["Astro", "Frontend"],
            "link": "https://github.com/Noisk8/RadioKBalah",
            "area": _("Frontend"),
        },
        {
            "name": "landing_harbour-master",
            "description": _("Landing pages para gateways DAO orientadas a privacidad."),
            "tech": ["HTML", "CSS"],
            "link": "https://github.com/Noisk8/landing_harbour-master",
            "area": _("Frontend"),
        },
        {
            "name": "montando_nodo_nym",
            "description": _("Notas para montar y operar nodos Nym."),
            "tech": ["Nym", "Infra"],
            "link": "https://github.com/Noisk8/montando_nodo_nym",
            "area": _("Sistemas"),
        },
    ]

    context = {
        "profile": profile,
        "skills": skills,
        "projects": projects,
        "wikimedia": wikimedia,
    }

    return context


def home(request):
    context = _portfolio_context()
    context["pdf_mode"] = False
    return render(request, "portfolio/home.html", context)


def cv_pdf(request):
    if HTML is None or CSS is None:
        return HttpResponse("WeasyPrint no está instalado en el entorno.", status=500)

    context = _portfolio_context()
    context["pdf_mode"] = True
    html_string = render_to_string("portfolio/home.html", context, request=request)
    base_url = request.build_absolute_uri("/")
    css_url = request.build_absolute_uri(static("portfolio/styles.css"))

    pdf_file = HTML(string=html_string, base_url=base_url).write_pdf(
        stylesheets=[CSS(css_url)]
    )

    response = HttpResponse(pdf_file, content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="perfil_noisk8.pdf"'
    return response

# Create your views here.
