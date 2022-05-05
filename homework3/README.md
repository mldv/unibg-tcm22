# Homework 3

## Consegna

Continuare con l'implementazione del sistema, aggiungendo le funzionalità che servono per ottenere il seguente comportamento.
Utente A è il gestore di una gara, colui che carica i risultati.
Utente B è il gestore di un'altra gara.
Utente C vuole visualizzare i risultati.

1. Utente A fa una chiamata POST all'endpoint `/register_race` fornendo in input (almeno) i seguenti dati: 
    - `race_name`: nome della gara
    - `race_date`: la data di svolgimento
    - `email`: la propria email.

    È possibile prevedere di aggiungere altri dati (es. il luogo di svolgimento).
    
    In futuro ci sarà probabilmente un form HTML che Utente A compilerà, per ora è sufficiente creare solo il backend.

    Utente A riceve come risposta un `race_id`, univoco per la gara nel sistema, e un `token` che userà come segreto per fare l'upload dei risultati.
    In futuro si potrebbe voler mandare questi dati via mail.

2. Utente A carica i risultati parziali utilizzando l'endpoint `/uploadxml` (POST) con il `token`. Il body della richiesta contiene l'XML in formato standard. Utente A carica diverse volte i risultati parziali, aggiornandoli.

3. Utente B registra una gara (diversa da quella di utente A).

4. ***(BONUS)*** Utente B prova a caricare dei risultati ma l'XML non rispetta lo standard. Il sistema restituisce un errore. Successivamente carica i risultati in formato corretto.

5. Utente C vuole vedere quali eventi sono disponibili nel sistema: fa una chiamata GET a `/list_races` e ottiene una lista JSON degli eventi, ciascun evento è un dizionario con (almeno) race_name, race_date, race_id.

6. Utente C ottiene l'elenco delle categorie presenti all'evento X con una chiamata GET a `/list_classes?id=X`

7. Utente C ottiene la classifica attuale della categoria Y dell'evento X con una chiamata GET a `/results?id=X&class=Y`. 
La classifica deve essere quella indicata nell'upload più recente di Utente A. 
Utilizzare un formato di risposta ritenuto appropriato e spiegare il motivo.

8. Utente B ottiene il file XML dei risultati della gara di Utente A, con una chiamata GET a `/downloadxml?id=X`.

9. ***(BONUS)*** Utente C ottiene l'elenco di tutti gli atleti che rappresentano il club Z all'evento X con una chiamata GET a `/results?id=X&organisation=Z`.

    Il nome del club corrisponde al campo `PersonResult/Organisation/Name` nell'XML.