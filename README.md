# Application de Gestion de Collection de Cafés
(english below)

## Introduction
Ce projet consiste à développer une API pour gérer une collection de cafés. Les utilisateurs peuvent ajouter de nouveaux cafés, rechercher des cafés par emplacement, afficher tous les cafés disponibles, mettre à jour les prix du café et supprimer des cafés de la collection.

## Fonctionnalités
- Affichage d'un café aléatoire à partir de la collection.
- Recherche de cafés par emplacement.
- Ajout de nouveaux cafés à la collection.
- Mise à jour des prix du café.
- Suppression de cafés de la collection.

## Technologies Utilisées
- Python 3.x
- Flask : Framework web pour les applications Python.
- Flask-SQLAlchemy : Intégration de SQLAlchemy dans Flask pour la gestion de la base de données.
- SQLite : Base de données SQL légère pour stocker les informations sur les cafés.
- Postman : Outil de test et de documentation des API.

## Installation et Configuration
1. Assurez-vous d'avoir Python 3.x installé sur votre système.
2. Clonez ou téléchargez les fichiers du projet à partir du dépôt.
3. Installez les packages requis à l'aide de pip et du fichier `requirements.txt` : `pip install -r requirements.txt`.
4. Configurez les variables d'environnement nécessaires :
   - `TopSecretAPIKey` : Clé secrète pour l'API (à configurer dans les variables d'environnement).
5. Exécutez le script `main.py` pour démarrer l'application Flask.

## Structure du Projet
- `main.py` : Script principal contenant la logique de l'application Flask.
- `templates/` : Répertoire pour les modèles HTML.
    - `index.html` : Page d'accueil de l'API.
- `cafes.db` : Fichier de base de données SQLite pour stocker les informations sur les cafés.
- `requirements.txt` : Liste des packages Python requis.

## Utilisation
1. Exécutez l'application Flask à partir du script `main.py`.
2. Accédez à l'URL fournie par Flask dans votre navigateur ou utilisez Postman pour tester les endpoints de l'API.
3. Consultez la documentation de l'API pour comprendre les différentes requêtes et réponses possibles.

## Documentation de l'API
- La documentation complète de l'API est disponible [ici](https://documenter.getpostman.com/view/20632735/2s93RWNWaH).

## Remarques
- Assurez-vous de configurer la clé API secrète dans les variables d'environnement pour l'authentification.
- Ce projet a été réalisé dans le cadre d'un apprentissage des APIs REST avec Flask et SQLAlchemy.
- Utilisez Postman pour tester et explorer les fonctionnalités de l'API.
- Ce projet a été réalisé dans le cadre du cours [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) d'Angela Yu sur la plateforme Udemy.

---

# Application de Gestion de Collection de Cafés

## Introduction
This project aims to develop an API for managing a collection of cafes. Users can add new cafes, search for cafes by location, display all available cafes, update coffee prices, and delete cafes from the collection.

## Features
- Displays a random cafe from the collection.
- Searches for cafes by location.
- Adds new cafes to the collection.
- Updates coffee prices.
- Deletes cafes from the collection.

## Technologies Used
- Python 3.x
- Flask: Web framework for Python applications.
- Flask-SQLAlchemy: Integration of SQLAlchemy into Flask for database management.
- SQLite: Lightweight SQL database for storing cafe information.
- Postman: API testing and documentation tool.

## Installation and Configuration
1. Make sure you have Python 3.x installed on your system.
2. Clone or download the project files from the repository.
3. Install the required packages using pip and the `requirements.txt` file: `pip install -r requirements.txt`.
4. Set up the necessary environment variables:
   - `TopSecretAPIKey`: Secret key for API authentication (configure in environment variables).
5. Run the `main.py` script to start the Flask application.

## Project Structure
- `main.py`: Main script containing Flask application logic.
- `templates/`: Directory for HTML templates.
    - `index.html`: API home page.
- `cafes.db`: SQLite database file for storing cafe information.
- `requirements.txt`: List of required Python packages.

## Usage
1. Run the Flask application using the `main.py` script.
2. Access the URL provided by Flask in your web browser or use Postman to test the API endpoints.
3. Refer to the API documentation to understand the different requests and responses possible.

## API Documentation
- Full API documentation is available [here](https://documenter.getpostman.com/view/20632735/2s93RWNWaH).

## Notes
- Ensure to configure the secret API key in the environment variables for authentication.
- This project was completed as part of learning RESTful APIs with Flask and SQLAlchemy.
- Use Postman to test and explore the API functionalities.
- - This project was completed as part of the [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) course by Angela Yu on the Udemy platform.
