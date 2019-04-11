#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import subprocess

try:
    import scribus
except ImportError, err:
    print "This Python script is written for the Scribus scripting interface."
    print "It can only be run from within Scribus."
    sys.exit(1)




def main(argv):

    scribus.setUnit(scribus.UNIT_MILLIMETERS)
      
    # get page size and page count
    pagesize = scribus.getPageSize()
    pagenum = scribus.pageCount()
    
    
    #create on page
    selectedpage = scribus.valueDialog("Select page", "Create arrows and annotation links on page (1-" + str(pagenum)+ ") :" ,"1")
    
    # get active layer, create new layer for exit buttons, set it as active
    #activelayer = scribus.getActiveLayer()       
    scribus.createLayer("Arrowlinks")
    scribus.setActiveLayer("Arrowlinks")
    
    
    #progressbar max
    scribus.progressTotal(pagenum)

    arrowinitxpos = 10
    arrowinitypos = 30
    
    scribus.gotoPage(int(selectedpage))
    
    page = 1
###########################################      

    for i in range(pagenum):
        # create rectangle
        #exitrect = scribus.createRect(arrowinitxpos, 50, 30, 30, "exitrect")
        
        #messagebar text
        scribus.messagebarText("Creating arrows and annotation links on page " + selectedpage + "...")
    
        
        #progress bar
        scribus.progressSet(page)
        
        #create and distribute arrow
        arrowpoly = [10, 30,  30,10,  50,30,  40,30, 40,50,  20,50,  20,30,  10,30]
        arrowup = scribus.createPolygon(arrowpoly)
        scribus.sizeObject(10, 10, arrowup)
        scribus.moveObjectAbs(arrowinitxpos, arrowinitypos, arrowup)
        scribus.setFillColor("White", arrowup)
        
        
        #create and distribute links  
        arrowlink = scribus.createText(arrowinitxpos, arrowinitypos+11, 10, 10, "link_to_page_" + str(page))
        #setLinkAnnotation(page,x,y,["name"])
        scribus.setLinkAnnotation(int(page),0,0,arrowlink)
        
        arrowinitxpos += 11
        
        if arrowinitxpos > 250:
            arrowinitypos += 24
            arrowinitxpos = 10
        
        # add page number to iteration        
        page += 1




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


