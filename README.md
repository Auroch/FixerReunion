# FixerReunion

Solution pour fixer des réunions en fonction des disponibilités CalDAV et des préférences utilisateurs.

## Prérequis

- **Python ≥3.10** avec `pip`
- **Docker** (facultatif mais recommandé pour la base de données et l’IA)

## Installation des dépendances

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Variables d’environnement

- `CALDAV_URL` – URL du serveur CalDAV
- `CALDAV_USERNAME` et `CALDAV_PASSWORD` – identifiants de connexion
- `LLM_ENDPOINT` – URL du service d’IA (Ollama ou LocalAI)

Exportez ces variables avant de lancer les commandes Django.

## Initialisation de la base de données

```bash
python manage.py migrate
python manage.py createsuperuser
```

## Lancement de l’application

```bash
python manage.py runserver 0.0.0.0:8000
```

## Composant IA (Ollama ou LocalAI)

Vous pouvez exécuter le service d’IA avec Docker :

```bash
docker run -p 11434:11434 ollama/ollama # ou localai/localai
```

Pointez ensuite `LLM_ENDPOINT` vers `http://localhost:11434`.
