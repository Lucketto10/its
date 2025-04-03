#esercizi08-13

def build_profile(nome, cognome, età, capelli, peso):
    return f"{nome} {cognome}, età {età}, capelli {capelli}, peso {peso}"

profilo = {"nome" : "Luca", "cognome" : "Taggiasco", "età" : 19, "capelli" : "scuri", "peso" : 73}
profile = build_profile(profilo["nome"], profilo["cognome"], profilo["età"], profilo["capelli"], profilo["peso"])

print(profile)