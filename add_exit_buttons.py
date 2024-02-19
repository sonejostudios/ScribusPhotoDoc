#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

try:
    import scribus
except ImportError:
    print("This Python script is written for the Scribus scripting interface.")
    print("It can only be run from within Scribus.")
    sys.exit(1)




def main(argv):

    scribus.setUnit(scribus.UNIT_MILLIMETERS)
      

    # get page size
    pagesize = scribus.getPageSize()

    
###########################################      

    # size and position of the exit buttons    
    linksize = pagesize[0]/30
    linkpos = pagesize[0]-linksize-2

    
    # set up exit to page
    pagenum = scribus.pageCount()
    exittopage = scribus.valueDialog("Exit to page", "Exit buttons should go to page (1-" + str(pagenum)+ ") :" ,"1")
    
    #error
    #if exittopage > pagenum:
    #    scribus.messageBox("Error", "This page doesn't exist.")
    #    sys.exit()

    
    
    # get active layer, create new layer for exit buttons, set it as active
    activelayer = scribus.getActiveLayer()       
    scribus.createLayer("Exitbuttons")
    scribus.setActiveLayer("Exitbuttons")

       

    #progressbar max
    scribus.progressTotal(pagenum)


    # iterate through all the pages    
    page = 1
    while (page <= pagenum):
        
        #messagebar text
        scribus.messagebarText("Create exit buttons...")
        
        scribus.progressSet(page)
        scribus.gotoPage(page)

        # create rectangle
        exitrect = scribus.createRect(linkpos, 2, linksize, linksize, "exitrect"+ str(page))
        scribus.setFillColor("White", exitrect)

        # create text in rectangle    
        exittext = scribus.createText(linkpos, 4, linksize, linksize, "exittext"+ str(page))
        
        scribus.setText("X", exittext)
        scribus.setFontSize(20, exittext)
        scribus.setTextAlignment(1, exittext)
        
        # create link annotation    
        exitlink = scribus.createText(linkpos, 2, linksize, linksize, "exitlink"+ str(page))
        #setLinkAnnotation(page,x,y,["name"])
        scribus.setLinkAnnotation(int(exittopage),0,0,exitlink)

        
        # add page number to iteration        
        page += 1


    # go back to active layer    
    scribus.setActiveLayer(activelayer)


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


