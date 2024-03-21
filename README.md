# StaticSiteGenerator
This is the second guided project from [boot.dev](https://www.boot.dev/)

Static Site Generator builds and hosts a webserver. Core site functionality like CSS stylesheets, images and so on should be placed in the **static** folder.

Content is generated from markdown files placed in the **content** folder.

Main.py purges existing public folder before copying data from static and generating html files from the content folder.

## How to run
Run *main.bat* or *main.sh* These files will kick off the process of generating the site and once complete start a webserver on localhost port 8888