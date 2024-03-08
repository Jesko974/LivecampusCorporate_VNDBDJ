# LivecampusCorporate_VNDBDJ

# Projet "Hello World" avec Filebeat

Ce projet vise à créer une application "Hello World" avec une architecture de microservices, la collecte des logs à l'aide de Filebeat, et la visualisation des logs dans Kibana.

## Contenu du projet

Le projet comprend les fichiers suivants :

- **Dockerfile** : Définit la construction de l'image Docker pour notre application.
- **index.html** : Fichier HTML pour l'application "Hello World".
- **nginx.conf** : Configuration nginx pour servir l'application.
- **docker-compose.yml** : Fichier de configuration Docker Compose pour déployer les services.
- **filebeat.yml** : Configuration Filebeat pour la collecte des logs.

## Déploiement

Pour déployer l'application, suivez ces étapes :

1. Assurez-vous d'avoir Docker et Docker Compose installés sur votre système.
2. Clonez ce dépôt sur votre machine.
3. Dans le répertoire du projet, exécutez la commande suivante pour construire les images Docker et démarrer les services :

    ```
    docker-compose up -d
    ```

4. Accédez à l'URL spécifiée dans le fichier docker-compose.yml pour voir l'application web.

## Collecte des Logs

Filebeat est utilisé pour collecter les logs de l'application et les envoyer à Elasticsearch pour le stockage. Vous pouvez accéder à l'interface utilisateur de Kibana pour visualiser et analyser les logs collectés.

Pour accéder à Kibana, utilisez l'URL spécifiée dans le fichier docker-compose.yml.

