import os

def getdirs(path):
    

    """
    List of extensions we want to find in the paths, I've gone with a 
    github repo to help me with this part:

    https://github.com/dyne/file-extension-list

    """

    extensions = [
        'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw', # images
        'mp3','mp4', 'm4a', 'aac','ogg','flac', 'wav', 'wma' # music and sound
        'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp', # Video and movies
        'doc', 'docx', 'xls', 'xlsx', 'ppt','pptx', 'txt' # Productivity 
    ]

    for DirectoryPaths, Directories, files in os.walk(path):
        for i in files:
            absPath = os.path.abspath(os.path.join(DirectoryPaths, i))
            getExts = absPath.split('.')[-1] # so we get the actual extension path
            if getExts in extensions:
                print(absPath)
                yield absPath