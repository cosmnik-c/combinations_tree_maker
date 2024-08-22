import sys
import requests
import json
from graphviz import Digraph

sys.stdout.write("\nFetching elements, please wait... ")
sys.stdout.flush()
response = requests.get("https://eelements.apps.adamenglish.net/statistics/getElements.php")
sys.stdout.write("Done\n\n")
responseText = response.text

rec1 = json.loads(responseText)
recipes = {e["id"]: e for e in rec1} 

def getElementTree(id):
    if len(recipes[id]["parents"]) != 2: return id
    return {id: [getElementTree(recipes[id]["parents"][0]),getElementTree(recipes[id]["parents"][1])]}


dot = Digraph()
def visualizeTree(tree: dict, saved:set = set()): #i have no idea what i'm doing
    id = tree if type(tree) in (float, int) else list(tree.keys())[0]
    if id in saved: return
    saved.add(id)
    
    dot.node(str(id), recipes[id]["name"])
    if type(tree) in (float, int): return

    dot.edge(str(tree[id][0]) if type(tree[id][0]) in (float, int) else str(list(tree[id][0].keys())[0]), str(id))
    dot.edge(str(tree[id][1]) if type(tree[id][1]) in (float, int) else str(list(tree[id][1].keys())[0]), str(id))

    visualizeTree(tree[id][0])
    visualizeTree(tree[id][1])


element_id = int(input("Element ID: "))
element_tree = getElementTree(element_id)

visualizeTree(element_tree)
name = str(element_id)
dot.render("./" + name, format='png', view=True)
