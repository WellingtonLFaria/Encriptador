# Importando biblioteca
from encriptador import Encriptador

# Instanciando o Encriptador
encriptador = Encriptador(2)

# Mensagem a ser encriptada
msg = "Hello World"

# Encriptando mensagem
msg_encriptada = encriptador.encriptar(msg)

# Decriptando a mensagem
msg_decriptada = encriptador.decriptar(msg_encriptada)

print(msg_encriptada, msg_decriptada)