# Documentation - Agent IA de coding

## Francais

### Presentation

Ce projet est un agent d'intelligence artificielle concu pour aider a lire, ecrire et modifier du code dans un projet local. Il utilise `smolagents` avec un modele OpenAI et expose des outils simples que l'agent peut appeler pour travailler sur les fichiers.

L'objectif principal est de permettre a l'agent de comprendre une demande de developpement, de consulter les fichiers necessaires, puis d'enregistrer directement les modifications sur disque.

### Fonctionnement general

Le fichier principal est `main.py`. Il charge les variables d'environnement, configure le modele OpenAI, declare les outils disponibles, puis lance l'agent avec une instruction utilisateur.

Les outils disponibles sont :

- `read_file(filepath)` : lit le contenu d'un fichier local.
- `writing_code(filepath, content)` : remplace entierement le contenu d'un fichier par un nouveau contenu.

L'agent est configure pour utiliser obligatoirement `writing_code` lorsqu'il doit modifier du code. Cela evite qu'il reponde seulement avec du code dans le terminal sans sauvegarder le resultat.

### Structure du projet

- `main.py` : configuration de l'agent, du modele et des outils.
- `code.py` : fichier de code modifiable par l'agent.
- `README.md` : courte description du projet.
- `SYSTEM.md` : prompt systeme/personnalisation du comportement attendu.
- `MEMORY.md` : fichier prevu pour stocker de la memoire ou du contexte futur.
- `.env` : fichier local contenant les variables sensibles, comme la cle API.

### Prerequis

Avant d'executer le projet, il faut avoir :

- Python 3.11 ou une version compatible.
- Un environnement virtuel Python.
- Les dependances installees, notamment `smolagents`, `python-dotenv` et les librairies liees au modele utilise.
- Une cle API OpenAI dans le fichier `.env`.

Exemple de variable attendue :

```env
OPENAI_API_TOKEN=your_api_key_here
```

### Lancement

Depuis la racine du projet :

```bash
source venv/bin/activate
python main.py
```

Actuellement, `main.py` lance directement une demande de test :

```python
agent.run("Créer moi 2 fonctions dans code.py une qui fais la division et l autre qui fait une addition")
```

Pour utiliser l'agent sur une autre tache, il suffit de remplacer cette instruction par une nouvelle demande.

### Exemple d'utilisation

Demande possible :

```python
agent.run("Ajoute une fonction multiplication dans code.py")
```

L'agent peut alors lire `code.py`, generer le nouveau contenu et sauvegarder le fichier avec `writing_code`.

### Points importants

- L'outil `writing_code` remplace tout le contenu du fichier cible.
- Il faut donc demander a l'agent de conserver le code existant si necessaire.
- Les fichiers sensibles comme `.env` ne doivent pas etre partages.
- L'agent travaille uniquement avec les outils qui lui sont fournis.

### Ameliorations possibles

- Ajouter un outil qui modifie seulement une partie d'un fichier.
- Ajouter des tests automatiques apres chaque modification.
- Ajouter une interface CLI pour saisir les demandes sans modifier `main.py`.
- Ajouter une validation des chemins de fichiers pour eviter les ecritures non desirees.

---

## English

### Overview

This project is an AI coding agent designed to read, write, and modify code inside a local project. It uses `smolagents` with an OpenAI model and provides simple tools that the agent can call to interact with files.

The main goal is to let the agent understand a development request, inspect the required files, and save the resulting code changes directly to disk.

### How It Works

The main file is `main.py`. It loads environment variables, configures the OpenAI model, defines the available tools, and runs the agent with a user instruction.

Available tools:

- `read_file(filepath)` : reads the content of a local file.
- `writing_code(filepath, content)` : fully replaces a file with new content.

The agent is instructed to always use `writing_code` when it needs to modify code. This prevents it from only printing code in the terminal without actually saving the result.

### Project Structure

- `main.py` : agent, model, and tool configuration.
- `code.py` : example code file that the agent can modify.
- `README.md` : short project description.
- `SYSTEM.md` : system prompt / behavior instructions.
- `MEMORY.md` : placeholder for future memory or context.
- `.env` : local file for sensitive environment variables, such as the API key.

### Requirements

Before running the project, you need:

- Python 3.11 or a compatible version.
- A Python virtual environment.
- Required dependencies, including `smolagents`, `python-dotenv`, and the libraries needed by the selected model.
- An OpenAI API key stored in `.env`.

Expected environment variable example:

```env
OPENAI_API_TOKEN=your_api_key_here
```

### Running the Agent

From the project root:

```bash
source venv/bin/activate
python main.py
```

At the moment, `main.py` directly runs a test request:

```python
agent.run("Créer moi 2 fonctions dans code.py une qui fais la division et l autre qui fait une addition")
```

To use the agent for another coding task, replace that instruction with a new request.

### Example Usage

Possible request:

```python
agent.run("Add a multiplication function in code.py")
```

The agent can read `code.py`, generate the updated content, and save the file with `writing_code`.

### Important Notes

- `writing_code` replaces the entire target file.
- Ask the agent to preserve existing code when needed.
- Sensitive files such as `.env` should not be shared.
- The agent can only act through the tools provided to it.

### Possible Improvements

- Add a tool that edits only part of a file.
- Run automated tests after each modification.
- Add a CLI interface to submit requests without editing `main.py`.
- Validate file paths to avoid unwanted writes.
