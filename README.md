# MIAGE G4 – Domaine F : Rapports (Matières, Enseignants, Présences)

Ce projet fait partie du travail collaboratif MIAGE G4.  
Le Domaine F consiste à **extraire, afficher et exporter des rapports** basés sur des **API externes** fournies par d’autres groupes.

Les rapports disponibles sont :
- Rapport des **matières**
- Rapport des **enseignants**
- Rapport des **présences**
- Export **PDF** pour chaque rapport

---

## 📌 Objectifs du Domaine F

- Consommer plusieurs API externes (enseignants, matières, présences)
- Afficher les données dans des tableaux HTML propres
- Ajouter des filtres (présences)
- Générer des rapports PDF professionnels
- Organiser le code de manière claire et modulaire

---

## 🏗️ Architecture du projet

rapports/
│
├── api_clients/
│   ├── matieres.py
│   ├── enseignants.py
│   └── presences.py
│
├── templates/
│   └── rapports/
│       ├── matieres.html
│       ├── enseignants.html
│       └── presences.html
│
├── pdf_utils.py
├── views.py
└── urls.py

Code

---

## 🌐 APIs utilisées

### 🔹 API Matières
GET http://10.3.0.145:5000/matieres

Code

### 🔹 API Enseignants
GET http://10.3.17.208:5000/enseignants

Code

### 🔹 API Présences
GET https://si-presences-gbh.onrender.com/api/cours/

Code

Paramètres disponibles :
- `date`
- `classe_id`
- `enseignant_id`

---

## 📊 Fonctionnalités principales

### ✔ Rapport Matières
- Affichage du code matière
- Intitulé
- Année universitaire
- Volume horaire
- Export PDF

### ✔ Rapport Enseignants
- Nom / Prénom
- Email
- Statut
- Raison sociale
- Ministère / Collectivité
- Export PDF

### ✔ Rapport Présences
- Date
- Heure début / fin
- Matière
- Enseignant
- Classe
- Salle
- Nombre d’heures
- Filtres dynamiques
- Export PDF

---

## 📄 Export PDF

Chaque rapport possède un bouton permettant de générer un PDF :

- `/rapports/matieres/pdf/`
- `/rapports/enseignants/pdf/`
- `/rapports/presences/pdf/`

Les PDF sont générés via **ReportLab**.

---

## ⚙️ Installation et exécution

### 1. Installer les dépendances
```bash
pip install -r requirements.txt
2. Installer ReportLab
bash
pip install reportlab
3. Lancer le serveur Django
bash
python manage.py runserver
4. Accéder aux rapports
Matières : http://127.0.0.1:8000/rapports/matieres/

Enseignants : http://127.0.0.1:8000/rapports/enseignants/

Présences : http://127.0.0.1:8000/rapports/presences/

🚧 Difficultés rencontrées
🔸 Intégration des API externes
Formats JSON différents

Absence de documentation complète

Gestion des erreurs réseau

🔸 Organisation du projet
Nécessité de séparer clairement les domaines

Abandon de la partie “compositions” pour se concentrer sur les rapports

🔸 Migrations Django
Modèles incomplets

Champs non initialisés

Routes mal configurées
