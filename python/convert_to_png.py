import os
import sys
import glob
import threading



def convert_to_png(image_file: str):
    """Função para converter a imagem para PNG se ainda não estiver em PNG"""
    if not image_file.endswith('.png'):
        new_image_file = os.path.splitext(image_file)[0] + '.png'
        os.system(f'convert "{image_file}" "{new_image_file}"')
        os.remove(image_file)

def convert_images_to_png(folder: str):
    """Função que converte todas as imagens em uma pasta para PNG em paralelo usando threads"""
    image_files = glob.glob(os.path.join(folder, '*'))
    
    threads = []
    for img in image_files:
        print(img)
        threads.append(threading.Thread(target= lambda : convert_to_png(img)))
    
    [t.start() for t in threads]
    [t.join() for t in threads]


if __name__ == "__main__":
    folder = sys.argv[1]
    convert_images_to_png(folder)