# Perfil de Noisk8 (Django)

Pequeña aplicación en Django que resume proyectos de Python, admin de sistemas y frontend de [@Noisk8](https://github.com/Noisk8). Incluye links directos a repos relevantes.

## Requerimientos
- Python 3.10+ recomendado
- `venv` para aislar dependencias

## Ejecutar en local
```bash
git clone <tu-repo> perfil_noisk8
cd perfil_noisk8
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\\Scripts\\activate
pip install -r requirements.txt

# Migraciones base de Django
python manage.py migrate

# Levantar
python manage.py runserver
# Visita http://127.0.0.1:8000
```

## Despliegue en GitHub (código)
1. Crea un repo vacío en GitHub.
2. Desde este directorio:
   ```bash
   git init
   git add .
   git commit -m "feat: perfil django"
   git branch -M main
   git remote add origin git@github.com:<tu-usuario>/<tu-repo>.git
   git push -u origin main
   ```
3. (Opcional) Añade un workflow de CI para asegurar que corren los tests/migraciones al hacer push.

> Nota: GitHub Pages no ejecuta Django. Para un despliegue público usa un PaaS (Railway, Render, Fly.io, Coolify, etc.), configurando las variables de entorno y un servidor WSGI (gunicorn/uvicorn) según la guía de tu proveedor.

## Personalizar contenido
- La data que nutre la página está en `portfolio/views.py` (perfil, skills, proyectos). Modifícala con nuevos repos o descripciones.
- Los estilos viven en `portfolio/static/portfolio/styles.css`.
- Templates en `templates/base.html` y `portfolio/templates/portfolio/home.html`.

## Estructura rápida
- `perfil_noisk8/` configuración del proyecto Django.
- `portfolio/` app que sirve la página con data estática.
- `templates/` templates compartidos.
- `portfolio/static/portfolio/` estilos.
