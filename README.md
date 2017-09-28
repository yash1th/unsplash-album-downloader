# Unsplash-Album-Downloader

Using this script you will be able to download the entire album of a user (uploads, likes or collections) or a collection (by specifying Collection - ID)


Dependencies
=======
Make sure you have [Python](https://www.python.org/downloads/) installed and PATH variable set.

Ubuntu
-----
If you don't have ```pip``` for Python:
```
sudo apt-get install python-pip
```
You will need modules ```requests``` installed, which are in ```requirements.txt```
```
pip install -r requirements.txt
```
Windows
-----
Follow [this guide](https://pip.pypa.io/en/stable/installing/) to install  ```pip```  and configure PATH variable.
The rest is the same.

Using script
-----

For downloading User albums, simply run:

```
python download_user_album.py [username]
```

By default, if no flags are passed, the script will download all the ```uploads``` of the user (If any) in a ```full size``` format. To customize the nature of downloads, Please include following flags

```-a``` for the type of album.

For example if you include ```u``` with it as follows

```
python download_user_album.py [username] -a u
```
will download all the photos that has been uploaded by the user. Similarly,

        l - for all the photos liked by the user

        c - for all the collections of the user

        q - for everything related to a user (uploads, likes, collections)


```-m``` for the format of the photo to download

```
python download_user_album.py [username] -a u -m f
```
will download all the photos uploaded by the user in a ```full size``` format. Similarly,

```w``` - raw format

```r``` - regular format

```s``` - small format

```t``` - thumb format

For downloading a particular collection, simply run

```
python download_collection_album.py [collection-id]
```
Please include a ```-c``` flag if it's a curated collection. For example,
```
python download_collection_album.py 160 -c
```
