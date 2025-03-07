#esercizio8-10

teams = ["Roma", "Barcellona", "Valencia", "Atletico Madrid"] 
sent_messages=[]

def send_messages():
    while teams:

        message=teams.pop(0)

        print(message)


        sent_messages.append(message)

send_messages()

print("Lista originale:", teams)
print("Messaggi inviati:", sent_messages)