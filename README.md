# ScribusPhotoDoc
A collection of scripts for Scribus to create navigable PDF photo documentations.



![screenshot](https://raw.githubusercontent.com/sonejostudios/ScribusPhotoDoc/master/PhotoDoc.jpg "ScribusPhotoDoc")


__Description:__

This is a collection of python scripts for Scribus to build navigable PDF photo documentations.
Use case: You took a lot of pictures from a building and objects in that building. Having a lot of pictures is nice, but quite useless without the information about the position and direction. And maybe you want to add even more information to the pictures, highlight or link objetcs, add descriptions, names, etc...
This collection of scripts may be a solution for this. They import all the pictures of a specific folder into a new scribus project (one picture / page) and create basic navigation buttons for the PDF file.
After exporting, you get a PDF file in which you can navigate between the pictures by clicking on the different items and arrows.
Of course, this can be used not only for maps and buildings, but also for any kind of photo documentation, e.g. for objects, details, whatever...


__Scripts:__

ScribusPhotoDoc is made of 3 (+1 Main) python scripts:

1. __import_all_images.py__ : This script creates a new project and import all images of choosen folder into scribus pages (on the "Background" layer). If wanted, it can add the file names of the pictures to each page on a "Filenames" layer.

2. __add_exit_buttons.py__ : This script creates an "exit button" on each page, allowing to navigate back to a specific page (default = page 1). All exit buttons are placed in a new layer called "Exitbuttons".

3. __add_arrows_and_links.py__ : This script adds as many arrows and annotation links as pages to a specific page (default = page 1). All arrows and annotation links are placed in a new layer called "Arrowlinks". Each link is named to its linked page, e.g. "link_to_page_7".

4. __Full_PhotoDoc.py__ : This is the main script. It just starts each of the previous script in the right order. Start this script for a full PhotoDoc experience! :)


Each script is a whole Scribus script, which can be used separately.



__Instalation:__

Download the .zip file and unzip it where you want, if you have a Scribus Script folder, unzip it there!



__Usage (Starting):__

1. Prepare your working directory: Create a new folder and put all the pictures you want for the documentation inside this folder. Be sure you have only one picture for each "view" or "object"! If not, remove all unneeded pictures.

2. Change the filenames of the pictures, so they are in the order you want (e.g. put the map of the building as first file by adding 00_ to the filename as prefix).

3. Start Scribus (you don't need to create a new project, so cancel the new project dialog).

4. In Menu "Scripter", "Execute Script", choose Full_PhotoDoc.py. This will start the full PhotoDoc Wizard script (see below). If used once, you will find it also under "Recent Scripts".



__Usage (PhotoDoc Wizard):__

1. A new Document Dialog will pop up. Make the adjustments you want for your project. I recommand Single Page, Format = Letter, Orientation = Landscape, Bleed = 0. Leave "Number of pages" to 1. Press OK.

2. A folder chooser dialog will pop up. Choose your working directory with the pictures you prepared before. Press OK.

3. A file filter Dialog will pop up. If you want to filter some image extensions or names, change the value, otherwise leave "*.*" Caustion: This filter is case sensitive! Press OK.

4. An import images dialog will pop up with the amount of (filtered) images found. If you want to add the file names to the images, press Yes. If you want to leave the images without filenames, press No. Scribus will import all the images into the project and add filenames if wanted. Depending on the amount of images, this can take some time.

5. An exit page dialog will pop up. Choose the destination page for the exit buttons (default = page 1). Usually, it should be the page with the general map. Press OK. Scribus will create an exit button on each page. Depending on the amount of images, this can take some time.

6. An select page dialog for arrows and links creation is poping up. Choose the destination page for the arrows and links (default = page 1). Usually, it should be the page with the general map. Press OK. Scribus will create of each page an arrow an a link on the selected page. Depending on the amount of images, this can take some time.

7. If the done dialog is poping up, everything is set up up correctly! Spread your arrows and links and export your project to a PDF File.



__Layers:__

When the script is done, the following layers have been created:
- Arrowlinks: a layer with the arrows and the annotation links to the pages
- Exitbuttons: a layer with the exit buttons
- Filenames:  a layer with the file names of the images (if wanted)
- Background : a layer with the images
    


__Tips:__

- Show layers in Scribus: Menu/Windows/Layers or F6
- Rotate object (e.g. arrows): R (do not rotate the links!)
- Show object properties: Menu/Windows/Properties or F2
- In the properties, you can rotate and resize the images (select the "Background" layer first)
- The object name of a link shows the destination page, e.g. "link_to_page_7"
- Try to put also arrows and links into the images to navigate directly
- Reduce the size of your pictures before starting PhotoDoc to speed up the process and reduce the PDF file size
- Use the power of Scribus to enhance the documentation with textes, arrows, weblinks...
- If you need to reproduce a step, delete the step layer and restart step script, e.g. "add_exit_buttons.py"
- Export a PDF with 96 dpi as image resolution to reduce the PDF file size



