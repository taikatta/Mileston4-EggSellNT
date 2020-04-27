[![Build Status](https://travis-ci.org/taikatta/Mileston4-EggSellNT.svg?branch=master)](https://travis-ci.org/taikatta/Mileston4-EggSellNT)


# Egg - Sell - NT

## Table of Contents

1. [Summary](#Summary)

2. [Project purpose](#Project-purpose)

3. [UX](#ux)
    - [User stories](#User-stories)
    - [Admin stories](#Admin-stories)

4. [Design and colors](#Design-and-colors)
    
5. [Wireframes](#Wireframes)

6. [Features](#Features)

7. [Technology Used](#Technology-Used)

8. [Testing](#Testing)

9. [Credits](#Credits)

10. [DEPLOYMENT](#DEPLOYMENT)

11. [Disclaimer](#Disclaimer)

[Back to Top](#table-of-contents)

### Project purpose: 

The purpose of the project is to build a full-stack site based around business logic used to control a centrally-owned dataset.

The site allows users to search eggs, they can search by farm as well, and after login they can purchase the products.

The project has the following sections:

* Home page
Contains a background image.

* Shop page
Contains all the available eggs.

* Farm page
You can view the farms from where the eggs arrive.

* Contact
Contains our contact details and the names of our employees with pictures.

* Login / Register page
Login page with option to register if someone is not a member yet.

* Cart
After a product is added to the cart, the user can view the containt of the cart here.

[Back to Top](#table-of-contents)
### UX

#### User stories:

* As a user I would like to be able to view the site on any device I may have, including mobile, tablet, desktop.

* As a user I would like to be able to search to find what I need.

* As a user I would like to read more details about a product after clicking on it.

* As a user I would like to be able to find information about my previous order.

* As a user I would like to search based on from which farm the eggs are coming from.

* As a user I would like to be able to contact Egg - Sell - NT with my questions.

* As a user I would like to be able to register on the site.

#### Admin stories:

* As an admin I would like to be able to login to an administration panel.

[Back to Top](#table-of-contents)

### Design and colors:

#### Fonts:

I used Noto Sans, from Google Fonts

On fonts.google.com in the about section the description of the font is the following: When text is rendered by a computer, sometimes there will be characters in the text that can not be displayed, because no font that supports them is available to the computer. Noto helps to make the web more beautiful across platforms for all languages. Currently, Noto covers over 30 scripts, and will cover all of Unicode in the future. This is the Sans Latin, Greek and Cyrillic family. It has Regular, Bold, Italic and Bold Italic styles and is hinted.

Sans-serif is used as the default backup font in case when Nunito Sans was not possible to load.

#### Colors:





[Back to Top](#table-of-contents)

#### Initial Wireframes:

Originally on the home page I wanted to have one background picture and 3 of our latest donated books, but then I discovered Parallax (Materialize). Parallax is an effect where the background image is moved at a different speed than the foreground content while scrolling, so I decided to use Parallax instead.

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

I wanted to have a nice photo and text when the link is shared on Messenger, so I added OG meta tags to base.html and used Sharing Debugger (Facebook developer tools) to debug. I made a typo in the title, I had to fix it. 


#### Features Left to Implement:

[Back to Top](#table-of-contents)

### Technology Used:

* Required: HTML, CSS, JavaScript, Python+Django, Postgres, Stripe payments

#### Languages, Frameworks, Editors & Version Control:

* HTML5
* CSS3
* JavaScript
* Python
* Bootstrap
* Django
* jQuery
* VSCode: Was used as a code editor.
* Git: Version control.
* <a href="https://github.com">Github</a> Used as a Git repository hosting service
* <a href="https://www.heroku.com/">Heroku</a> Is a container-based cloud Platform, I used Heroku to deploy this app.

#### Tools Used:

* Django
* <a href="https://fonts.google.com/specimen/Nunito">Google Fonts</a> Used Nunito Sans fonts
* <a href="https://favicon.io/favicon-converter/">Favicon Generator</a> Used to make the right Favicon for the project, I converted the home page background image to a favicon.
* <a href="https://www.canva.com/photos/">Canva photos</a> Used to find the background images.
* <a href="https://validator.w3.org/">W3C Validator</a> Used to check the validity of my HTML and CSS.
* <a href="http://pep8online.com/">PEP 8 Online Validator</a> Used to check my Python code.
* <a href="https://moqups.com">moquaps</a> Used to create wireframes.
* facebook for developers: I used the [Sharing Debugger](https://developers.facebook.com/tools/debug/) to see the information that is used when my website content is shared on Facebook, Messenger and other places.

[Back to Top](#table-of-contents)

### Testing

During the development of the project I carries out testing. 

#### Functionality Test

| Nr | Test          | Action | Before image  | After image  | Test result |
| ---|:-------------:| :----: | :-----:| :-----:| :-----:|
| 1 | Clicking anywhere on home page | Click anywhere  | ![Home page page](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/home_page.png) Home page| ![Shop](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/shop.png) Shop | Passed |
| 2 |  Using search bar |  Search for blue  | ![Search for blue](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/search.png) Search for blue|![search result](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/search_result.png) Search result|Passed |
| 3 |  Adding eggs to cart | Adding blue egg to cart | ![Adding egg](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/adding_eggs_to+cart.png) Adding eggs | ![Cart](https://egg-sell-nt.s3-eu-west-1.amazonaws.com/media/photos/test/cart.png) Checking cart  |  Passed |


#### Code Validation

* CSS was validated using W3C CSS Validation Service - Jigsaw

* HTML was validated using W3C Markup Validation Service.

* Python code was validated using PEP8 online checker.

#### Defensive design

* Warning messages were used when user entered already taken username at registration, or wrong password/username when signing in.

[Back to Top](#table-of-contents)

### Credits

#### Acknowledgements

[Back to Top](#table-of-contents)

### DEPLOYMENT

### Disclaimer

This project was created for educational use only.

[Back to Top](#table-of-contents)





https://miniwebtool.com/django-secret-key-generator/



I attended Python django dev to deployment course by Brad Traversyon on Udemy, I used his solution for message alert.
https://www.udemy.com/course/python-django-dev-to-deployment/


W3C errors:
 The value of the for attribute of the label element must be the ID of a non-hidden form control.