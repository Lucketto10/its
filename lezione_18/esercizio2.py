class InvalidPasswordError(Exception):
    pass

def validate_password(password):
    if len(password) < 20:
        raise InvalidPasswordError("La password deve essere lunga almeno 20 caratteri.")
    
    uppercase_count = 0
    for c in password:
        if c.isupper():
            uppercase_count += 1
    if uppercase_count < 3:
        raise InvalidPasswordError("La password deve contenere almeno 3 lettere maiuscole.")
    
    special_char_count = 0
    for c in password:
        if not c.isalnum():  
            special_char_count += 1
    if special_char_count < 4:
        raise InvalidPasswordError("La password deve contenere almeno 4 caratteri speciali.")
    
    return "La password è valida!"

password = input("Inserisci una password: ")

# Controlliamo se la password è valida
try:
    print(validate_password(password)) 
except InvalidPasswordError as e:
    print(f"Errore: {e}")  
