import random
import hashlib #per l'applicazione dell'hash

def imposta_password():
    """
    Questa funzione chiede all'utente di inserire un nome utente e una password,
    genera un salt casuale, applica un hash alla combinazione di password e salt,
    e salva queste informazioni in un file 'passwords.txt'.
    """

    # Chiede all'utente di inserire nome utente e password, utilizziamo l'input standard
    username = input("Inserisci il tuo nome utente: ")
    password = input("Inserisci la tua password: ")

    # Genera un salt casuale utilizzando due caratteri
    salt = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=2))
    #random.choices() sceglie casualmente 2 caratteri da un elenco di lettere maiuscole e minuscole e numeri.

    # Applica l'hash alla combinazione di password e salt
    # Utilizziamo la funzione sha256 per l'hash
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()

    # Salva nome utente, salt e password criptata in un file
    with open("passwords.txt", "a") as file:
        file.write(f"{username}, {salt}, {hashed_password}\n")
        # Il file viene aperto in modalità append ("a"), quindi ogni nuova esecuzione della funzione aggiunge una nuova riga senza sovrascrivere le precedenti.

    print("Password impostata e salvata nel file.")
    #per confermare il salvataggio

# Esegui la funzione
imposta_password()
