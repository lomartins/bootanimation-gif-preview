import glob
import imageio

BOOTANIMATION_PATH = "./bootanimation"
INFINITE_LOOP_LIMIT = 3

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
        if len(split) > 1:
            parts.append(BootAnimationPart(split[0], split[1], split[2], split[3]))
    except IndexError:
        print("Invalid file desc.txt.")
        quit()


images = []
for part in parts:
    files = sorted(glob.glob(f'{BOOTANIMATION_PATH}/{part.path}/*.png'))
    if part.repeat != 0:
        part_repeat = part.repeat
    else:
        part_repeat = INFINITE_LOOP_LIMIT

    for repeat in range(0, part_repeat+1):
        for file_i in range(len(files)):
            images.append(imageio.imread(files[file_i]))
            if (file_i == len(files)-1):
                for delay in range(0, part.pause):
                    images.append(imageio.imread(files[file_i]))


fpsList = [desc_fps]
for fps in fpsList:
    kargs = { 'fps': fps }
    filename = f'bootanimation-{fps}fps.gif'
    imageio.mimsave(filename, images, 'GIF', **kargs)
    print(f'{filename} generated.')
