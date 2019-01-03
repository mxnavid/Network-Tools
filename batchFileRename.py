"""
This will rename all files in a given directory.
For test purpose, its removing different types of character from
a given mp4 files.
"""

import os

def main(dir):
    startRemoving = ".20"
    
    
    for videos in os.listdir(dir):
        src = dir + '/' + videos
        dst = videos.split(startRemoving,1)[0]
        dst = dst.replace(".", "_")
        dst = dst.replace(":", "_")
        dst = dst.replace("'","")
        dst = dir + '/'+ dst + '.mp4'

        print(dst)
        os.rename(src, dst)

# put the Directory path in this parameter
if __name__ == "__main__":
    main('DIRECTORY_PATH')

#TODO Someday I will make a seperate repo with non-networking tools