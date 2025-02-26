#esercizio3C5

utente : dict = {"nome" : str(input("Inserisci il nome utente: ")), "ruolo" : str(input("Inserire il ruolo: ")), "età" : int(input("Inserire l'età: "))}  

match utente:
    case utente if utente["ruolo"] == "admin":
        print("Accesso completo a tutte le funzionalità") 
    case utente if utente["ruolo"] == "moderatore":
        print("Può gestire i contenuti ma non modificare le impostazioni")
    case utente if utente["ruolo"] == "ospite":
        print("Accesso ristretto! Solo visualizzazione dei contenuti")
    case uente if utente["ruolo"] !=["admin", "operatore", "ospite"]:
        print("Attenzione!Ruolo non riconosciuto!Accesso negato!")
    case utente if utente["età"] >= 18:
        print("Accesso standard a tutti i servizi")
    case utente if utente["età"] < 18:
        print("Accesso limitato! Alcune funzionalità sono bloccate")

