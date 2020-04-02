# PlottrOrganizr
An application for managing your plotter files on a neat website. 

## What does this application do? 
This application allows you to view all your designs on a neat website by hosting a local server which queries through your local file system. 

The directory the application is started in is used as the base directory. 
All folders in this directory are searched a `bild.png` / `bild.jp[e]g` file. 
If one of these exists, it is marked as a directory which contains plotter files. 
This means that it is added to a database and therewith displayed on the website. 

If the server starts up correctly, it opens the website on your default web browser. On this webpage there is a list of all
your designs, always with the preview picture (`bild.png`/`bild.jp[e]g`) and the folder name as the title. If you click an
item, this will open the associated folder in the windows explorer. 

The server does automatically generate low-res thumbnails to save bandwidth and offer blazing fast speeds. 

If you add a `notiz.txt` to your folder, the containing text will be displayed below the folder title. 

## Who is this for? 

This application was made for managing plotter design files but could be used by anyone who manages designs. 

## How can I run it? 

Use `pip` to install all dependencies from `requirements.txt`. Then run the `src/server.py`. The `src/index.html`
contains the frontend (made with Vue.js), it is converted to `src/index_shortended.html` by the `src/convert.py` 
to allow pasting directly into the server. 
