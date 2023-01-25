[![Build Status](https://travis-ci.org/taikatta/Mileston4-EggSellNT.svg?branch=master)](https://travis-ci.org/taikatta/Mileston4-EggSellNT)


# Egg - Sell - NT

## Table of Contents

1. [Project purpose](#Project-purpose)

2. [UX](#ux)
    - [User stories](#User-stories)
    - [Admin stories](#Admin-stories)

3. [Design and colors](#Design-and-colors)
    
4. [Wireframes](#Wireframes)

5. [Features](#Features)

6. [Technology Used](#Technology-Used)

7. [Testing](#Testing)

8. [DEPLOYMENT](#DEPLOYMENT)

9. [Credits](#Credits)

10. [Disclaimer](#Disclaimer)

[Back to Top](#table-of-contents)

This is my final Milestone Project on the Full Stack Web Developer Code Institute course. For Full Stack Frameworks with Django module.

### Project purpose: 

The purpose of the project is to build a full-stack site based around business logic used to control a centrally-owned dataset.

The site allows users to search eggs by keywords, they can search by farm as well, and after registration/login they can purchase the products.

The project has the following sections:

* Home page  
Contains a background image, clicking anywhere on the background image opens the shop page. The javascript behind it is from [Stackoverflow](https://stackoverflow.com/questions/40749122/open-new-tab-when-user-click-anywhere-on-the-page-only-once).

* Shop page  
Contains all the available products (eggs).

* Farm page  
You can view the farms from where the eggs arrive.

* About Us page  
You can view the employees of Egg-Sell-NT.

* Login / Register page  
Login page with option to register if someone is not a member yet.

* Profile page  
If the user is logged in there is a Profile page, where the user can check their order history.

* Cart  
After a product is added to the cart, the user can view the content of the cart here.

[Back to Top](#table-of-contents)
### UX

#### User stories:

* As a user I would like to be able to view the site on any device I may have, including mobile, tablet, desktop.

* As a user I would like to be able to search to a keyword to find what I need.

* As a user I would like to read more details about a product after clicking on it.

* As a user I would like to be able to find information about my previous orders.

* As a user I would like to search based on which farm the eggs are coming from.

* As a user I would like to be able to contact Egg - Sell - NT with my questions.

* As a user I would like to be able to register on the site.

#### Admin stories:

* As an admin I would like to be able to login to an administration panel

* As an admin I don't want a user to be able to checkout an empty cart

[Back to Top](#table-of-contents)

### Design and colors:

#### Fonts:

I used Noto Sans, from Google Fonts.

On fonts.google.com in the about section the description of the font is the following: When text is rendered by a computer, sometimes there will be characters in the text that can not be displayed, because no font that supports them is available to the computer. Noto helps to make the web more beautiful across platforms for all languages. Currently, Noto covers over 30 scripts, and will cover all of Unicode in the future. This is the Sans Latin, Greek and Cyrillic family. It has Regular, Bold, Italic and Bold Italic styles and is hinted.

Sans-serif is used as the default backup font in case when Nunito Sans was not possible to load.

#### Colors:

* ![#495057](https://placehold.it/15/495057/000000?text=+) #495057 - font color

* ![#F2F4F5](https://placehold.it/15/F2F4F5/000000?text=+) #F2F4F5 - card, media background color

[Back to Top](#table-of-contents)

#### Initial Wireframes:

[Mobile View - Register, Login and Home pages](https://github.com/taikatta/Mileston4-EggSellNT/blob/master/wireframes/initial_design_mobile_register_login_home.png)

[Mobile View - Details and Cart pages](https://github.com/taikatta/Mileston4-EggSellNT/blob/master/wireframes/initial_design_mobile_details_cart.png)

[Mobile View - Shop and About Us pages](https://github.com/taikatta/Mileston4-EggSellNT/blob/master/wireframes/initial_design_mobile_shop_about_us.png)

[Desktop View - Shop, Home and About Us pages](https://github.com/taikatta/Mileston4-EggSellNT/blob/master/wireframes/initial_design_desktop_shop_home_about_us.png)


#### Final Wireframes:

[Mobile View - Farms and Login page](https://github.com/taikatta/Mileston4-EggSellNT/blob/master/wireframes/final_design_mobile_farms_login.png)

[Mobile View - Shop and Home page](https://github.com/taikatta/Mileston4-EggSellNT/blob/master/wireframes/final_design_mobile_shop_home.png)

[Desktop View - Farms and Login page](https://github.com/taikatta/Mileston4-EggSellNT/blob/master/wireframes/final_design_desktop_farms_login.png)

[Desktop View - Shop and Home page](https://github.com/taikatta/Mileston4-EggSellNT/blob/master/wireframes/final_design_desktop_shop_home.png)


[Back to Top](#table-of-contents)


### Features:

#### Open Graph (OG)

I wanted to have a nice photo and text when the link is shared on Messenger, so I added OG meta tags to base.html and used Sharing Debugger (Facebook developer tools) to debug. I made a typo in the title, I had to scrape the URL again.


[Back to Top](#table-of-contents)

### Technology Used:

* Required: HTML, CSS, JavaScript, Python+Django, Postgres, Stripe payments

#### Languages:

* HTML5
* CSS3
* JavaScript
* Python

#### Libraries, frameworks, tools used

* <a href="https://getbootstrap.com/">Bootstrap</a> framework was used for developing a responsive, mobile-first website
* <a href="https://www.djangoproject.com/">Django</a> as python web framework used for rapid development, maintainable, clean design
* <a href="https://jquery.com/">jQuery</a> JavaScript library to simplify HTML DOM manipulation
* <a href="https://fonts.google.com/specimen/Nunito">Google Fonts</a> Used Noto Sans fonts
* <a href="https://fontawesome.com/">FontAwesome</a> as icon provider
* <a href="https://stripe.com/">Stripe</a> made it possible to receive payments for the eggs
* <a href="https://pypi.org/project/psycopg2/">Psycopg2</a> as database adapter for the Python
* <a href="https://gunicorn.org/">Gunicorn</a> or Green Unicorn, a WSGI server implementation used to run Python web application
* <a href="https://code.visualstudio.com/">VSCode</a> was used as a code editor
* <a href="https://git-scm.com/">Git</a> Version control
* <a href="https://github.com">Github</a> Used as a Git repository hosting service
* <a href="https://www.heroku.com/">Heroku</a> Is a container-based cloud Platform, I used Heroku to deploy this app.
* <a href="https://favicon.io/favicon-converter/">Favicon Generator</a> Used to make the right Favicon for the project, I converted the home page background image to a favicon.
* <a href="https://www.canva.com/photos/">Canva photos</a> Used to find the background images.
* <a href="https://validator.w3.org/">W3C Validator</a> Used to check the validity of my HTML and CSS.
* <a href="http://pep8online.com/">PEP 8 Online Validator</a> Used to check my Python code.
* <a href="https://moqups.com">moquaps</a> Used to create wireframes.
* <a href="https://compressjpeg.com/">compressjpg</a> and <a href="https://compresspng.com/">compresspng</a>Used to compress all my images.
* facebook for developers: I used the [Sharing Debugger](https://developers.facebook.com/tools/debug/) to see the information that is used when my website content is shared on Facebook, Messenger and other places.
* <a href="https://travis-ci.org/">Travis CI</a> for continuous integration
* <a href="https://aws.amazon.com/s3/">AWS S3 Bucket</a> as a cloud storage
* <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html">Boto3 </a>to make use of Amazon S3
* <a href="https://python-pillow.org/">Pillow</a> for saving image file formats
* <a href="https://miniwebtool.com/django-secret-key-generator/">miniwebtool</a> for generating new SECRET_KEY
* <a href="https://thispersondoesnotexist.com/">This person does not exist</a> for employee photos


#### Databases

* <a href="https://www.postgresql.org/">PostgreSQL</a> database service provided directly by Heroku
* <a href="https://www.sqlite.org/index.html">SQlite3</a> provided by django

[Back to Top](#table-of-contents)

### Testing

* During the development of the project I carried out testing, I used Google Chrome Developer Tools consistently to check each changes.

* I have tested the site on Google Chrome, Safari and Firefox. And on the following mobile devices: Xiaomi, iPhone11 and iPhone6. And on iPad tablet.

* [Am I Responsive](http://ami.responsivedesign.is/#): Responsive design testing wasn’t working because of the `X-Frame-Options: SAMEORIGIN` security settings.

* Originally when the user clicked on `Add` button next to a product without adding a quantity, nothing happened, as it was considered as 0, quantity needed to be added first. I changed this, because I assumed that it was more user friendly to consider quantity = 1, saving extra clicking for the user.

* The Checkout button is disabled iff there is nothing in the cart.

#### Functionality Test

| Nr | Test          | Action | Before image  | After image  | Test result |
| ---|:-------------:| :----: | :-----:| :-----:| :-----:|
| 1 | Clicking anywhere on home page | Click anywhere  | ![Home page page](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/home_page.png) Home page| ![Shop](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/shop.png) Shop | Passed |
| 2 |  Register | User register | ![Register](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/register.png) Register view | ![Register success](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/register_success.png) Register sucess |  Passed |
| 3 |  Login | User login | ![Login](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/login.png) Login view | ![Login success](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/register_success.png) Login sucess |  Passed |
| 4 |  Profile| Checking Order history | ![Home page](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/lena_home.png) Home Page| ![Profile page](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/lena_profile.png) Profile Page |  Passed |
| 5 |  Using search bar |  Search for blue  | ![Search for blue](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/search.png) Search for blue|![search result](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/search_result.png) Search result|Passed |
| 6 |  Product detail view |  Clicking on More Info  | ![More Info](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/search_result.png) More Info|![More Info result](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/search_more_info.png) More Info result|Passed |
| 7 |  Adding eggs to cart | Adding blue egg to cart | ![Adding egg](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/adding_eggs_to+cart.png) Adding eggs | ![Cart](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/cart.png) Checking cart  |  Passed |
| 8 |  Checkout | Checkout | ![Checkout view](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/checkout.png) Checkout view | ![Paying done](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/checkout_success.png) Paying done |  Passed |
| 9 |  About Us page | Clicking on About Us in Navbar | ![Home page](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/home_page.png) Home page | ![About Us](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/about.png) About Us view |  Passed |
| 10 |  Farms page | Clicking on Farms in Navbar | ![Homa page](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/home_page.png) Home page | ![Farms](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/farms.png) Farm view |  Passed |
| 11 |  Logout | Clicking on Logout | ![Shop](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/shop.png) Shop view| ![Logout success](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/logged_out_success.png) Logout success|  Passed |
| 12 |  Search | Searching for a word that only exists in title | ![Search for pink](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/pink_search.png) Search for pink| ![Search result for pink](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/pink_result.png) Search result for pink|  Passed |
| 13 |  Search | Searching for a word that only exists in description | ![Search for auracana](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/auracana_search.png) Search for auracana| ![Search result for auracana](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/auracana_result.png) Search result for auracana|  Passed |
| 14 |  404 page | Visiting a page that does not exist | ![Search for farm 6](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/search_farm_6.png) Search for farm 6| ![Search result for farm 6](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/404.png) Search result for farm 6|  Passed |
| 15 |  500 page | Server Error | ![Home page](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/home_page.png) Home page| ![Server Error](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/500.png) Server Error|  Passed |
| 16 |  Going to login URL | going to [login url](https://egg-sell-nt.herokuapp.com/accounts/login) | ![As a logged in user](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/home_page.png) As a logged in user| ![As a not logged in user](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/login.png) As not logged in|  Passed |
| 17 |  Going to register URL | going to [register url](https://egg-sell-nt.herokuapp.com/accounts/register) | ![As a logged in user](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/home_page.png) As a logged in user| ![As a not logged in user](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/register.png) As not logged in|  Passed |



#### Browser Compatibility test

| Nr | Browser         | Image  | Test result |
| ---|:-------------:| :---------------: | :-----:|
| 1 | Chrome | ![Chrome](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/chrome.png) Chrome | Passed |
| 2 | Safari | ![Safari](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/safari.png) Safari| Passed |
| 3 | Firefox | ![Firefox](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/firefox.png) Firefox | Passed |



#### Code Validation

* CSS was validated using W3C CSS Validation Service - Jigsaw

* HTML was validated using W3C Markup Validation Service.

* Python code was validated using PEP8 online checker.

#### Defensive design

* Warning messages were used when user entered already taken username at registration, or wrong password/username when signing in.

[Back to Top](#table-of-contents)

### DEPLOYMENT

#### Running Code Locally


1. Follow this link to my [Repository on Github](https://github.com/taikatta/Mileston4-EggSellNT) and open it.

2. Click `Clone or Download`.

3. In the Clone with HTTPs section, click the `copy` icon.

4. In your local IDE open Git Bash.

5. Change the current working directory to where you want the cloned directory to be made.

6. Type `git clone`, and then paste the URL you copied earlier.

7. Press enter and your local clone will be ready.

8. Create and start a new environment:  
python -m .venv venv  
source env/bin/activate

9. Install the project dependencies:  
pip install -r requirements.txt

10. Create a new file, called `env.py` and add your environment variables:

import os  
os.environ.setdefault("STRIPE_PUBLISHABLE", "secret key here")
os.environ.setdefault("STRIPE_SECRET", "secret key here")
os.environ.setdefault("DATABASE_URL", "secret key here")
os.environ.setdefault("SECRET_KEY", "secret key here")
os.environ.setdefault("AWS_ACCESS_KEY_ID", "secret key here")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "secret key here")

11. Go to `settings.py` file and add your environment variables.

12. Add `env.py` to .gitignore file

13. Go to terminal and run the following: `python3 manage.py makemigrations`, then `python3 manage.py migrate` to migrate all existing migrations to postgres database.

14. Create a superuser: `python3 manage.py createsuperuser`

15. Run it with the following command:  
`python manage.py runserver`

16. Open `localhost:8000` on your browser

17.  Add `/admin` to the end of the url address and login with your superuser account and create new products.

#### Deployment to Heroku

The following steps were taken in order to deploy this site to Heroku:

1. Created a new app in `Heroku` with a unique name, chose my region

2. Went to `Resources`, within Add-ons searched `Heroku Postgres`, chose Hobby Dev - Free version, then clicked `Provision` button.

3. In `Settings` clicked on `Reveal Config Vars` button, and copied the value of `DATABASE_URL`

4. Returned to terminal window and run `sudo pip3 install dj_database_url`

5. Also run `sudo pip3 install psycopg2`. Created a requirements.txt file using the terminal command `pip3 freeze > requirements.txt`

6. Went to `settings.py` and added `import dj_database_url` and updated `DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}` also updated `env.py` with `os.environ.setdefault("DATABASE_URL", "postgres://postgres key - copied earlier from Heroku")`

7. I run `python3 manage.py makemigrations`, then `python3 manage.py migrate` to migrate all existing migrations to postgres database.

8. I created a superuser: `python3 manage.py createsuperuser`

9. Logged in to `Amazon AWS`, went to `S3` and created a new `S3` bucket.

10. Returned to terminal window and run `sudo pip3 install django-storages` and `sudo pip3 install boto3`. Went to `settings.py` and added `storages` to `INSTALLED_APPS`.

11. Also in `settings.py` the following lines are added:

AWS_S3_OBJECT_PARAMETERS = {  
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',  
    'CacheControl': 'max-age=94608000'  
}

AWS_STORAGE_BUCKET_NAME = 'egg-sell-nt'  
AWS_S3_REGION_NAME = 'eu-west-1'  
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")  
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")  

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

12. Updated `env.py` with `AWS` keys (these keys are from `S3`).

13. Created `custom_storages.py` at the top level:

from django.conf import settings  
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):  
&nbsp;&nbsp;&nbsp;location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):  
&nbsp;&nbsp;&nbsp;location = settings.MEDIAFILES_LOCATION

14. Went to `settings.py` and added:

STATICFILES_LOCATION = 'static'  
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

MEDIAFILES_LOCATION = 'media'  
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

15. Returned to terminal window and run `python3 manage.py collectstatic`

16. Returned to `Heroku`. In `Settings` clicked on `Reveal Config Vars` button, and added all the following config vars from `env.py`:

| Key         | Value | 
|:-------------:| :----: | 
|  AWS_ACCESS_KEY_ID | secret key here  |
|  AWS_SECRET_ACCESS_KEY | secret key here |
|  DATABASE_URL | secret key here |
|  DISABLE_COLLECTSTATIC| 1 |
|  SECRET_KEY | secret key here |
|  STRIPE_PUBLISHABLE | secret key here |
|  STRIPE_SECRET| secret key here |

17. Clicked to `Deploy`, then `GitHub`, searched for my repository and clicked to `Connect` button.

18. Returned to terminal window and run `sudo pip3 install gunicorn` and added to `requirements.txt`

19. Created a `Procfile` using the following command: `echo web: gunicorn ms4.wsgi:application`

20. Ran `git add .`, `git commit -m "my commit message"` and `git push` commands to push all changes to my GitHub repository.

20. Returned to `Heroku` and hit `Deploy Branch`

21. Once the build is complete, click on `Open app`

22. Went to `settings.py` and added `egg-sell-nt.herokuapp.com` to `ALLOWED_HOSTS`

23. Ran `git add .`, `git commit -m "my commit message"` and `git push` commands to push all changes to my GitHub repository.

24. Returned to `Heroku` and hit `Deploy Branch` again.

### Credits

#### Media

I found the background images and the farm images on Canva photos. All are employees are non existing people, they photos were found on: <a href="https://thispersondoesnotexist.com/">This person does not exist</a>. The images of the eggs were taken by me, using the eggs from our community garden.

#### Acknowledgements

Special thanks to my mentor, Brian Macharia for his time and clear guidance. Thank you for being a good mentor and for guiding me on the right path.

[Back to Top](#table-of-contents)

### Disclaimer

This project was created for educational use only.

[Back to Top](#table-of-contents)
