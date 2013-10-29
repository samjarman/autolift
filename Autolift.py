#!/usr/bin/env python

'''
AutoLift - A tool for downloading images from Interfacelift.Com
Author: Sam Jarman
'''

import unirest
import urllib
import argparse

parser = argparse.ArgumentParser(description='A tool for downloading images from Interfacelift.com')
parser.add_argument('--api-key', required=True, help='Your interfacelift API key (available from interfacelift.com)')
parser.add_argument('--destination', default=".", help='Where to save the images to. (eg /Users/user/Pictures/)')
parser.add_argument('--num-images', default=3, type=int, help='The number of images to fetch (default 3)')
parser.add_argument('--resolution', default='1440x900', help='Resolution of the images (e.g. 1440x900)')
parser.add_argument('--sort-by', default="date", help='How to sort the images')
parser.add_argument('--order', default="desc", help='Which order the images are sorted in')
parser.add_argument('--start', default=0, type=int, help='Which order the images are sorted in')
args = parser.parse_args()
 
def download_individual_callback(response):
  print ("Image downloading with id: " + str(response.body[u'wallpaper_id']))
  path = args.destination + response.body[u'filename']
  print(path)
  f = open(path,'wb')
  f.write(urllib.urlopen(response.body[u'download_url']).read())
  f.close()
  print("Download complete for image with id:" + str(response.body[u'wallpaper_id']))

def download_individual(id):

  response = unirest.get(
    "https://interfacelift-interfacelift-wallpapers.p.mashape.com/v1/wallpaper_download/%d/%s/" % (id, args.resolution),
    {
      "X-Mashape-Authorization": args.api_key
    },
    download_individual_callback
  );


def get_images_callback(response):
  for image in response.body:
    id = image[u'id']
    download_individual(id)
    print("Kicking off download for image with id: " + str(id))


def get_images():

  url = "https://interfacelift-interfacelift-wallpapers.p.mashape.com/v1/wallpapers/?limit=%d&resolution=%s&sort_by=%s&sort_order=%s&start=%d" % (args.num_images, args.resolution, args.sort_by, args.order, args.start)

  response = unirest.get(
    url,
    {
        "X-Mashape-Authorization": args.api_key
    }, 
    get_images_callback
  );


get_images()