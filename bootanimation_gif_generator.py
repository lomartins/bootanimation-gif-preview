import glob
import imageio

BOOTANIMATION_PATH = "./bootanimation"

class BootAnimationPart:
    def __init__(self, name, repeat, pause, path):
            self.mode = name
            self.repeat = int(repeat)
            self.pause = int(pause)
            self.path = path

desc_txt = open(f'{BOOTANIMATION_PATH}/desc.txt')
desc_width, desc_height, desc_fps = map(lambda x: int(x), desc_txt.readline().split(' '))

parts = []
for line in desc_txt:
    split = line.replace('\n', '').split(' ')
    try:
        parts.append(BootAnimationPart(split[0], split[1], split[2], split[3]))
    except IndexError:
        print("Invalid file desc.txt.")
        quit()


images = []
for part in parts:
    filepath = sorted(glob.glob(f'{BOOTANIMATION_PATH}/{part.path}/*.png'))
    for repeat in range(0, part.repeat+1):
        for file_i in range(len(filepath)):
            images.append(imageio.imread(filepath[file_i]))
            if (file_i == len(filepath)-1):
                for delay in range(0, part.pause):
                    images.append(imageio.imread(filepath[file_i]))


fpsList = [desc_fps]
for fps in fpsList:
    kargs = { 'fps': fps }
    filename = f'bootanimation-{fps}fps.gif'
    imageio.mimsave(filename, images, 'GIF', **kargs)
    print(f'{filename} generated.')
