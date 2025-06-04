# FixerReunion

Solution pour fixer des réunions en fonction des disponibilités CalDAV et des préférences utilisateurs.

## Licence

Ce projet est distribué sous licence **GNU Affero General Public License v3.0**. Le texte complet se trouve dans le fichier [LICENSE](LICENSE).

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

---

Cette application fournit un exemple minimal de service de planification de r\u00e9unions avec Django.

## D\u00e9veloppement local

```bash
# cloner le d\u00e9p\u00f4t puis construire l'image
docker build -t fixerreunion .
# lancer le serveur
docker run -p 8000:8000 fixerreunion
```

L'application sera disponible sur `http://localhost:8000/creer/`.
