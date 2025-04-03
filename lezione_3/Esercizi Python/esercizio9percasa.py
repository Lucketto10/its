def cambia_segno(target: str = "3.14"):
    counter: int = 0
    pi: float = 0.0
    denominatore: int = 1
    segno: int = 1
    while True:

        pi += segno * (4/denominatore)
        segno *= -1
        denominatore+=2

        counter += 1
        if str(pi)[:len(target)] == target:
            print(f"Per raggiungere {target} sono state necessarie {counter} ripetizioni")
            break

        
cambia_segno(target="3.14")    
cambia_segno(target="3.141")
cambia_segno(target="3.1415")
cambia_segno(target="3.14159")