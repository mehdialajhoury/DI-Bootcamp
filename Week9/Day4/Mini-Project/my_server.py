from mcp.server.fastmcp import FastMCP

# Initialisation de votre serveur
mcp = FastMCP("SmartSentinel")

@mcp.tool()
def analyze_risk(text: str) -> str:
    """
    Analyse le texte d'une issue ou d'un fichier pour évaluer son niveau de risque.
    Retourne un score (0-10) et une catégorie (LOW, MEDIUM, HIGH, CRITICAL).
    """
    text = text.lower()
    score = 0
    
    # Mots-clés pondérés
    critical_words = ["security", "vulnerability", "hack", "breach", "fatal", "production down"]
    high_words = ["crash", "broken", "urgent", "error", "exception", "timeout"]
    medium_words = ["bug", "fix", "warning", "latency", "slow"]

    for word in critical_words:
        if word in text: score += 5
    for word in high_words:
        if word in text: score += 3
    for word in medium_words:
        if word in text: score += 1

    # Normalisation
    final_score = min(score, 10)
    
    if final_score >= 8:
        category = "CRITICAL"
    elif final_score >= 5:
        category = "HIGH"
    elif final_score >= 2:
        category = "MEDIUM"
    else:
        category = "LOW"

    return f"Risk Score: {final_score}/10 | Category: {category}"

@mcp.tool()
def recommend_action(risk_category: str) -> str:
    """
    Recommande une action officielle basée sur la catégorie de risque (LOW, MEDIUM, HIGH, CRITICAL).
    Utilisez le résultat de 'analyze_risk' pour fournir la catégorie.
    """
    category = risk_category.upper()
    
    if "CRITICAL" in category:
        return "ACTION REQUISE: Escalader immédiatement au CTO. Créer un ticket P0. Ne pas écrire de code tant que ce n'est pas validé."
    elif "HIGH" in category:
        return "ACTION REQUISE: Créer un ticket prioritaire. Assigner à un développeur senior."
    elif "MEDIUM" in category:
        return "ACTION REQUISE: Ajouter au backlog du prochain sprint."
    else:
        return "ACTION REQUISE: Aucune action immédiate. Surveiller."

if __name__ == "__main__":
    # Lance le serveur en mode stdio (communication standard)
    mcp.run()