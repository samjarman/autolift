# Autolift

This tool lets you download as many images as you like from [interfacelift.com](http://interfacelift.com).

## Installation

You'll need [an API key from interfacelift](https://www.mashape.com/interfacelift/wallpapers/pricing). Heads up, they charge.

You'll also need the unirest library. You can install it with [pip](http://www.pip-installer.org/):

    $ pip install unirest

## Usage

Edit `Autolift.py`. Modify the parameters at the top of the file, save and run with:

    $ ./Autolift.py --api-key YOUR_API_KEY

Full usage:

    usage: Autolift.py [-h] --api-key API_KEY [--destination DESTINATION]
                       [--num-images NUM_IMAGES] [--resolution RESOLUTION]
                       [--sort-by SORT_BY] [--order ORDER] [--start START]

    A tool for downloading images from Interfacelift.Com

    optional arguments:
      -h, --help            show this help message and exit
      --api-key API_KEY     Your interfacelift API key (available from
                            interfacelift.com)
      --destination DESTINATION
                            Where to save the images to
      --num-images NUM_IMAGES
                            The number of images to fetch (default 3)
      --resolution RESOLUTION
                            Resolution of the images (e.g. 1440x900)
      --sort-by SORT_BY     How to sort the images
      --order ORDER         Which order the images are sorted in
      --start START         Which order the images are sorted in