# __CatAI__

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvalleyeyecareaz.com%2Fwp-content%2Fuploads%2F2019%2F05%2Fbigstock-Cataract-concept-Senior-woman-175059088.jpg&f=1&nofb=1" width="200" height="145" />

## __CatAI__ is a program designed to detect cataracts
### Designed in 2021 for the _WAICY_ Competition 2021, I (Richard Barlian, age 11) created a program to detect cataracts. Cataracts has always been a problem in our community; my grandfather, grandmother, and lots of, particularly elderly people in our community, have been diagnosed with it. I used a CNN to create an Image Classifier, trained with data from people with Cataracts, and those who didn't.
---
## Instructions
### Instructions for setup
* To run this program, you need to use Python 3.7.
* The code is developed and tested under Python 3.7.0 (https://www.python.org/ftp/python/3.7.0/python-3.7.0-amd64.exe)
* After that, you need to install the necessary modules (modules are found in `requirements.txt` - you can install using this command `pip install -r requirements.txt`)
* If you have a __CUDA__ enabled GPU, you may have to use tensorflow-directml

### Instructions for running
* `cd` into the `.\program\` directory</li>
* Run `python main.py`
* Click `Detect`
* It will ask you to find your file, keep in mind that it should be a `jpg` image
* If you want to take a photo of your eyes, please take a picture of only one, without any accessories such as contact lenses or glasses, and use a higher resolution camera
* There are also images in `program\sample_images` if you want to use a sample image
* Wait for a few seconds (it may take a bit long, depending on your device)
* It will show the image with the diagnosis
----
## Disclaimer:
* This project is not in any way supposed to be an alternative to medical advice.
* This is not meant to be used as a replacement to medical advice, but as an extension.
* The purpose of this project is only to detect cataracts in its early stages, so you can seek medical advice sooner.