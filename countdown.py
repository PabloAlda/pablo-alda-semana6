print("Tienes 10 segundos para desactivar la BOMBA, tienes que cortar el cable correcto. Hay 5 cables de diferentes colores, uno de elllos desactiva la bomba y el otro la explota automáticamente. Los colores de los cables son rojo, verde, amarillo, azul y negro.")
number = 10
hasPaintedPoints = False
while number >=0:
    userInput = input("¿Que cable corto?")
    if userInput == 'rojo':
        print("HAS DESACTIVADO LA BOMBA, HAS CONSEGUIDO SOBREVIVR.")
        break
    if userInput == 'verde':
        print("LA BOMBA HA EXPLOTADO, HAS MUERTO.")
        break

    if (number < 8 and number > 2):
        if not  hasPaintedPoints:
            print('...')
            hasPaintedPoints = True
            number = 3
            number -= 1
        continue
    print(number)
    number -=1
    if number <= 0:
        print("LA BOMBA HA EXPLOTADO, HAS MUERTO.")

