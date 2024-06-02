# PP4: Pure Drive Fitness

![Site Home Page](https://puredrivefitness-68f4e5eedb4f.herokuapp.com/)

**Developer: Andrew Pierce**

💻 [Visit live website](https://puredrivefitness-68f4e5eedb4f.herokuapp.com/)  
(Ctrl + click to open in new tab)

## Table of Contents
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
  - [Design](#design)
    - [Colors](#colors)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
      - [Models](#models)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Automated testing](#automated-testing)
    - [Tests on various devices](#tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

<hr> 

## User Stories

### User

#### Sessions

1. As a **user** I can **see the session types on the welcome page** so that I can **see headline information about the sessions**
2. As a **user** I can **read detail about the session types that are available** so that **I understand what is best for me**
3. As a **user** I can **book a session** so that I can **begin my training**
4. As a **user** I can **view my booked sessions** so that I can **cancel if i need to**
5. As a **user** I can **leave a comment as I book** so that I can **inform the trainer about my requirements**
6. As a **user** I can **receive booking emails** so that I can **get confirmation that it has been booked**

#### Blog

7. As a **user** I can **view all of the available blogs in a clear and simple layout** so that I can **find a blog a would like to read**
8. As a **user** I can **see a short excerpt from the blog** so that I can **understand what it is about**
9. As a **user** I can **read the blog** so that I can **learn about the subject**
10. As a **user** I can **like a blog** so that I can **give positive feedback on posts I enjoyed**
11. As a **user** I can **comment on a blog** so that **ask questions or leave useful informtation for other users**

#### General

12. As a **user** I can **easily navigate the website** so that I can **find the information I am looking for**
13. As a **user** I can **log in securely to my account** so that I can **view my details**
14. As a **user** I can **see contact information for the trainer** so that I can **get in touch as required**
15. As a **user** I can **send a message to the trainer** so that I **ask questions if I want to**
16. As a **user** I can **see location information for the trainer** so that I **know where to go for sessions**
17. As a **user** I can **find the trainers social media accounts** so that I **follow their accounts**

### Site Admin

18. As a **site admin** I can **display a welcoming home screen** so that **users will want to see the sessions and blogs I offer**
19. As a **site admin** I can **create, delete, and edit sessions** so that **I can tailor the information available to users**
20. As a **site admin** I can **add diary entries** so that **users can book sessions**
21. As a **site admin** I can **receive booking emails** so that **I am informed when users book with me**
22. As a **site admin** I can **create, delete, and edit blogs** so that **I can produce new blog content and maintain it as needed**
23. As a **site admin** I can **add blogs in a draft state** so that **they are only public when I want them to be**
24. As a **site admin** I can **allow users to comment on blog posts** so that **they can engage with the post**
25. As a **site admin** I can **approve comments** so that **ensure that only appropriate comments are published**
26. As a **site admin** I can **get comment notifications** so that **I am aware when a comment needs to be approved**
27. As a **site admin** I can **receive questions and comments submitted from my contact page** so that I can **answer user queries**

### Kanban, & User Stories

- GitHub Kanban was used to track all open user stories
- Ready, In Progress, Testing, Done headings were used in the kanban

#### User Stories

<details><summary>User Account</summary>

![Account](/static/Readme_images/issues_account.png)
</details>

<details><summary>Blog</summary>

![Blog](/static/Readme_images/issues_blog.png)
</details>

<details><summary>Contact</summary>

![Contact](/static/Readme_images/issues_contact.png)
</details>

<details><summary>General</summary>

![General](/static/Readme_images/issues_general.png)
</details>

<details><summary>Session</summary>

![Session](/static/Readme_images/issues_session.png)
</details>

#### Kanban Board

<details><summary>Kanban examples at various stages of the project</summary>

Basic Welcome page complete, contact form in testing and session booking in progress
![Kanban_1](/static/Readme_images/kanban_1.png)

Session editing in testing and blog functions in progress
![Kanban_2](/static/Readme_images/kanban_2.png)

Comment and likes in testing, comment notifications and approval in progress
![Kanban_3](/static/Readme_images/kanban_3.png)

All work completed
![Kanban_4](/static/Readme_images/kanban_4.png)
</details>

##### Back to [top](#table-of-contents)<hr>

## Wireframes
Balsamiq is the tool that I commonly use to wireframe my projects.  It has the capability to quickly and easily draft website layouts on a multitude of representative platform sizes.  

<details><summary>Welcome</summary>  

![Welcome](/static/Readme_images/wireframe_welcome.png)
</details>

<details><summary>Blog</summary>  

Blog Preview
![Blog Preview](/static/Readme_images/wireframe_blog.png)

Blog Detail
![Blog Detail](/static/Readme_images/wireframe_read.png)
</details>

<details><summary>Sessions</summary>  

Session Details
![Session Details](/static/Readme_images/wireframe_sessions.png)

Session Booking
![Session Booking](/static/Readme_images/wireframe_booking.png)
</details>

<details><summary>Contact Me</summary>  

![Contact Me](/static/Readme_images/wireframe_contact.png)
</details>

<details><summary>User Account</summary>  

![User Account](/static/Readme_images/wireframe_account.png)
</details>

##### Back to [top](#table-of-contents)<hr>

## Design

### Colors

The colour scheme was chosen to provide a good contrast for accesibility whilst also being quite subtle.  The black for the header and social footer was given a transparancy of 90% to make it less harsh.

The images were then created with a blue gradient/orange theme to add more color and interest to the site.

### Fonts

 The font selected was sans-serif with different sizing, weight and spacing used to add interest to the text.

##### Back to [top](#table-of-contents)<hr>

## Structure

The site was designed for the user to find the layout simple to use and navigate through.

The header contains a top section in black which contains the company name and login/logout/sign up functions.  Below that is the nav bar colored beige.

The footer is in two sections, mirroring the header.  The beige section includes location and contact information with the black section containing links for the site owners social accounts.

### Website pages

- The site consists of the following pages:

  Welcome page

  The Blog
  - Blog listing
  - Blog detail

  Sessions
  - Session Listing
  - Session Booking
  - No Sessions Availble
  - Session Booked

  Contact me
  - Contact form
  - Contact Success

  User account

  Note:
  Django admin template were used for all admin functions hence there was no need to design a specific page for this

##### Back to [top](#table-of-contents)<hr>

## ElephantSQL

ElephantSQL was used to host the SQL database.

This elegant solution allows cloud based stroage to be used so the same DB can be used at all time.  This is especially useful during development as local and deployed versions can be tested with the same data saving time and aiding consistency of results.

<details><summary>ElephantSQL details</summary>

![ElephantSQL](/static/Readme_images/elephantsql.png)<br>

</details>

##### Back to [top](#table-of-contents)<hr>

## Database

<details><summary>See Database Diagram</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/database/database-diagram.png">
</details>

##### Back to [top](#table-of-contents)<hr>

## Models  

### User Model

| Key        | Name         | Type        |
| ---------- | ------------ | ----------- |
| PrimaryKey | user_id      | AutoField   |
|            | password     | Varchar     |
|            | last_login   | Varchar     |
|            | is_superuser | Boolean     |
|            | username     | Varchar     |
|            | first_name   | Varchar    |
|            | last_name    | Varchar     |
|            | email        | Varchar     |
|            | is_staff     | Boolean     |
|            | is_active    | Boolean     |
|            | date_joined  | Varchar     |

### Posts Model

| Key        | Name                 | Type          |
| ---------- | -------------------- | ------------- |
| PrimaryKey | id      | AutoField     |
| ForeignKey | author | User model |
|            | title                | Char model    |
|            | slug | SlugField     |
|            | last_update | DateTimeField |
|            | content    | TextField |
|            | image       | CloudinaryField |
|            | excerpt     | TextField |
|            | created_on      | DateTimeField |
|            | status       | IntegerField |
|            | category     | IntegerField |
|            | likes      | ManyToManyField |

### Comments Model

| Key        | Name                 | Type          |
| ---------- | -------------------- | ------------- |
| PrimaryKey | id                   | AutoField     |
| ForeignKey | post                | Post model   |
|            | name                 | CharField     |
|            | email                 | EmailField     |
|            | body                 | TextField |
|            | created_on               | DateTimeField |
|            | approved          | BooleanField     |

### Sessions Model

| Key        | Name                 | Type          |
| ---------- | -------------------- | ------------- |
| PrimaryKey | id                   | AutoField     |
|            | session_type           | TextField  |
|            | description           | CharField  |
|            | excerpt           | TextField  |
|            | image          | CloudinaryField  |
|            | last_update           | DateTimeField  |
|            | created_on          | DateTimeField  |

### Appointments Model

| Key        | Name                 | Type          |
| ---------- | -------------------- | ------------- |
| PrimaryKey | id                   | AutoField     |
|            | appointment_type           | TextField  |
|            | date_time           | DateTimeField  |
|            | booking_id           | OneToOneField  |

### Bookings Model

| Key        | Name                 | Type          |
| ---------- | -------------------- | ------------- |
| PrimaryKey | id                   | AutoField     |
| ForeignKey | user          | Profile model  |
|            | session_type           | TextField  |
|            | notes           | TextField  |
|            | appointment           | OneToOneField  |
|            | last_update           | DateTimeField  |
|            | created_on          | DateTimeField  |

##### Back to [top](#table-of-contents)<hr>

## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python
- Django
- Bootstrap

### Libraries & Tools

- [Balsamiq](https://balsamiq.com/)
- [Favicon.io](https://favicon.io)
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/)
- [Font Awesome](https://fontawesome.com/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Heroku Platform](https://id.heroku.com/login)
- [Elephant SQL](https://customer.elephantsql.com/instance)
- [Cloudinary](https://cloudinary.com/)
- [jQuery](https://jquery.com)
- [Postgres](https://www.postgresql.org/)
- Validation:
  - [WC3 Validator](https://validator.w3.org/)
  - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
  - [JShint](https://jshint.com/)
  - [CI Python Liner(PEP8)](https://pep8ci.herokuapp.com/)
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
  - [Wave Validator](https://wave.webaim.org/)

##### Back to [top](#table-of-contents) 

## Features

### Header

- Featured on all pages
- The first section provides login/logout/signup options
- The second section provides simple navigation with clear icons and hover functionality
- User stories covered: 12, 13

<details><summary>See feature images</summary>

![Header](/static/Readme_images/feature_header.png)
</details>

### Footer

- Featured on all pages
- There are 2 section, one for contact and location information and one for social media links
- User stories covered: 14, 16, 17, 18

<details><summary>See feature images</summary>

![Footer](/static/Readme_images/feature_footer.png)
</details>

### Welcome Page

- Main Landing page for the site
- Displays hero image
- Contains 3 main sections that link to the main functionality for each type - blogs, sessions and contact me
- User stories covered: 1, 7, 14, 18

<details><summary>See feature images</summary>

![Welcome Blogs](/static/Readme_images/feature_welcome_blog.png)
![Welcome Sessions](/static/Readme_images/feature_welcome_sessions.png)
![Welcome Contact](/static/Readme_images/feature_welcome_contact.png)

</details>

### Blog Listing

- Shows all the available blogs
- gives the option to like a blog if you are logged in
- User stories covered: 7, 8, 10

<details><summary>See feature images</summary>

![Blog Listing](/static/Readme_images/feature_blog_listing.png)
</details>

### Blog Detail

- Shows the blog detail
- Gives the option to comment on a blog if you are logged in
- User stories covered: 9, 11, 24

<details><summary>See feature images</summary>

![Blog Detail](/static/Readme_images/feature_blog_detail.png)
</details>

### Blog Comment Notification

- Alerts the admin that there are comments to be approved
- User stories covered: 26

<details><summary>See feature images</summary>

![Blog Comment Notification](/static/Readme_images/feature_notification.png)
</details>

### Session Detail

- Shows the user what sessions are available and detailed information about each session
- User stories covered: 2

<details><summary>See feature images</summary>

![Session Detail](/static/Readme_images/feature_session_detail.png)
</details>

### Session Booking

- Allows the user to book sessions and leave notes about the booking
- The user is emailed once a booking has been made
- A success screen is shown on booking, a failure screen is shown if no sessions are available
- User stories covered: 3, 5, 6, 21

<details><summary>See feature images</summary>

![Session Booking](/static/Readme_images/feature_booking.png)
![Session Booked](/static/Readme_images/feature_booking_success.png)
![Session Failure](/static/Readme_images/feature_booking_failure.png)
</details>

### Contact Me

- Allows the user to communicate with the site owner
- The site owner is emailed once a message has been sent
- A success screen is shown once sent
- User stories covered: 14, 15, 27

<details><summary>See feature images</summary>

![Session Booking](/static/Readme_images/feature_contact.png)
![Session Booked](/static/Readme_images/feature_contact_success.png)
</details>

### User Account

- Allows the user see their details and bookings
- Allows the user to cancel bookings
- User stories covered: 13, 4

<details><summary>See feature images</summary>

![Session Booking](/static/Readme_images/feature_account.png)
</details>

### Admin Section

- Allows the site owner to create/edit/destroy posts, sessions, appointments, users, bookings and comments
- User stories covered: 19, 20, 22, 23, 25

<details><summary>See example feature images</summary>

![Session Booking](/static/Readme_images/feature_admin_1.png)
![Session Booking](/static/Readme_images/feature_admin_2.png)
![Session Booking](/static/Readme_images/feature_admin_3.png)
</details>

##### Back to [top](#table-of-contents)

## Validation  

## HTML Validation

The W3C Markup Validation Service was used to validate the HTML of the website.  

### Welcome  

welcome.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpuredrivefitness-68f4e5eedb4f.herokuapp.com%2F)

- No Errors Found

### Login  

login.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpuredrivefitness-68f4e5eedb4f.herokuapp.com%2Faccounts%2Flogin%2F)

- No Errors Found

### Sign Up

signup.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpuredrivefitness-68f4e5eedb4f.herokuapp.com%2Faccounts%2Fsignup%2F)

| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | Embedded Sign up page | End tag p implied, but there were open elements. | Error on system template.  Does not affect view or site performance |
| Error | Embedded Sign up page | Unclosed element span. | Error on system template.  Does not affect view or site performance |
| Error | Embedded Sign up page |  Stray end tag span. | Error on system template.  Does not affect view or site performance |
| Error | Embedded Sign up page |  No p element in scope but a p end tag seen. | Error on system template.  Does not affect view or site performance |

### Sign Out

signout.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpuredrivefitness-68f4e5eedb4f.herokuapp.com%2Faccounts%2Flogout%2F)

- No Errors Found

### Blog List

blog.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpuredrivefitness-68f4e5eedb4f.herokuapp.com%2Fblog%2F)

- No Errors Found

### Blog Detail Page

blog_detail.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpuredrivefitness-68f4e5eedb4f.herokuapp.com%2Fblog%2Fshopping-for-fitness%2F)

- No Errors Found  

### Booking Page

booking.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpuredrivefitness-68f4e5eedb4f.herokuapp.com%2Fbooking%2F)

| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | Booking | Bad value /booking/booking_form/?session_type=Weight Loss for attribute href on element a: Illegal character in query: space is not allowed. | Not a html error but an error in data passed into the html code |

### Booking Form

booking_form.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpuredrivefitness-68f4e5eedb4f.herokuapp.com%2Fbooking%2Fbooking_form%2F%3Fsession_type%3DMotivation)

- No Errors Found, 1 info notice

| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Info | Booking Form | Trailing slash on void elements has no effect and interacts badly with unquoted attribute values. | Inconsequntial error passed in by standard form|

### Booking Success

booking_success.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpuredrivefitness-68f4e5eedb4f.herokuapp.com%2Fuser-account%2F#textarea)

- No Errors Found

### Booking Unavailable

booking_full.html [results](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpuredrivefitness-68f4e5eedb4f.herokuapp.com%2Fbooking%2Fbooking_form%2F%3Fsession_type%3DMotivation)

- No Errors Found, 1 info notice

| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Info | Booking Full | Trailing slash on void elements has no effect and interacts badly with unquoted attribute values. | Inconsequntial error passed in by standard form|

### Contact Me

contact.html [results](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpuredrivefitness-68f4e5eedb4f.herokuapp.com%2Fcontact%2F)

- No Errors Found

### Contact Success

success.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpuredrivefitness-68f4e5eedb4f.herokuapp.com%2Fsuccess%2F)

- No Errors Found

### Account Page

account.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpuredrivefitness-68f4e5eedb4f.herokuapp.com%2Fuser-account%2F#textarea)

- No Errors Found

##### Back to [top](#table-of-contents)

### CSS Validation
The W3C Jigsaw CSS Validation Service was used to validate the CSS of the website.

<details><summary>base.css</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-css.png">
</details> 

<details><summary>account.css</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-css.png">
</details> 

<details><summary>cart.css</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-css.png">
</details> 

<details><summary>checkout.css</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-css.png">
</details> 

<details><summary>contact.css</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-css.png">
</details> 

<details><summary>home.css</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-css.png">
</details> 

<details><summary>products.css</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-css.png">
</details> 

<details><summary>profile.css</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-css.png">
</details> 

##### Back to [top](#table-of-contents)

### JavaScript Validation
JSHint javaScript Validation Service was used to validate all javaScript files.

<details><summary>base.js</summary>  
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-js-base.png">
</details>  

- No issues raised

<details><summary>custom_admin.js</summary>  
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-js-base.png">
</details>  

- No issues raised


<details><summary>home.js</summary>  
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-js-base.png">
</details>  

- No issues raised

<details><summary>product-management.js</summary>  
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-js-product-management.png">
</details>  

- No issues raised

<details><summary>products.js</summary>  
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-js-products.png">
</details>  

- No issues raised

<details><summary>quantity-input.js</summary>  
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-js-quantity-input.png">
</details>  

- No issues raised

<details><summary>stripe_elements.js</summary>  
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-js-stripe-elements.png">
</details>  

- one undefined variable Stripe which originates from a external script
- one undefined variable $ which originates from jquery a external script

<details><summary>toasts.js</summary>  
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-js-toasts.png">
</details>  

- No issues raised


##### Back to [top](#table-of-contents)<hr> 

## PEP8 Validation
[CI Python Linter](https://pep8ci.herokuapp.com/) was used to check the code for PEP8 requirements.


### Cart

<details><summary>contexts.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-cart-contexts.png">
</details>

<details><summary>cart_tools.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-cart-cart-tools.png">
</details>

<details><summary>test_contexts.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-cart-test-contexts.png">
</details>

<details><summary>test_views.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-cart-test-views.png">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-cart-urls.png">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-cart-views.png">
</details>

<hr>

### Checkout

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-checkout-forms.png">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-checkout-models.png">
</details>

<details><summary>signals.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-checkout-signals.png">
</details>

<details><summary>test_forms.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-checkout-test-forms.png">
</details>

<details><summary>test_models.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-checkout-test-models.png">
</details>

<details><summary>test_views.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-checkout-test-views.png">
</details>

<details><summary>test_webhook_handler.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-checkout-test-webhook-handler.png">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-checkout-urls.png">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-checkout-views.png">
</details>

<details><summary>webhook_handler.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-checkout-webhook-handler.png">
</details>

<details><summary>webhooks.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-checkout-webhooks.png">
</details>

<hr>

### Contact

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-contact-forms.png">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-contact-models.png">
</details>

<details><summary>test_forms.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-contact-test-forms.png">
</details>

<details><summary>test_models.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-contact-test-models.png">
</details>

<details><summary>test_views.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-contact-test-views.png">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-contact-urls.png">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-contact-views.png">
</details>

<hr>

### Custom Admin

<details><summary>contexts.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-custom-admin-contexts.png">
</details>

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-custom-admin-forms.png">
</details>

<details><summary>test_forms.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-custom-admin-test-forms.png">
</details>

<details><summary>test_views.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-custom-admin-test-views.png">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-custom-admin-urls.png">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-custom-admin-views.png">
</details>

<details><summary>widgets.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-custom-admin-widgets.png">
</details>

<hr>

### Home

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-home-models.png">
</details>

<details><summary>test_views.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-home-test-views.png">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-home-urls.png">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-home-views.png">
</details>

<hr>

### Infinity Innovations

<details><summary>asgi.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-ii-asgi.png">
</details>

<details><summary>settings.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-ii-settings.png">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-ii-urls.png">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-ii-views.png">
</details>

<details><summary>wsgi.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-ii-wsgi.png">
</details>

<hr>

### Products

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-products-models.png">
</details>

<details><summary>test_models.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-products-test-models.png">
</details>

<details><summary>test_views.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-products-test-views.png">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-products-urls.png">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-products-views.png">
</details>

<hr>

### Products

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-profiles-forms.png">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-profiles-models.png">
</details>

<details><summary>test_forms.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-profiles-test-forms.png">
</details>

<details><summary>test_models.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-profiles-test-models.png">
</details>

<details><summary>test_views.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-profiles-test-views.png">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-profiles-urls.png">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-profiles-views.png">
</details>

<hr>

### Root

<details><summary>custom_storages.py</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/validation/validation-py-root-custom-storages.png">
</details>

##### Back to [top](#table-of-contents)<hr> 

## Accessibility  
The [WAVE WebAIM web accessibility evaluation tool](https://wave.webaim.org/) was used to ensure the website met high accessibility standards.  
- All pages returned 0 errors.
- I have added sr only tags throught the website to ensure that the website is accessible
- There are contrast errors, there is not a dark enough orange to have white text, I have decided to change the color as dark as I can but these contrast errors still exist
- To suit the them of my website I'm keeping the orange color
- All alerts presented were for redundant links whichweres taken into account during development.

<details><summary>Home</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/accessibility/access-home.png">
</details>

<details><summary>Product List</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/accessibility/access-product-list.png">
</details> 

<details><summary>Product Detail</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/accessibility/access-product-detail.png">
</details>

<details><summary>Checkout</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/accessibility/access-checkout.png">
</details>

<details><summary>Checkout Success</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/accessibility/access-checkout-success.png">
</details>

<details><summary>Contact</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/accessibility/access-contact.png">
</details>

<details><summary>Profile</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/accessibility/access-profile.png">
</details>

<details><summary>Reviews</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/accessibility/access-reviews.png">
</details>

<details><summary>Policy</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/accessibility/access-policy.png">
</details>

<details><summary>Login</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/accessibility/access-login.png">
</details>

<details><summary>Logout</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/accessibility/access-logout.png">
</details>

<details><summary>Reset Password</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/accessibility/access-password-rest.png">
</details>

<details><summary>Register</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/accessibility/access-register.png">
</details>

<details><summary>Admin Management</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/accessibility/access-management.png">
</details>

<details><summary>404</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/accessibility/access-home.png">
</details>

##### Back to [top](#table-of-contents)<hr> 

## Lighthouse

Performance, best practices and SEO was tested using Lighthouse.

<details><summary>Home</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/lighthouse/lh-home.png">
</details>

<details><summary>Product List</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/lighthouse/lh-product-list.png">
</details> 

<details><summary>Product Detail</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/lighthouse/lh-product-detail.png">
</details>

<details><summary>Checkout</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/lighthouse/lh-checkout.png">
</details>

<details><summary>Checkout Success</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/lighthouse/lh-checkout-success.png">
</details>

<details><summary>Contact</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/lighthouse/lh-contact.png">
</details>

<details><summary>Profile</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/lighthouse/lh-profile.png">
</details>

<details><summary>Reviews</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/lighthouse/lh-reviews.png">
</details>

<details><summary>Policy</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/lighthouse/lh-policy.png">
</details>

<details><summary>Login</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/lighthouse/lh-login.png">
</details>

<details><summary>Logout</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/lighthouse/lh-logout.png">
</details>

<details><summary>Reset Password</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/lighthouse/lh-reset-password.png">
</details>

<details><summary>Register</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/lighthouse/lh-register.png">
</details>

<details><summary>Custom Admin</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/lighthouse/lh-custom-admin.png">
</details>

<details><summary>Admin Management</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/lighthouse/lh-management.png">
</details>

<details><summary>404</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/lighthouse/lh-home.png">
</details>

##### Back to [top](#table-of-contents)<hr> 

## Testing

1. Manual testing User Stories
2. Automated testing

### Manual testing

1. As a **customer** I can **login, register and logout** so that **buy items and save my information**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Register | Hover over or click the account button, then click the register button, use your email and enter into the two email fields, enter a username, and a password into the two password fields, click sign up button, go to your email and confirm the email, you are now registered | User is brought to the sign up page, user is then sent confirmation email, user is then sent to confirmation page, user is then notified that they have registered | Works as expected |
| Login | Hover over or click the account button, then click the login button, use your email and enter into the email field, or enter your username, and then enter your password into the password field, click sign in button, you are now logged in | User is brought to the login page, user is then notified that they have logged in | Works as expected |
| Logout | Hover over or click the account button, then click the logout button, click sign out button, you are now logged out | User is brought to the logout page, user is then notified that they have logged out | Works as expected |

<details><summary>See Register Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-register-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-register-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-register-3.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-register-4.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-register-5.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-register-6.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-register-7.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-register-8.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-register-9.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-register-10.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-register-11.png"><br>
</details>

<details><summary>See Login Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-login-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-login-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-login-3.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-login-4.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-login-5.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-login-6.png"><br>
</details> 

<details><summary>See Logout Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-logout-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-logout-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-logout-3.png"><br>
</details> 

<br>

2. As a **customer** I can **easily navigate the website** so that **I find my item and pay for it**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Header | Hover over or click the header, user can search and go to other pages, hover over or click real or digital in header, user is brought to products page | User is presented with navigation to home, products, profile, contact, checkout, cart | Works as expected |

<details><summary>See Header Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-header-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-header-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-header-3.png"><br>
</details> 

<br>

3. As a **customer** I can **view a list of products** so that **decide what item I'm buying**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Proudct List | Click the call to action button in the home hero or use the real or digital header buttons to navigate to the product list page | User is presented with list of products | Works as expected |

<details><summary>See Proudct list Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-list-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-list-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-list-3.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-list-4.png"><br>
</details> 

<br>

4. As a **customer** I can **search list of products** so that **I can find the item I want to buy**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Proudct Search | Click the search input in the header, type in what you want to search for, press enter or click the search button | User is presented with list of products that they searched for | Works as expected |

<details><summary>See Proudct Search Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-search-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-search-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-search-3.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-search-4.png"><br>
</details> 

<br>

5. As a **customer** I can **filter list of products** so that **I can find the item I want to buy**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Proudct Filter | Navigate to the product list page, click the filter box's, select a filter from the dropdown menu | User is presented with list of products that they filtered for | Works as expected |

<details><summary>See Proudct Filter Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-3.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-4.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-5.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-6.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-7.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-8.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-9.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-10.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-11.png"><br>
</details> 

<br>

6. As a **customer** I can **sort the list of products** so that **find the item I want to buy**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Proudct Filter | Navigate to the product list page, click the sort dropdown box, select a sort filter from the dropdown menu | User is presented with list of products sorted in their selected choice | Works as expected |

<details><summary>See Proudct Sort Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-3.png"><br>
</details> 

<br>

7. As a **customer** I can **click to see more info on a product** so that **decide to buy the item**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Proudct Detail | Navigate to the product list page, click the on the image of a product | User is brought to product detail page, info is presented | Works as expected |

<details><summary>See Proudct Detail Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-detail-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-detail-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-detail-3.png"><br>
</details> 

<br>

8. As a **customer** I can **add a product to my cart** so that **I can buy it later**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Proudct Detail | Navigate to the product list page, click the on the image of a product, click add to cart button | User cart is updated, user is notified | Works as expected |

<details><summary>See Proudct Detail Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-detail-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-detail-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-detail-3.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-detail-4.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-detail-5.png"><br>
</details> 

<br>

9. As a **customer** I can **choose the correct product theme** so that **I can buy the correct product theme**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Proudct Detail | Navigate to the product list page, click the on the image of a product, click the theme dropdown container, select the correc theme, click add to cart button | User cart is updated, user is notified | Works as expected |

<details><summary>See Proudct Detail Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-detail-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-detail-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-detail-3.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-detail-6.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-detail-4.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-detail-5.png"><br>
</details> 

<br>

10. As a **customer** I can **add multiple items of product to the cart** so that **buy more than one item**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Proudct Detail | Navigate to the product list page, click the on the image of a product, click the quantity input and enter input or click the increment and decrement buttons, click add to cart button | User cart is updated, user is notified | Works as expected |

<details><summary>See Proudct Detail Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-detail-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-detail-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-detail-3.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-detail-7.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-detail-8.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-detail-9.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-detail-4.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-product-detail-5.png"><br>
</details> 

<br>

11. As a **customer** I can **view my items in the cart** so that **I know what I'm buying**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Cart | Hover and click the cart button in the top right | User's cart is displayed | Works as expected |

<details><summary>See Cart Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-cart-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-cart-2.png"><br>
</details> 

<br>

12. As a **customer** I can **delete items from my cart** so that **I can change my order and what I'm buying**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Cart | Hover and click the cart button in the top right, click the delete button | Item from the cart is deleted, user is notified | Works as expected |

<details><summary>See Cart Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-cart-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-cart-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-cart-3.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-cart-4.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-cart-5.png"><br>
</details> 

<br>

13. As a **customer** I can **change the item type and quantity** so that **I can change what I'm buying**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Cart | Hover and click the cart button in the top right, click the quantity input and enter quantity and click update | Item from the cart is updated, user is notified | Works as expected |

<details><summary>See Cart Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-cart-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-cart-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-cart-6.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-cart-7.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-cart-8.png"><br>
</details> 

<br>

14. As a **customer** I can **pay for the items in my cart** so that **I can receive the order**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Checkout | Hover and click the cart button in the top right, click the checkout order button, fill out form, click the complete order button | User is brought to checkout page, user is notified when order is complete | Works as expected |

<details><summary>See Checkout Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-checkout-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-checkout-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-checkout-3.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-checkout-4.png"><br>
</details> 

<br>

15. As a **customer** I can **receive a confimation email** so that **I can receive my order**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Checkout Success | Hover and click the cart button in the top right, click the checkout order button, fill out form, click the complete order button | User is brought to checkout page, user is notified when order is complete | Works as expected |

<details><summary>See Checkout Success Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-checkout-5.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-checkout-6.png"><br>
</details> 

<br>

16. As a **customer** I can **update and save my profile information** so that **easily buy again**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Profile | Hover and click the view profile button in the top right, fill out form, click the update information form | User is brought to profile page, user is notified | Works as expected |

<details><summary>See Profile Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-profile-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-profile-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-profile-3.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-profile-4.png"><br>
</details> 

<br>

17. As a **customer** I can **contact the site admin** so that **I can talk about any issues I might have**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Contact | Hover and click the view contact button in the top right, fill out form, click the send button | User is brought to contact page, user is notified | Works as expected |

<details><summary>See Contact Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-contact-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-contact-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-contact-3.png"><br>
</details> 

<br>

18. As a **customer** I can **talk to a chatbot** so that **I can get help when buying**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| ChatBot | Click the chatbot button in the bottom right, ask it a question about the company | Chatbot returns answer about the company | Works as expected |
| ChatBot | Click the chatbot button in the bottom right, say a good thing about your product you bought, click yes sure after response, enter a short review | Chatbot returns answer asking you to enter a competition, chatbot will take short review and make a full review | Works as expected |
| ChatBot | Click the chatbot button in the bottom right, ask it a question about the your order tracking, then type in your order number | Chatbot returns answer to what your order status is and tracks the order | Works as expected |
| ChatBot | Click the chatbot button in the bottom right, ask it a question about the your looking for products, click yes sure button | Chatbot returns answer about your desired products, also return links to products | Works as expected |

<details><summary>See Contact Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-chatbot-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-chatbot-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-chatbot-3.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-chatbot-4.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-chatbot-5.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-chatbot-6.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-chatbot-7.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-chatbot-8.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-chatbot-9.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-chatbot-10.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-chatbot-11.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-chatbot-12.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-chatbot-13.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-chatbot-14.png"><br>
</details> 

<br>

19. As a **customer** I can **view a specific category of products** so that **find the product I want to buy**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Proudct Filter | Navigate to the product list page, click the filter box's, select a filter from the dropdown menu | User is presented with list of products that they filtered for | Works as expected |

<details><summary>See Proudct Filter Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-3.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-4.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-5.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-6.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-7.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-8.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-9.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-10.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-11.png"><br>
</details> 

<br>

20. As a **customer** I can **view a specific brand of products** so that **I can find the product I'm looking for**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Proudct Filter | Navigate to the product list page, click the filter box's, select a filter from the dropdown menu | User is presented with list of products that they filtered for | Works as expected |

<details><summary>See Proudct Filter Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-3.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-4.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-5.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-6.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-7.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-8.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-9.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-10.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-filter-sort-11.png"><br>
</details> 

<br>

21. As a **customer** I can **see a notification when completing an action** so that **I know my action was a success**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Profile | Hover and click the view profile button in the top right, fill out form, click the update information form | User is brought to profile page, user is notified | Works as expected |

<details><summary>See Profile Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-profile-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-profile-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-profile-3.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-profile-4.png"><br>
</details> 

<br>

22. As a **customer** I can **track my order** so that **I can see when it is delivered and where my order is**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Track Order | Hover and click the view profile button in the top right, click the order number under order history, click track order | User is brought to track order page | Works as expected |

<details><summary>See Track Order Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-track-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-track-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-track-3.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-track-4.png"><br>
</details> 

<br>

23. As a **customer** I can **see and write a review** so that **decide to buy and give feedback**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| ChatBot | Click the chatbot button in the bottom right, say a good thing about your product you bought, click yes sure after response, enter a short review | Chatbot returns answer asking you to enter a competition, chatbot will take short review and make a full review | Works as expected |

<details><summary>See Chatbot Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-chatbot-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-chatbot-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-chatbot-5.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-chatbot-6.png"><br>
</details> 

<br>

24. As a **site admin** I can **display a welcoming home screen** so that **customers will be willing to buy**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Home | Click the home button in the top left | Welcoming home screen is displayed | Works as expected |

<details><summary>See Home Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-home-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-home-2.png"><br>
</details> 

<br>

25. As a **site admin** I can **add new products to the list** so that **customers can buy new products**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Custom Admin | Click the admin button in the top right unser the account dropdown, click the add product button under product management, fill out form and click add product button | User is taken to custom admin, then to form page | Works as expected |

<details><summary>See Custom Admin Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-2.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-3.png"><br>
</details> 

<br>

26. As a **site admin** I can **update products from the list** so that **customers have correct information about products**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Custom Admin | Click the admin button in the top right unser the account dropdown, click the edit product button under product management, select your product, click select button, fill out form and click edit product button | User is taken to custom admin, then to form page | Works as expected |

<details><summary>See Custom Admin Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-4.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-5.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-6.png"><br>
</details> 

<br>

27. As a **site admin** I can **delete products from the list** so that **customers can buy new products**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Custom Admin | Click the admin button in the top right unser the account dropdown, click the delete product button under product management, select your product, click select button, fill out form and click delete product button | User is taken to custom admin, then to form page | Works as expected |

<details><summary>See Custom Admin Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-7.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-5.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-6.png"><br>
</details> 

<br>

28. As a **site admin** I can **add new categories to list** so that **customers can easily navigate products**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Custom Admin | Click the admin button in the top right unser the account dropdown, click the add category button under category management, fill out form and click add category button | User is taken to custom admin, then to form page | Works as expected |

<details><summary>See Custom Admin Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-8.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-3.png"><br>
</details> 

<br>

29. As a **site admin** I can **update categories from the list** so that **customers can correctly see each category**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Custom Admin | Click the admin button in the top right unser the account dropdown, click the edit category button under category management, select your category, click select button, fill out form and click edit category button | User is taken to custom admin, then to form page | Works as expected |

<details><summary>See Custom Admin Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-9.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-5.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-6.png"><br>
</details> 

<br>

30. As a **site admin** I can **delete categories from the list** so that **I can update products into their correct category**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Custom Admin | Click the admin button in the top right unser the account dropdown, click the delete product button under product management, select your product, click select button, fill out form and click delete product button | User is taken to custom admin, then to form page | Works as expected |

<details><summary>See Custom Admin Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-12.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-5.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-6.png"><br>
</details> 

<br>

31. As a **site admin** I can **add new brands to list** so that **customers can easily navigate products**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Custom Admin | Click the admin button in the top right unser the account dropdown, click the add brand button under brand management, fill out form and click add brand button | User is taken to custom admin, then to form page | Works as expected |

<details><summary>See Custom Admin Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-14.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-3.png"><br>
</details> 

<br>

32. As a **site admin** I can **update brands from the list** so that **customers can correctly see each brand**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Custom Admin | Click the admin button in the top right unser the account dropdown, click the edit brand button under brand management, select your brand, click select button, fill out form and click edit brand button | User is taken to custom admin, then to form page | Works as expected |

<details><summary>See Custom Admin Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-15.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-5.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-6.png"><br>
</details> 

<br>

33. As a **site admin** I can **delete brands from the list** so that **I can update products into their correct brand**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Custom Admin | Click the admin button in the top right unser the account dropdown, click the delete brand button under brand management, select your brand, click select button, fill out form and click delete brand button | User is taken to custom admin, then to form page | Works as expected |

<details><summary>See Custom Admin Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-18.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-5.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/manual-testing/mt-admin-6.png"><br>
</details> 

##### Back to [top](#table-of-contents)<hr> 

### Automated testing

- Testing was done using the built in Django module, unittest.
- Coverage was also usesd to generate a report

#### Cart

- test_contexts.py
- test_views.py

<details><summary> See images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/auto-tests/at-cart.png">
</details>

#### Checkout

- test_forms.py
- test_models.py
- test_views.py
- test_webhook_handler.py

<details><summary> See images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/auto-tests/at-checkout.png">
</details>

#### Contact

- test_forms.py
- test_models.py
- test_views.py

<details><summary> See images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/auto-tests/at-contact.png">
</details>

#### Custom Admin

- test_forms.py
- test_views.py

<details><summary> See images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/auto-tests/at-custom-admin.png">
</details>

#### Home

- test_views.py

<details><summary> See images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/auto-tests/at-home.png">
</details>

#### Products

- test_models.py
- test_views.py

<details><summary> See images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/auto-tests/at-products.png">
</details>

#### Profiles

- test_forms.py
- test_models.py
- test_views.py

<details><summary> See images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/auto-tests/at-profiles.png">
</details>

### Coverage  
A Python test plugin called coverage was used to generate the following results and display how much of the code was covered by the unittest module.

<details><summary> Coverage</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/auto-tests/at-coverage-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/auto-tests/at-coverage-2.png">
</details>

### Device Testing & Browser compatibility

The site uses to test on various real world devices was [BrowserStack](https://www.browserstack.com/)  

This allowed me to test on real devices and not just device emulators.

##### Back to [top](#table-of-contents)<hr> 

## Bugs

| **Bug** | **Fix** |
| ------- | ------- |
| Chatbot - if you ask a certain question, the chatbot intelligence can't give you an accurate answer | Spend more time and resources to improve chatbot intelligence |
| Homepage - typewriter text - if you exit the page onto another page and return to the page, it will glitch the typewriter text | Add a js listener to block the function from calling if the user exits the page |

##### Back to [top](#table-of-contents)<hr>

## Deployment

### Heroku Deployment

[Official Page](https://devcenter.heroku.com/articles/git) (Ctrl + click)

This application has been deployed from GitHub to Heroku. A guide to deploying to Heroku can be found [here](https://devcenter.heroku.com/articles/github-integration)
Here are the steps to deployment
- Login or create an account at [Heroku](https://dashboard.heroku.com/)

<details><summary> See images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/heroku/deployment-1.png">
</details>

- Click on New > Create new app in the top right of the screen.

<details><summary> See images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/heroku/deployment-2.png">
</details>

- Add an app name and select location, then click 'create app'.

<details><summary> See images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/heroku/deployment-3.png">
</details>

- Under the deploy tab of the next page, select connect to GitHub.

- Log in to your GitHub account when prompted.

<details><summary> See images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/heroku/deployment-4.png">
</details>

- Select the repository that you want to be connected to the Heroku app.

<details><summary> See images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/heroku/deployment-5.png">
</details>

- Click on the settings tab.

<details><summary> See images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/heroku/deployment-6.png">
</details>

- Scroll down to the config vars section, and add 2 config vars:
    * The first key is CREDS and the value here is the creds.json file that was generated for the google sheets API to work properly.
    * The second key is PORT and the Value is 8000
  

<details><summary> See images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/heroku/deployment-7.png">
</details>

- Once you have set up the config vars, scroll down to buildpacks (still under the settings tab)

- Add the Python and Node.js buildpacks to your app and make sure that when they are displayed, they appear in the order:
    * Python
    * Node.JS
  

<details><summary> See images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/heroku/deployment-8.png">
</details>

- Navigate back to the settings tab.

- Select automatic deploys to allow Heroku to build the site with new changes each time changes are pushed to GitHub.

<details><summary> See images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/heroku/deployment-9.png">
</details>

- In the 'manual deploy' section beneath this, make sure the branch selected is 'main' and click deploy branch.

<details><summary> See images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/heroku/deployment-10.png">
</details>

### AWS S3 Bucket Setup  

To set up an AWS S3 bucket:

1. Sign in to the AWS Management Console and open the Amazon S3 console.  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/aws/aws-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/aws/aws-2.png">
</details>

2. Click on the "Create Bucket" button.  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/aws/aws-3.png">
</details>

3. Enter a unique name for your bucket, and select the region where you want the bucket to be located.
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/aws/aws-4.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/aws/aws-5.png">
</details>

4. Configure any additional options, such as versioning, object-level logging, and object tagging, as needed.  

5. Click on the "Create" button to create the bucket.

6. Set up the appropriate permissions for the bucket, such as access control lists (ACLs) and bucket policies, to control who can access the data in the bucket.  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/aws/aws-6.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/aws/aws-7.png">
</details>

7. Upload files to the bucket using the AWS S3 console, the AWS S3 CLI, or the AWS S3 SDK.  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/aws/aws-8.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/aws/aws-9.png">
</details>

8. Access your files through the AWS S3 Console, AWS S3 CLI, or the AWS S3 SDK.  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/aws/aws-10.png">
</details>  

### Stripe Endpoint

1. Register for a Stripe account at stripe.com
2. Log into your Stripe account and navigate to the Developers section  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/stripe/stripe-1.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/stripe/stripe-2.png">
</details>  

3. In the Developers section, locate the API keys section and take note of the publishable and secret keys  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/stripe/stripe-3.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/stripe/stripe-4.png">
</details> 

4. Create environment variables in your local environment and on Heroku, such as STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY, with the values of the publishable and secret keys  

5. Return to the Developers section of your Stripe account and click on the Webhooks tab  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/stripe/stripe-5.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/stripe/stripe-6.png">
</details> 

6. Create a webhook with the URL of your website, such as https://example.com/checkout/wh/  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/stripe/stripe-7.png"><br>
<img src="https://raw.githubusercontent.com/dmccaffrey01/CI_PP5_INFINITY_INNOVATIONS/main/docs/stripe/stripe-8.png">
</details> 

7. Choose the events you want to receive, such as payment_intent.payment_failed and payment_intent.succeeded  

8. Take note of the key generated for this webhook  

9. Create an environment variable, such as STRIPE_WH_SECRET, with the value of the webhook secret key on your local environment and Heroku  

10. Test the webhook to ensure it is working properly and troubleshoot any issues that may arise.  

### Fork Repository
To fork the repository by following these steps:
1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner
<hr>

### Clone Repository
You can clone the repository by following these steps:
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it 
3. Select if you prefere to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7.Press Enter to create your local clone.

##### Back to [top](#table-of-contents)<hr>

## Credits

### Code  
- Code Institute for the cart and checkout app as a basis for my checkout and basket apps
- Code Institute Slack community for guidance on many of my bug fixes.

### Media
[MidJourney](https://www.midjourney.com/)

### Chatbot
[Voiceflow](https://voiceflow.com/)

##### Back to [top](#table-of-contents)<hr>

## Acknowledgements

### Special thanks to the following:
- My Mentor Mo Shami for his excellent guidance and valuable advice 
- Code Institute Slack Community
- Code Institute Tutor Support
