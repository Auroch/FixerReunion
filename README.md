# FixerReunion

Cette application fournit un exemple minimal de service de planification de r\u00e9unions avec Django.

## D\u00e9veloppement local

```bash
# cloner le d\u00e9p\u00f4t puis construire l'image
docker build -t fixerreunion .
# lancer le serveur
docker run -p 8000:8000 fixerreunion
```

L'application sera disponible sur `http://localhost:8000/creer/`.
