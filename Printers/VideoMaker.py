import os
import shlex
import shutil
from subprocess import check_call
from PngDrawer import PngDrawer


class VideoMaker(object):

    defaultTmpDir = 'tmp'
    defaultVideoParams = {'y':'', 'r':'25','f':'image2',\
        'b':'100000k'}
    defaultEncoder = 'avconv'
    
    def __init__(self, tmpDir=defaultTmpDir,
        encoder=defaultEncoder, videoParams=defaultVideoParams):
        self.tmpDir = tmpDir
        self.videoParams = videoParams
        self.encoder = encoder

    def makeClean(self, animation, fileName):
        
        # Delete tmpDir if it exists
        if os.path.exists(self.tmpDir):
            shutil.rmtree(self.tmpDir)

        # Recreate tmpDir
        os.makedirs(self.tmpDir)

        # Draw animation pngs in tmpDir
        self.drawPngs(animation)

        # Encode video using ffmpeg and params
        self.encodeVideo(fileName, animation)

        # Delete tmpDir
        shutil.rmtree(self.tmpDir)


    def drawPngs(self, animation):
        pngDrawer = PngDrawer(animation)
        pngDrawer.drawAnimationPngs(self.tmpDir)

    def buildCommandLine(self, fileName, frameFormat):
        commandLine = self.encoder
        for param in self.videoParams.keys():
            commandLine = commandLine + " -" + param + \
                " " + self.videoParams[param]
        commandLine = commandLine + " -i " + self.tmpDir + "/%" + \
            frameFormat + ".png " + fileName
        return commandLine

    def encodeVideo(self, fileName, animation):
        paramString = self.buildCommandLine(fileName, animation.frameFormat)
        print paramString
        args = shlex.split(paramString)
        check_call(args)
