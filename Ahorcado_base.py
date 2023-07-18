class infoJugador:
    #Crea la informacion basica del jugador
    def __init__(self, nombre = "", palabra = "", pista = ""):
        self.nombre = nombre
        self.palabra = palabra
        self.pista = pista
    
    def __str__(self):
        return(str(self.nombre))

    #Pide el nombre que se usa dentro de crear jugar
    def __pedirNombre(self):
        self.nombre = input("Ingrese el nombre del jugador: ")
        return self.nombre
    
    #Crea la pista
    def __pedirPista(self):
        self.pista = input("Ingrese una pista para su palabra: ")
        return self.pista

    #Pide la palabra, y de inmediatamente su respectiva pista
    def __pedirPalabra(self):
        self.palabra = input("Ingrese su palabra a adivinar: ")
        self.__pedirPista()
        return self.palabra
        
    #Metodo que crea al jugador
    def crearJugador(self):
        print("JUEGO DE AHORCADO")
        self.__pedirNombre()
        self.__pedirPalabra()

class nuevoJuego:
    #datos necesarios para crear una partida
    def __init__(self, adivinar = "", contador = 0):
        self.adivinar = adivinar
        self.contador = contador
        self.palabrasUsadas = []
        pass
    
    #Usa la clase de la informacion del jugador y empieza la partida
    def partida(self):
        juego = infoJugador()
        juego.crearJugador()
        self.intento(juego.palabra)

    #Con recursion se crea un pequeño loop del juego
    def intento(self, palabra):
        #Si self.contador, que esta dentro de la clase nuevoJuego llega a 6 se acaba
        if self.contador >= 6:
            print("PERDISTE!")
        else:
            #Aqui se ven presentes los intentos junto al input de la palabra
            print("Este es tu intento #", self.contador + 1," de 6 intentos")
            self.adivinar = input("Adivinanza: "+ "\n")
            #Si la palabra es igual ganas
            if self.adivinar == palabra:
                print("GANASTE!")
            #Si no es una palabra que hayas usado ya se descuenta un intento
            elif self.adivinar not in self.palabrasUsadas:
                self.contador += 1
                self.palabrasUsadas.append(self.adivinar)
                self.intento(palabra)
            else:
                #Si la palabra esta repetida se vuelve a hacer un intento
                print("Ya uso esa palabra! Vuelva a intentar")
                self.intento(palabra)
    
                
    