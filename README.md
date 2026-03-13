# Markdown to PDF Converter 📄

Une application Streamlit élégante et complète pour convertir des fichiers Markdown en PDF, HTML ou DOCX.

## Fonctionnalités

### ✨ Conversion de base
- **Import facile** : Importez des fichiers Markdown ou collez directement du contenu
- **Édition en direct** : Modifiez votre Markdown en temps réel
- **Prévisualisation live** : Visualisez le rendu pendant que vous tapez

### 📤 Export multi-format
- **PDF** : Export avec mise en page professionnelle
- **HTML** : Export HTML autonome avec CSS intégré
- **DOCX** : Export Word compatible

### 📐 Options de page avancées
- **Formats de page** : A4, A5, Letter, Legal
- **Orientation** : Portrait ou Paysage
- **Marges personnalisables** : Haut, bas, gauche, droite
- **En-tête/Pied de page** : Texte personnalisé et numérotation
- **Table des matières** : Génération automatique
- **Filigrane** : Texte en arrière-plan

### 🎨 Thèmes
- **Professionnel** : Style business moderne
- **Académique** : Style universitaire avec serif
- **Minimaliste** : Design épuré
- **Moderne** : Couleurs vives contemporaines

### 📁 Gestion des fichiers
- **Import depuis URL** : Chargez un fichier .md distant
- **Conversion par lot** : Convertissez plusieurs fichiers à la fois
- **Historique des exports** : Suivez vos dernières conversions
- **Nom de fichier personnalisable** : Définissez le nom avant téléchargement

### 📚 Aide intégrée
- **Cheatsheet Markdown** : Référence rapide de la syntaxe
- **Compteur de statistiques** : Mots, caractères, lignes

## Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/DylaneTrader/markdown-to-pdf.git
cd markdown-to-pdf
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

Lancez l'application Streamlit :
```bash
streamlit run app.py
```

L'application s'ouvrira dans votre navigateur à `http://localhost:8501`

## Guide d'utilisation

1. **Importer** : Uploadez un fichier Markdown ou collez votre contenu dans l'éditeur
2. **Configurer** : Utilisez la sidebar pour ajuster les options (format, marges, thème)
3. **Prévisualiser** : Vérifiez le rendu dans le panneau de droite
4. **Exporter** : Cliquez sur "Générer PDF/HTML/DOCX" puis téléchargez

## Dépendances

- `streamlit` : Framework d'application web
- `markdown` : Conversion Markdown vers HTML
- `xhtml2pdf` : Conversion HTML vers PDF
- `python-docx` : Génération de fichiers DOCX
- `requests` : Téléchargement depuis URL
- `Pillow` : Support d'images

## Déploiement Streamlit Cloud

Pour le déploiement sur Streamlit Cloud, le fichier `packages.txt` est requis pour installer les dépendances système nécessaires.

## License

MIT License