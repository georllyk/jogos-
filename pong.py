importar pygame
Sistema Isport

# Inicializar o Pygame
pygame.init()

# Dimensões da tela

largura = 800 
altura = 400
tela = pygame.display.set_mode((largura, altura)) 
pygame.display.set_caption('Pong')


#Cores 

branco = (255, 255, 255)
preto = ((0, 0, 0)
azul = (0, 128, 255) 
verde = (0, 255, 0)
amarelo = (255, 255, 0)

#Fosições e tamannos das raquetes e bola

raquete_largura = 10
raquete_altura = 100
raquete_esquerda = y altura //2 - raquete altura // 2 raquete altura // 2
raquete_direita_y = altura //2 
bola_dx,  bola_y =  largura // 2, altura // 2
bola_dx, bola_dy = 5, 5

#Principal do loop
while True:
   # Processa eventos
 for evento in  pygame.event.get():
   if evento.type == Pygame.QUIT:
  pygame.quit() 
  sys.exit()

#Movimenta raquetes
 teclas =  pygame.key.get_pressed()
  if teclas [pygame.К_w):
  raquete_esquerda_y -= velocidade_raquete
 if teclas[pygame.K_s]:
