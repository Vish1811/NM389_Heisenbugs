import PIL
import numpy as np
image_frames=[]
days=np.arange(1,24)

for k in days:
    new_frame=PIL.Image.open(r'C:\Users\codev\Desktop\Automate\jpegs'+'\\'+str(k)+'.jpg')
    image_frames.append(new_frame)
    
image_frames[0].save('temperature_timelapse.gif',format='GIF',
                     append_images=image_frames[1:],save_all=True,duration=300,
                     loop=0)