from imposta_password import imposta_password
from attacco_dizionario import attacco_dizionario

# Esegui la funzione imposta_password
imposta_password()
#a scopo illustrativo basta inserire due combinazioni di username e password per passare alla funzione successiva

# Esegui la funzione attacco_dizionario
attacco_dizionario('dizionario.txt', 'passwords.txt')

#dizionario.tzt è stato creato tramite Crunch, un generatore di wordlist basato su pattern specifici (il file è stato generato da un utente sul web, nel caso volessimo creare un set personalizzato può generare tutte le possibili combinazioni di un set di caratteri fornito, sia esso numeri, lettere o simboli, entro una lunghezza minima e massima specificata)
#https://cyber-drops.com/2020/07/17/attacco-a-dizionario/ è il link da cui ho importato il dizionario