def gehaltsrechner():

    arbeits_zeit, frage, lohn_stunde = abfrage()
    monate = berechnung(arbeits_zeit, frage, lohn_stunde)
    steuernabzuege(arbeits_zeit, frage, lohn_stunde, monate)


def abfrage():
    while True:
        lohn_stunde = input("Stundenlohn bitte eingeben: ")
        if lohn_stunde.isnumeric():
            break
    while True:
        arbeits_zeit = input("Wie viele Stunden arbeiten Sie im Monat?: ")
        if arbeits_zeit.isnumeric():
            break
    while True:
        frage = input("""Wenn sie ihr Gehalt im Monat wissen möchten, tippen Sie: -Monat-. 
Falls im Jahr: -Jahr-. 
Wenn beide: -Beide-
> """).lower()
        if frage == "monat" or frage == "jahr" or frage == "beide":
            break
    return arbeits_zeit, frage, lohn_stunde


def berechnung(arbeits_zeit, frage, lohn_stunde):
    monate = 0
    if "monat" in frage:
        gehalt_monat = int(lohn_stunde) * int(arbeits_zeit)
        print(f"Ihr Gehalt im Monat beträgt: {gehalt_monat}€")
    elif "jahr" in frage:
        while True:
            monate = (input("Wie viele Monate im Jahr arbeiten Sie?: "))
            if monate.isnumeric() and 12 >= int(monate) > 0:
                gehalt_jahr = int(lohn_stunde) * int(arbeits_zeit) * int(monate)
                print(f"Ihr Gehalt im Jahr beträgt: {gehalt_jahr}€")
                break
    elif "beide" in frage:
        while True:
            monate = (input("Wie viele Monate im Jahr arbeiten Sie?: "))
            if monate.isnumeric() and 12 >= int(monate) > 0:
                gehalt_monat = int(lohn_stunde) * int(arbeits_zeit)
                gehalt_jahr = int(lohn_stunde) * int(arbeits_zeit) * int(monate)
                print(f"Ihr Gehalt im Monat beträgt: {gehalt_monat}€")
                print(f"Ihr Gehalt im Jahr beträgt: {gehalt_jahr}€")
                break
    return monate


def steuernabzuege(arbeits_zeit, frage, lohn_stunde, monate):
    while True:
        steuern = input("Steuernabzüge berechnen? (Ja/Nein): ").lower()
        if steuern == "nein":
            exit()
        elif steuern == "ja":
            if "monat" in frage:
                nach_steuern = int(lohn_stunde) * int(arbeits_zeit) / 1.19
                print(f"Ihr Gehalt im Monat nach Steuernabzügen beträgt: {round(nach_steuern, 2)}€")
            if "jahr" in frage:
                nach_steuern = int(lohn_stunde) * int(arbeits_zeit) / 1.19 * int(monate)
                print(f"Ihr Gehalt im Jahr nach Steuernabzügen beträgt: {round(nach_steuern, 2)}€")
            if "beide" in frage:
                nach_steuern = int(lohn_stunde) * int(arbeits_zeit) / 1.19
                nach_steuern1 = int(lohn_stunde) * int(arbeits_zeit) / 1.19 * int(monate)
                print(f"Ihr Gehalt im Monat nach Steuernabzügen beträgt: {round(nach_steuern, 2)}€")
                print(f"Ihr Gehalt im Jahr nach Steuernabzügen beträgt: {round(nach_steuern, 2)}€")
        break


if __name__ == "__main__":
    while True:
        print("Gehaltsrechner!")
        gehaltsrechner()

# todo: Das Program nach den Abzügen beenden
