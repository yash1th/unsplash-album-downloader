# Unsplash Public Album Downloader

Using this script you will be able to download the entire album of a user (uploads, likes or collections) or a just collection (by specifying Collection-ID) in any size you like.


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

Before running the script, please assign a **Application ID** to **APP_ID** variable in the python script **download_user_album.py**. If you do not have one, you can create [here](https://unsplash.com/documentation#creating-a-developer-account). For downloading user albums, simply run:

```
python download_user_album.py [username] [albumtype] [size]
```

By default, if no flags are passed, the script will download all the ```uploads``` of the user (If any) in a ```regular``` size. To customize the nature of downloads, Please include following flags


```albumtype```  takes the following values -

* ```uploads``` to download all the photos uploaded by user

* ```likes``` to download all the photos liked by user

* ```collections``` to download all the collections of a user

* ```all``` to download all of the above *uploads*, *likes*, *collections*


```size``` takes the following values -

* ```raw``` to download the raw size

* ```full``` to download the full size

* ```regular``` to download the full size

* ```small``` to download the full size

* ```thumb``` to download the full size

Example :
-----

```
python download_user_album.py likes small
```
downloads all photos liked by user in small size.

For downloading a particular collection, simply run

```
python download_collection_album.py [collection-id] [curated flag] [size]
```

* ```collection-id``` is the id of the collection

* ```size``` is similar to above and takes the same values

Please include a ```-c``` flag when it's a curated collection you are trying to download. For example,
```
python download_collection_album.py 160 -c full
```
downloads the collection with id #160 (which is a curated collection) in a full size. So, we have to include the ```-c``` flag.

app_id text file
-------

You can also include the application ID in **app_id.txt** file. Make sure the file is in the same location as the above scripts.

Downloaded files
-----

All the photos will be downloaded in a separate folder with the name of the user and the type of download you requested.

#### Example folder names:

* yaswanth amara-unsplash-likes-full

* Jakob Owens-unsplash-collection-Behind The Scenes-regular

Since there is a API limit for a public access application for Unsplash (50 requests per hour), if you are trying to download a large number of photos, you might want to run the same command again once you are out of requests. The above scripts will check the folder for the photos that were already downloaded and then will download **ONLY** the remaining photos.

Thanks
-----
This program would not be possible without **UNSPLASH** and their awesome photographers.

**I sincerely appreciate if you give necessary credit to the Photographers and Unsplash whenever you use their photos.**
