def vowelsCounter(s : str) -> int:
    if not s:
        return 0
    else:
        if s[0].lower() in 'aeiou':
            return 1 + vowelsCounter(s[1:])
        else:
            return vowelsCounter(s[1:])

print(f"La stringa \"\" contiene {vowelsCounter ("")} vocali!")
print(f"La stringa \"Ciao\" contiene {vowelsCounter ("Ciao")} vocali!")
print(f"La stringa \"Pappagallo\" contiene {vowelsCounter ("Pappagallo")} vocali!")
print(f"La stringa \"Ho visto lei che bacia lui\" contiene {vowelsCounter ("Ho visto lei che bacia lui")} vocali!")
