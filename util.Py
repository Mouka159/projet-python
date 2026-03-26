# Dictionnaire des produits avec prix et stock
produits = {
    "ordinateur": {"prix": 300, "stock": 10},
    "telephone": {"prix": 250, "stock": 5},
    "imprimante": {"prix": 150, "stock": 8},
    "clavier": {"prix": 100, "stock": 12},
    "souris": {"prix": 80, "stock": 20}
}

class SmartShop:
    def __init__(self):
        self.panier = {}

    def saisir_client(self):
        print("====== Information du client ======")
        nom = input("Entrez le nom du client: ")
        email = input("Entrez l'email du client: ")
        return {"nom": nom, "email": email}

    def afficher_produits(self):
        print("\n====== Produits disponibles ======")
        for nom, info in produits.items():
            print(f"- {nom} : {info['prix']} FCFA (stock : {info['stock']})")

    def saisir_commande(self):
        commande = {}
        while True:
            self.afficher_produits()
            produit = input("\nEntrez le nom du produit: ").lower()
            if produit not in produits:
                print("Produit non disponible. Veuillez réessayer.")
                continue
            try:
                quantite = int(input("Entrez la quantité: "))
                if quantite <= 0:
                    print("La quantité doit être supérieure à 0.")
                    continue
                if quantite > produits[produit]["stock"]:
                    print("Stock insuffisant. Veuillez choisir une quantité plus petite.")
                    continue
            except ValueError:
                print("Veuillez entrer un nombre valide.")
                continue

            # Ajouter au panier
            commande[produit] = commande.get(produit, 0) + quantite
            # Mettre à jour le stock
            produits[produit]["stock"] -= quantite

            continuer = input("Souhaitez-vous ajouter un autre produit ? (oui/non): ").lower()
            if continuer != "oui":
                break
        return commande

    def calcul_total(self, commande):
        return sum(produits[p]["prix"] * q for p, q in commande.items())

    def afficher_resultat(self, client, commande):
        print("\n+++++++++ RÉCAPITULATIF +++++++++")
        print(f"Client: {client['nom']}")
        print(f"Email: {client['email']}\n")

        for produit, quantite in commande.items():
            print(f"- {produit} x {quantite} = {produits[produit]['prix'] * quantite} FCFA")

        total = self.calcul_total(commande)

        if total > 1000:
            remise = total * 0.10
            total_final = total - remise
            print(f"\nTotal brut : {total} FCFA")
            print(f"Remise appliquée (10%) : -{remise} FCFA")
            print(f"Total à payer : {total_final} FCFA")
        else:
            print(f"\nTotal à payer : {total} FCFA")

        print("\n====== Stock restant ======")
        for nom, info in produits.items():
            print(f"- {nom} : {info['stock']}")

def main():
    print("Bienvenue sur SmartShop\n")
    shop = SmartShop()
    client = shop.saisir_client()
    commande = shop.saisir_commande()
    shop.afficher_resultat(client, commande)

main()
