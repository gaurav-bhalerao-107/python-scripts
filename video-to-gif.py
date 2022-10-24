## Import movie library using terminal. Type "pip install MoviePy" to do the same.



from moviepy.editor import *

clip = (VideoFileClip("ENTER THE FILE PATH HERE"))
clip.write_gif("output.gif")
