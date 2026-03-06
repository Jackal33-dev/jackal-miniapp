let tg = window.Telegram.WebApp;

function commander(produit, prix, quantite) {
    const data = {
        produit: produit,
        prix: prix,
        quantite: quantite
    };
    // envoyer les données au bot
    tg.sendData(produit);
    alert("Commande envoyée !");
}

