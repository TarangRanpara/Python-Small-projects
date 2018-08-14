import os
import shutil

'''If you're one of us, who just don't regularly arrangle dowloads folder or any general folder, and one moment when you see it, 
it is just a mess of several GbS and you're too lazy to arrange it.
this is the ultimate solution, it arrangles all your files by extensions.

just provide the folder path, try to use '//' instead of '/' in a path
feel free to make it rich.
'''

def arrange_files():
    
    #file extension
    music_formats = ['.pcm','.wav','.aiff','.mp3','.aac','.ogg','.wma','.au']
    pic_formats = ['.jpg','.jpeg','.png','.bpg','.tiff','.psd','.cpt','.ppm','.pgm','.pbm','.pnm','.exif','.jfif','.ico','.ps','.bmp']
    video_formats = ['.webm','.mkv','.flv','.vob','.ogv','.drc','.gif','.gifv','.mng','.avi','.mov','.qt','.wmv','.yuv','.rm','.rmvb','.asf','.amv','.mp4','.m4p','.3gp','.mpg','.mpeg','.m2v','.m4v','.flv','.f4v','.f4p','.f4a','.f4b']
    doc_formats = ['.doc','.docx','.pdf','.ppt','.pptx','.pptm','.pptm','.txt','.odt','.wpd','.wks','.tex','.rtf','.key','.odp','.pps','.xlsx','.xlsm','.accdb']
    zip_formats = ['.7z','.arj','.deb','.pkg','.rar','.rpm','.zip','.z']
    programming_formats = ['.py','.cpp','.c','.htm','.html','.css','.java','.jar','.php','.asp','.js','.asm','.xhtml','.jsp','.sql','.csv','.xml','.dat','.db','.dbf','.m','.odb']
    executables = ['.exe','.apk','.bin','.dmg','.app']

    #getting path from user
    path = input('Enter path of folder to be arranged:')
    #use '\\' instead of '\' for convenience

    if os.path.exists(path):

        #changing cwd
        os.chdir(path)

        #directory names
        music_dir = 'Music_directory'
        pic_dir = 'Images_directory'
        video_dir = 'Video_directory'
        doc_dir = 'Doc_directory'
        zip_dir = 'Zip_directory'
        prog_dir = 'Programming_directory'
        executables = 'Executable_files'
        others = 'Others'

        #list of folders
        folder_names = [music_dir,pic_dir,video_dir,doc_dir,zip_dir,prog_dir,executables,others]

        #listing files and direcories
        current_files = os.listdir()

         #creating directories if they doesn't exist
        for item in folder_names:
            if item not in current_files:
                os.mkdir(item)

        for item in current_files:

            #if it is directory
            if os.path.isdir(item) and (item not in folder_names):
                shutil.move(item,others)

            #if it is a file
            elif os.path.isfile(item):

                #getting file name and extesion
                f_name, ext = os.path.splitext(item)

                destination = ''

                #deciding destination
                if ext.lower() in music_formats:
                    destination = music_dir

                elif ext.lower() in pic_formats:
                    destination = pic_dir

                elif ext.lower() in video_formats:
                    destination = video_dir

                elif ext.lower() in doc_formats:
                    destination = doc_dir

                elif ext.lower() in zip_formats:
                    destination = zip_dir

                elif ext.lower() in programming_formats:
                    destination = prog_dir

                else:
                    destination = others
                
                #moving a file to destination
                shutil.move(item,destination)
    
    #if file doesn't exist
    else:
        print('path doesn\'t exist')
    
    print('Created by Tarang Ranpara!\n feel free to edit it.')

arrange_files()
