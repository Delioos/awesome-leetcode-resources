import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def create_graph(has_cycle=True):
    G = nx.DiGraph()
    nodes = ["Start", "Python", "Data", "AI", "Cloud", "Security", "DevOps", "Quantum"]
    for i in range(len(nodes) - 1):
        G.add_edge(nodes[i], nodes[i+1])
    if has_cycle:
        G.add_edge(nodes[-1], nodes[1])
    return G, nodes

def detect_cycle(G, nodes):
    tortue = nodes[0]
    lievre = nodes[0]
    step = 0
    
    while True:
        step += 1
        
        yield tortue, lievre, step
        
        # Avancer la tortue d'un nœud
        tortue = list(G.successors(tortue))[0] if list(G.successors(tortue)) else None
        
        # Avancer le lièvre de deux nœuds
        for _ in range(2):
            lievre = list(G.successors(lievre))[0] if list(G.successors(lievre)) else None
            if lievre is None:
                yield None, None, step  # Pas de cycle
                return
        
        # Vérifier si un cycle est détecté
        if tortue == lievre:
            yield tortue, lievre, step
            return
        
        # Vérifier si on a atteint la fin du graphe
        if tortue is None or lievre is None:
            yield None, None, step
            return

def update(frame):
    ax.clear()
    tortue, lievre, step = frame
    
    # Dessiner le graphe
    nx.draw(G, pos, ax=ax, with_labels=True, node_color='lightgreen', 
            node_size=3000, font_size=10, font_weight='bold', 
            arrows=True, arrowsize=20)

    # Mettre en évidence les pointeurs
    if tortue:
        nx.draw_networkx_nodes(G, pos, nodelist=[tortue], node_color='lightskyblue', node_size=3500)
    if lievre:
        nx.draw_networkx_nodes(G, pos, nodelist=[lievre], node_color='plum', node_size=3500)

    # Mettre en évidence le nœud de rencontre en orange clair
    if tortue == lievre and tortue is not None:
        nx.draw_networkx_nodes(G, pos, nodelist=[tortue], node_color='lightsalmon', node_size=3500)

    ax.set_title(f"Détection de cycle - Étape {step}", fontsize=16)
    ax.text(0.5, -0.1, f"Tortue: {tortue}, Lièvre: {lievre}", ha='center', va='center', transform=ax.transAxes)
    
    if tortue == lievre and tortue is not None:
        ax.text(0.5, 1.1, "Cycle détecté !", ha='center', va='center', transform=ax.transAxes, color='red', fontsize=16)
    elif tortue is None or lievre is None:
        ax.text(0.5, 1.1, "Pas de cycle trouvé", ha='center', va='center', transform=ax.transAxes, color='green', fontsize=16)

# Création du graphe
G, nodes = create_graph(has_cycle=True)  # Changer à False pour un graphe sans cycle
pos = nx.spring_layout(G, k=1, iterations=50)

# Configuration de l'animation
fig, ax = plt.subplots(figsize=(12, 8))
ani = FuncAnimation(fig, update, frames=detect_cycle(G, nodes), interval=1000, repeat=False)

plt.tight_layout()
plt.show()
