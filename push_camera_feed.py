# import pygame.camera
# import pygame.image

# pygame.camera.init()
# cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
# cam.start()
# img = cam.get_image()

# pygame.image.save(img, "/var/www/html/photo.jpg")
# pygame.camera.quit()
# print 'photo_pushed'

import sys
import time
import pygame
import pygame.camera
import pygame.image
from subprocess import call

pygame.init()
pygame.camera.init()

#create fullscreen display 640x480
#screen = pygame.display.set_mode((640,480),0)

#find, open and start low-res camera
cam_list = pygame.camera.list_cameras()
webcam = pygame.camera.Camera(cam_list[0],(32,24))
webcam.start()

while True:
    #grab image, scale and blit to screen
    imagen = webcam.get_image()
    imagen = pygame.transform.scale(imagen,(640,480))
 #   screen.blit(imagen,(0,0))

    #draw all updates to display

  #  pygame.display.update()
    pygame.image.save(imagen, 'photo.jpg')
    print 'photo saved'
#    print call(['whoami'])
#    print call(['cp', 'photo.jpg', '/var/www/html/photo.jpg'])
    call(['cp', 'photo.jpg', '/var/www/html/photo.jpg'])
    time.sleep(1)
    # check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
	        webcam.stop()
        	pygame.quit()
	        sys.exit()