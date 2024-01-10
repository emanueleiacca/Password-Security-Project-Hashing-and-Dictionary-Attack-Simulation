import hashlib

def attacco_dizionario(file_dizionario, file_password, max_tentativi=10000):
    """
    Questa funzione tenta di decifrare le password criptate utilizzando un approccio basato su dizionario.

    Args:
    file_dizionario (str): Il percorso del file di testo contenente le parole del dizionario.
    file_password (str): Il percorso del file contenente le password criptate.
    max_tentativi (int): Numero massimo di tentativi per password (default 10000).
    """

    # Legge il file del dizionario e memorizza le parole in una lista
    #il testo dovrebbe contenere parole comuni usate per gli attacchi a dizionario
    with open(file_dizionario, 'r') as file:
        parole_dizionario = file.read().splitlines()

    # Legge il file delle password criptate (nome utente, salt, e password criptata)
    with open(file_password, 'r') as file:
        password_entries = file.read().splitlines()

    # La funzione itera su ogni entry nel file delle password. Per ogni entry, estrae il nome utente, il salt, e la password criptata.
    for entry in password_entries:
        username, salt, hashed_password = entry.split(', ')

        # Tentativo di decifrare la password
        #Itera su ogni parola nel dizionario,
        for word in parole_dizionario:
            # Applica l'hash alla combinazione di parola del dizionario e salt
            tentativo_hash = hashlib.sha256((word + salt).encode()).hexdigest()

            # Confronta il tentativo di hash con la password criptata
            if tentativo_hash == hashed_password:
                print(f"Password trovata per l'utente {username}: {word}")
                break #
        else:
            print(f"Password non trovata per l'utente {username} dopo {max_tentativi} tentativi.")

# Esempio di chiamata della funzione
# attacco_dizionario('dizionario.txt', 'passwords.txt')

