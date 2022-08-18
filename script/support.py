from os import walk
import pygame
from settings import resource_path

def import_folder(path, scale=False, size=(64,64)):
    path = resource_path(path)
    surface_list = []
    for _, __, img_file in walk(path):
        for image in img_file:
            full_path = path + '/' + image
            if scale:
                image_surf = pygame.transform.scale(pygame.image.load(full_path).convert_alpha(), size)
            else:
                image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list
