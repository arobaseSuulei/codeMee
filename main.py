import os
from dotenv import load_dotenv
from smolagents import CodeAgent,OpenAIServerModel,InferenceClientModel, DuckDuckGoSearchTool,tool
import os


    
load_dotenv()

OPENAI_API_TOKEN=os.environ.get("OPENAI_API_TOKEN")



@tool
def writing_code(filepath:str,content:str)->str:
    """ Ecris ou remplace entierement le contenu d un fichier
    
    Args:
        filepath: le chemin du fichier (exemple, code.py ici pas dans main.py)
        content: le nouveau contenu complet du fichier
    """
    with open(filepath,"w",encoding="utf-8") as f:
        f.write(content)
    return f"Fichier {filepath} mis a jour (++{len(content)})"
    

@tool
def read_file(filepath:str)->str:
    """ Lis le contenu d un fichier 
    
    Args:
        filepath: le chemin du fichier a lire
    """
    with open(filepath,"r",encoding="utf-8") as f:
        return f.read()
        
        

model = OpenAIServerModel(
    model_id="gpt-4o-mini",
    api_key=OPENAI_API_TOKEN,
)

agent = CodeAgent(
    tools=[read_file,writing_code],
    model=model,
    instructions="Quand on te demande de modifier du code, utilise TOUJOURS l'outil "
                 "writing_code pour sauvegarder le résultat sur disque. Ne te contente "
                 "jamais de donner le code en texte dans ta réponse finale."
)

agent.run("Créer moi 2 fonctions dans code.py une qui fais la division et l autre qui fait une addition")