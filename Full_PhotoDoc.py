#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import subprocess

import import_all_images
import add_exit_buttons
import add_arrows_and_links


try:
    import scribus
except ImportError, err:
    print "This Python script is written for the Scribus scripting interface."
    print "It can only be run from within Scribus."
    sys.exit(1)




def main(argv):
    
    
##########################################   

    # 1.import all images
    import_all_images.main_wrapper(sys.argv)
    
    # 2.add exit buttons
    add_exit_buttons.main_wrapper(sys.argv)
    
    # 3.add arrows and links
    add_arrows_and_links.main_wrapper(sys.argv)
    
    # done
    pagenum = scribus.pageCount()
    donetext = """
The photo documentation is ready!

Page(s): """ + str(pagenum) + """
    
The following layers have been created:
    - Arrowlinks: a layer with the arrows and the annotation links to the pages
    - Exitbuttons: a layer with the exit buttons
    - Filenames:  a layer with the file names of the images (if wanted)
    - Background : a layer with the images
    
Tips:
    - Show layers in Scribus: Menu/Windows/Layers or F6
    - Rotate object (e.g. arrows): R (do not rotate the links!)
    - Show object properties: Menu/Windows/Properties or F2
    - In the properties, you can rotate and resize the images (select the "Background" layer first)
    - The object name of a link shows the destination page, e.g. "link_to_page_7"
    - Reduce the size of your pictures before starting PhotoDoc to speed up the process and reduce the PDF file size
    - Try to put also arrows and links into the images to navigate directly
    - Use the power of Scribus to enhance the documentation with textes, arrows, weblinks...
    - Export a PDF with 96 dpi as image resolution to reduce the PDF file size
"""
    scribus.messageBox("PhotoDoc", donetext)


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


