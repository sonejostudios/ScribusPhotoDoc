#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import glob
import os

try:
    import scribus
except ImportError:
    print("This Python script is written for the Scribus scripting interface.")
    print("It can only be run from within Scribus.")
    sys.exit(1)




def main(argv):

    
###########################################      

    scribus.newDocDialog()

    
    if scribus.haveDoc:
        scribus.setUnit(scribus.UNIT_MILLIMETERS)                                       
        (w,h) = scribus.getPageSize() 

        ###################
        
        # ask for workdir
        workdir = scribus.fileDialog("Open directory with images", "", haspreview=False, issave=False, isdir=True)
        #workdir = "/media/sda7/StudioSession3/PDFTools/pics"
        
        # file filter
        filefilter = scribus.valueDialog("File filter", "File filter examples: \n\n* or *.* = add all files\n*.jpg = add .jpg files only\nIMG_*.* = add all files starting with IMG_\n\nThis filter is case sensitive!","*.*")

        # get image paths 
        filelist = sorted(glob.glob(os.path.join(workdir,filefilter)))
        #scribus.messageBox("Help", str(filelist))
        
        # count files
        filesinworkdir = len(filelist)
        #scribus.messageBox("Help", str(filesinworkdir))
        
        #messagebar text
        scribus.messagebarText("Importing images...")
        
        #error
        if filesinworkdir == 0:
            scribus.messageBox("Error", "This directory is empty.")
            sys.exit()
        
        # add filename text?
        addfilenames = scribus.messageBox("Import images", "Files found in workdir : " + str(filesinworkdir) + "\n\nAdd file names to images?", button1=scribus.BUTTON_YES, button2=scribus.BUTTON_NO)
    
        #create text layer
        if addfilenames == 16384:
            activelayer = scribus.getActiveLayer()
            scribus.createLayer("Filenames")
            scribus.setActiveLayer(activelayer) 

        #progressbar max
        scribus.progressTotal(filesinworkdir)
        
        page = 1
        
        #create page, add and load image
        for i in filelist:
            scribus.progressSet(page)
            
            scribus.gotoPage(page)
            scribus.createImage(0, 0, w, h, "imagename"+str(page))
            scribus.loadImage(filelist[page-1], "imagename"+str(page))
            scribus.setScaleImageToFrame(True, proportional=True, name="imagename"+str(page))
            #scribus.setImageOffset(0, 0, "imagename"+str(page))
            #scribus.setScaleFrameToImage(name="imagename"+str(page))
            
            
            # add filename on page?
            if addfilenames == 16384:
                scribus.setActiveLayer("Filenames")
                filename = scribus.createText(2, 2, 50, 10, filelist[page-1])
                scribus.setText(os.path.basename(filelist[page-1]), filename)
                scribus.setTextColor("White", filename)
                scribus.setActiveLayer(activelayer)  
            
            scribus.newPage(-1)
            page += 1
            
            
        #delete last blank page
        scribus.deletePage(filesinworkdir+1)

            
    


##########################################   


def main_wrapper(argv):
    try:
        scribus.statusMessage("Running script...")
        scribus.progressReset()
        main(argv)
    finally:
        # Exit neatly even if the script terminated with an exception,
        # so we leave the progress bar and status bar blank and make sure
        # drawing is enabled.
        if scribus.haveDoc():
            scribus.setRedraw(True)
        scribus.statusMessage("")
        scribus.progressReset()


# This code detects if the script is being run as a script, or imported as a module.
# It only runs main() if being run as a script. This permits you to import your script
# and control it manually for debugging.
if __name__ == '__main__':
    main_wrapper(sys.argv)


