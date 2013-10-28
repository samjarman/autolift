#!/usr/bin/env python

'''
AutoLift - A tool for downloading images from Interfacelift.Com
Author: Sam Jarman
'''

import unirest
import urllib

##Fill these in

save_directory = "" #Where you would like to save the images
num_images = 3 #The number of images you would like to get
api_key = "" #Your API key from https://www.mashape.com/interfacelift/
resolution = "" #The resolution of the image you'd like eg '1440x900'
sort_by = "date"  #How to sort the images
sort_order = "desc" #The order by which they are sorted
start = 0  #The number of objects to skip over in the result set. Pair this parameter with 'limit' in order to implement paging of results.



def download_individual_callback(response):
	print ("Image downloading with id: " + str(response.body[u'wallpaper_id']))
	f = open(save_directory + response.body[u'filename'],'wb')
	f.write(urllib.urlopen(response.body[u'download_url']).read())
	f.close()
	print("Download complete for image with id:" + str(response.body[u'wallpaper_id']))

def download_individual(id):

	response = unirest.get(
		"https://interfacelift-interfacelift-wallpapers.p.mashape.com/v1/wallpaper_download/%d/%s/" % (id, resolution),
		{
			"X-Mashape-Authorization": api_key
		},
		download_individual_callback
	);


def get_images_callback(response):
	for image in response.body:
		id = image[u'id']
		download_individual(id)
		print("Kicking off download for image with id: " + str(id))


def get_images():

	url = "https://interfacelift-interfacelift-wallpapers.p.mashape.com/v1/wallpapers/?limit=%d&resolution=%s&sort_by=%s&sort_order=%s&start=%d" % (num_images, resolution, sort_by, sort_order, start)

	response = unirest.get(
		url,
		{
   			"X-Mashape-Authorization": api_key
		}, 
	 	get_images_callback
	);


get_images()