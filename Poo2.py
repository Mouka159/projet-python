produits = {
    "ordinateur": 300,
    "telephone": 250,
    "imprimante": 150,
    "clavier": 100,
}

class SmartShop:
    def __init__(self):
        self.panier = {}

    def saisir_client(self):
        print("====== Information du client ======")
        nom = input("Entrer le nom du client: ")
        email = input("Entrer l'email du client: ")
        client = {"nom": nom, "email": email}
        return client

    def afficher_produits(self):
        print("====== Les produits disponibles ======")
        for nom, prix in produits.items():
            print(f"- {nom} : {prix} FCFA")

    def saisir_commande(self):
        commande = {}
        while True:
            self.afficher_produits()
            produit = input("\nEntrer le nom du produit: ")
            if produit not in produits:
                print("Produit non disponible. Veuillez réessayer.")
                continue
            try:
                quantite = int(input("Entrer la quantité: "))
                if quantite <= 0:
                    print("La quantité doit être supérieure à 0.")
                    continue
            except ValueError:
                print("Veuillez entrer un nombre valide.")
                continue
            if produit in commande:
                commande[produit] += quantite
            else:
                commande[produit] = quantite
            continuer = input("Souhaitez-vous ajouter un autre produit? (oui/non): ").lower()
            if continuer != "oui":
                break
        return commande

    def calcul_total(self, commande):
        total = 0
        for produit, quantite in commande.items():
            total += produits[produit] * quantite
        return total

    def afficher_resultat(self, client, commande):
        print("+++++++++ RÉCAPITULATIF +++++++++")
        print(f"Client: {client['nom']}")
        print(f"Email: {client['email']}\n")
        for produit, quantite in commande.items():
            print(f"- {produit} x {quantite} = {produits[produit] * quantite} FCFA")
        total = self.calcul_total(commande)
        print(f"\nTotal à payer : {total} FCFA")

def main():
    print("Bienvenue sur SmartShop\n")
    shop = SmartShop()
    client = shop.saisir_client()
    commande = shop.saisir_commande()
    shop.afficher_resultat(client, commande)

main()