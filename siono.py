def si_o_no(pregunta):
    respuesta = input(pregunta + "(s/n): ").lower().strip()
    print("")
    while not(respuesta == "s" or respuesta == "si" or respuesta == "n" or respuesta == "no"):
        print("Por favor ingresa si ó no")
        respuesta = input(pregunta + "(s/n):").lower().strip()
        print("")
    if respuesta[0] == "s":
        return True
    else:
        return False