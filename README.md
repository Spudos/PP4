# PP4: Pure Drive Fitness

![Site Home Page](/static/document_images/multi_device.png)

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
4. As a **user** I can **view my booked sessions** so that I can **cancel if i need to or edit the session**
5. As a **user** I can **leave a comment as I book** so that I can **inform the trainer about my requirements**
6. As a **user** I can **receive booking emails** so that I can **get confirmation that it has been booked**

#### Blog

7. As a **user** I can **view all of the available blogs in a clear and simple layout** so that I can **find a blog a would like to read**
8. As a **user** I can **see a short excerpt from the blog** so that I can **understand what it is about**
9. As a **user** I can **read the blog** so that I can **learn about the subject**
10. As a **user** I can **like a blog** so that I can **give positive feedback on posts I enjoyed**
11. As a **user** I can **comment on a blog** so that **ask questions or leave useful information for other users**

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
- Ready, In Progress, Testing, Done headings were used in the Kanban

#### User Stories

<details><summary>User Account</summary>

![Account](/static/document_images/issues_account.png)
</details>

<details><summary>Blog</summary>

![Blog](/static/document_images/issues_blog.png)
</details>

<details><summary>Contact</summary>

![Contact](/static/document_images/issues_contact.png)
</details>

<details><summary>General</summary>

![General](/static/document_images/issues_general.png)
</details>

<details><summary>Session</summary>

![Session](/static/document_images/issues_session.png)
</details>

#### Kanban Board

<details><summary>Kanban examples at various stages of the project</summary>

Basic Welcome page complete, contact form in testing and session booking in progress
![Kanban_1](/static/document_images/kanban_1.png)

Session editing in testing and blog functions in progress
![Kanban_2](/static/document_images/kanban_2.png)

Comment and likes in testing, comment notifications and approval in progress
![Kanban_3](/static/document_images/kanban_3.png)

All work completed
![Kanban_4](/static/document_images/kanban_4.png)
</details>

##### Back to [top](#table-of-contents)<hr>

## Wireframes
Balsamiq is the tool that I commonly use to wireframe my projects.  It has the capability to quickly and easily draft website layouts on a multitude of representative platform sizes.  

<details><summary>Welcome</summary>  

![Welcome](/static/document_images/wf_welcome.png)
</details>

<details><summary>Blog</summary>  

Blog Preview
![Blog Preview](/static/document_images/wf_blog_listing.png)

Blog Detail
![Blog Detail](/static/document_images/wf_blog_detail.png)
</details>

<details><summary>Sessions</summary>  

Session Details
![Session Details](/static/document_images/wf_sessions.png)

Session Booking
![Session Booking](/static/document_images/wf_booking.png)
</details>

<details><summary>Contact Me</summary>  

![Contact Me](/static/document_images/wf_contact.png)
</details>

<details><summary>User Account</summary>  

![User Account](/static/document_images/wf_account.png)
</details>

##### Back to [top](#table-of-contents)<hr>

## Design

### Colors

The color scheme was chosen to provide a good contrast for accessibility whilst also being quite subtle.  The black for the header and social footer was given a transparency of 90% to make it less harsh.

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
  - No Sessions Available
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

This elegant solution allows cloud based storage to be used so the same DB can be used at all time.  This is especially useful during development as local and deployed versions can be tested with the same data saving time and aiding consistency of results.

<details><summary>ElephantSQL details</summary>

![ElephantSQL](/static/document_images/elephantsql.png)
</details>

##### Back to [top](#table-of-contents)<hr>

## Database

<details><summary>See Database Diagram</summary>

![ElephantSQL](/static/document_images/DB_diagram.png)
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
- The first section provides login/logout/sign up options
- The second section provides simple navigation with clear icons and hover functionality
- User stories covered: 12, 13

<details><summary>See feature images</summary>

![Header](/static/document_images/feature_header.png)
</details>

### Footer

- Featured on all pages
- There are 2 section, one for contact and location information and one for social media links
- User stories covered: 14, 16, 17, 18

<details><summary>See feature images</summary>

![Footer](/static/document_images/feature_footer.png)
</details>

### Welcome Page

- Main Landing page for the site
- Displays hero image
- Contains 3 main sections that link to the main functionality for each type - blogs, sessions and contact me
- User stories covered: 1, 7, 14

<details><summary>See feature images</summary>

Welcome Page Blog Section
![Welcome Blogs](/static/document_images/feature_welcome_blog.png)<br>
Welcome Page Session Section
![Welcome Sessions](/static/document_images/feature_welcome_sessions.png)<br>
Welcome Page Contact Section
![Welcome Contact](/static/document_images/feature_welcome_contact.png)

</details>

### Blog Listing

- Shows all the available blogs
- gives the option to like a blog if you are logged in
- User stories covered: 7, 8, 10

<details><summary>See feature images</summary>

![Blog Listing](/static/document_images/feature_blog_listing.png)
</details>

### Blog Detail

- Shows the blog detail
- Gives the option to comment on a blog if you are logged in
- User stories covered: 9, 11, 24

<details><summary>See feature images</summary>

![Blog Detail](/static/document_images/feature_blog_detail.png)
</details>

### Blog Comment Notification

- Alerts the admin that there are comments to be approved
- User stories covered: 26

<details><summary>See feature images</summary>

![Blog Comment Notification](/static/document_images/feature_notification.png)
</details>

### Session Detail

- Shows the user what sessions are available and detailed information about each session
- User stories covered: 2

<details><summary>See feature images</summary>

![Session Detail](/static/document_images/feature_session_detail.png)
</details>

### Session Booking

- Allows the user to book sessions and leave notes about the booking
- The user is emailed once a booking has been made
- A success screen is shown on booking, a failure screen is shown if no sessions are available
- User stories covered: 3, 5, 6, 21

<details><summary>See feature images</summary>

Booking Page
![Booking Page](/static/document_images/feature_booking.png)<br>
Booking Success
![Booking Success](/static/document_images/feature_booking_success.png)<br>
Booking Full
![Booking Full](/static/document_images/feature_booking_failure.png)
</details>

### Contact Me

- Allows the user to communicate with the site owner
- The site owner is emailed once a message has been sent
- A success screen is shown once sent
- User stories covered: 14, 15, 27

<details><summary>See feature images</summary>

Contact Me
![Contact Me](/static/document_images/feature_contact.png)<br>
Contact Success
![Contact Success](/static/document_images/feature_contact_success.png)
</details>

### User Account

- Allows the user see their details and bookings
- Allows the user to cancel and edit bookings
- User stories covered: 13, 4

<details><summary>See feature images</summary>

![Session Booking](/static/document_images/feature_account.png)
</details>

### Admin Section

- Allows the site owner to create/edit/destroy posts, sessions, appointments, users, bookings and comments
- User stories covered: 19, 20, 22, 23, 25

<details><summary>See example feature images</summary>

Admin Example 1
![Admin Example 1](/static/document_images/feature_admin_1.png)<br>
Admin Example 2
![Admin Example 2](/static/document_images/feature_admin_2.png)<br>
Admin Example 3
![Admin Example 3](/static/document_images/feature_admin_3.png)
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

- No Errors Found

### Booking Success

booking_success.html (source code copied into validator due to dynamic data)

- No Errors Found

### Booking Unavailable

booking_full.html [results](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpuredrivefitness-68f4e5eedb4f.herokuapp.com%2Fbooking%2Fbooking_form%2F%3Fsession_type%3DMotivation)

- No Errors Found

### Contact Me

contact.html [results](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpuredrivefitness-68f4e5eedb4f.herokuapp.com%2Fcontact%2F)

- No Errors Found

### Contact Success

success.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpuredrivefitness-68f4e5eedb4f.herokuapp.com%2Fsuccess%2F)

- No Errors Found

### Account Page

account.html  (source code copied into validator due to dynamic data)

- No Errors Found

##### Back to [top](#table-of-contents)

### CSS Validation
The W3C Jigsaw CSS Validation Service was used to validate the CSS of the website.

<details><summary>style.css</summary>

![style.css](/static/document_images/css_validation.png)
</details>

- No errors found

##### Back to [top](#table-of-contents)

### JavaScript Validation
JSHint javaScript Validation Service was used to validate all javaScript snippets.

<details><summary>base.html</summary>

![base.html](/static/document_images/js_base.png)
</details>

<details><summary>account.html</summary>

![user_account.html](/static/document_images/js_account.png)
</details>

- No errors found

##### Back to [top](#table-of-contents)<hr> 

## PEP8 Validation

[CI Python Linter](https://pep8ci.herokuapp.com/) was used to check the code for PEP8 requirements.  Screenshots for all of the major code components are included below.

### Blog App

<details><summary>admin.py</summary>

![admin.py](/static/document_images/pep8_blog_admin.png)
</details>

<details><summary>forms.py</summary>

![forms.py](/static/document_images/pep8_blog_forms.png)
</details>

<details><summary>models.py</summary>

![models.py](/static/document_images/pep8_blog_models.png)
</details>

<details><summary>tests.py</summary>

![tests.py](/static/document_images/pep8_blog_tests.png)
</details>

<details><summary>urls.py</summary>

![urls.py](/static/document_images/pep8_blog_urls.png)
</details>

<details><summary>views.py</summary>

![views.py](/static/document_images/pep8_blog_views.png)
</details>

### Booking App

<details><summary>admin.py</summary>

![admin.py](/static/document_images/pep8_book_admin.png)
</details>

<details><summary>forms.py</summary>

![forms.py](/static/document_images/pep8_book_forms.png)
</details>

<details><summary>models.py</summary>

![models.py](/static/document_images/pep8_book_models.png)
</details>

<details><summary>tests.py</summary>

![tests.py]()
</details>

<details><summary>urls.py</summary>

![urls.py](/static/document_images/pep8_book_urls.png)
</details>

<details><summary>views.py</summary>

![views.py](/static/document_images/pep8_book_views.png)
</details>

### Contact App

<details><summary>forms.py</summary>

![forms.py](/static/document_images/pep8_contact_forms.png)
</details>

<details><summary>tests.py</summary>

![tests.py](/static/document_images/pep8_contact_tests.png)
</details>

<details><summary>urls.py</summary>

![urls.py](/static/document_images/pep8_contact_urls.png)
</details>

<details><summary>views.py</summary>

![views.py](/static/document_images/pep8_contact_views.png)
</details>

### Welcome App

<details><summary>urls.py</summary>

![urls.py](/static/document_images/pep8_welcome_urls.png)
</details>

<details><summary>views.py</summary>

![views.py](/static/document_images/pep8_welcome_views.png)
</details>

### Puredrive App

<details><summary>settings.py</summary>

![settings.py](/static/document_images/pep8_puredrive_settings.png)
</details>

<details><summary>urls.py</summary>

![urls.py](/static/document_images/pep8_puredrive_urls.png)
</details>

<details><summary>manage.py</summary>

![manage.py](/static/document_images/pep8_puredrive_manage.png)
</details>

##### Back to [top](#table-of-contents)<hr> 

## Accessibility  
The [WAVE WebAIM web accessibility evaluation tool](https://wave.webaim.org/) was used to ensure key website pages met high accessibility standards.

- No errors found

welcome.html [results](https://wave.webaim.org/report#/https://puredrivefitness-68f4e5eedb4f.herokuapp.com/)

blog.html [results](https://wave.webaim.org/report#/https://puredrivefitness-68f4e5eedb4f.herokuapp.com/blog/)

blog_details [results](https://wave.webaim.org/report#/https://puredrivefitness-68f4e5eedb4f.herokuapp.com/blog/shopping-for-fitness/)

booking.html [results](https://wave.webaim.org/report#/https://puredrivefitness-68f4e5eedb4f.herokuapp.com/booking/)

contact.html [results](https://wave.webaim.org/report#/https://puredrivefitness-68f4e5eedb4f.herokuapp.com/contact/)

contact success [results](https://wave.webaim.org/report#/https://puredrivefitness-68f4e5eedb4f.herokuapp.com/success/)

##### Back to [top](#table-of-contents)<hr> 

## Lighthouse

Page Performance was tested using Lighthouse, all pages achieved a score of at least 95.

<details><summary>welcome.html</summary>

![welcome.html](/static/document_images/lh_welcome.png)
</details>

<details><summary>blog.html</summary>

![blog.html](/static/document_images/lh_blog.png)
</details>

<details><summary>blog_detail.html</summary>

![blog_detail.html](/static/document_images/lh_blog_detail.png)
</details>

<details><summary>booking.html</summary>

![booking.html](/static/document_images/lh_booking.png)
</details>

<details><summary>booking_form.html</summary>

![booking_form.html](/static/document_images/lh_booking_form.png)
</details>

<details><summary>booking_success.html</summary>

![booking_success.html](/static/document_images/lh_booking_success.png)
</details>

<details><summary>booking_full.html</summary>

![booking_full.html](/static/document_images/lh_booking_full.png)
</details>

<details><summary>contact.html</summary>

![contact.html](/static/document_images/lh_contact.png)
</details>

<details><summary>contact_success.html</summary>

![contact_success.html](/static/document_images/lh_success.png)
</details>

<details><summary>user_account.html</summary>

![user_account.html](/static/document_images/lh_account.png)
</details>

##### Back to [top](#table-of-contents)<hr> 

## Testing

1. Manual testing User Stories
2. Automated testing

### Manual testing

1. As a **user** I can **see the session types on the welcome page** so that I can **see headline information about the sessions**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Welcome Page | On the welcome page scroll down to the section below the blog section and you will see session types with brief descriptions | The user can see the session types | As expected |

2. As a **user** I can **read detail about the session types that are available** so that **I understand what is best for me**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Session Detail | From the welcome page either click the 'let's meet' button below the session section or click 'meet' in the nav bar | Detail for each available session type is listed | As expected |

3. As a **user** I can **book a session** so that I can **begin my training**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Session Booking | First you must log in then navigate to the session detail page.  Once you have navigated to the session detail page clicking on the session test will take you to a booking form if any sessions are available | A booking page is displayed | As expected |

4. As a **user** I can **view my booked sessions** so that I can **cancel if i need to or edit the session**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| User Account | When logged in click on 'Me' in the nav bar.  Scroll down to see the booked session detail below user information and cancel or edit as required.  A email will be sent if a booking is changed. | All upcoming and past session are displayed and edit/cancel functionality exists | As expected |

5. As a **user** I can **leave a comment as I book** so that I can **inform the trainer about my requirements**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Session Booking | When on the booking form a text box is provided to leave any comments on the booking | The text box is displayed for free form notes | As expected |

6. As a **user** I can **receive booking emails** so that I can **get confirmation that it has been booked**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Session Booking | Once you have successfully made a booking via the booking form you receive an email giving you details of the session you have booked | An email with relevant information is sent to the user | As expected |

7. As a **user** I can **view all of the available blogs in a clear and simple layout** so that I can **find a blog a would like to read**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Welcome Page | The first section below the header on the welcome page displays the most recent blog posts. Click on 'let's read' or 'Read' from the nav bar to view the blog listing| A blog listing is shown | As expected |
| Blog Listing | Once you have navigated to the blog listing all blogs are shown in a paginated view so that a selection can be made | The blog listing is displayed, 4 at a time | As expected |

8. As a **user** I can **see a short excerpt from the blog** so that I can **understand what it is about**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Blog Listing | Navigate to the blog listing page.  Each post shows a short excerpt from the post | An excerpt is shown | As expected |

9. As a **user** I can **read the blog** so that I can **learn about the subject**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Blog Detail | From the blog listing you can click on the post to view the full blog post | The blog post is displayed in an easy to read format | As expected |

10. As a **user** I can **like a blog** so that I can **give positive feedback on posts I enjoyed**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Blog Listing | You mst be logged in to access this functionality.  Navigate to the blog listing page, once there click on the thumbs up icon to like a page.  Clicking again removes the like from the post. | 'Likes' are displayed and the user can add their approval | As expected |

11. As a **user** I can **comment on a blog** so that **ask questions or leave useful information for other users**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Blog Listing | You mst be logged in to access this functionality.  Navigate to the blog listing page, once there click a blog to see the full blog.  Scroll to the bottom to the comment section and a dd a comment.  A notification will show that your comment is awaiting approval.  Further comments cannot be added until your comment is approved. | Full comment functionality is available | As expected |

12. As a **user** I can **easily navigate the website** so that I can **find the information I am looking for**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Header | The nav bar is shown on all pages and gives easy to nav buttons | Navigation is provided | As expected |

13. As a **user** I can **log in securely to my account** so that I can **view my details**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Header | From the first header section buttons for login/signup/logout are shown as appropriate | The user can log into their account | As expected |
| User Account | When logged in click on 'Me' in the nav bar to view your details | User details are shown | As expected |

14. As a **user** I can **see contact information for the trainer** so that I can **get in touch as required**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Footer | Scroll to the bottom of any page, full contact details are displayed | All contact details are given | As expected |
| Contact Me | Scroll down the home page to the contact section and click on 'Let's talk' or from the nav bar click on 'Talk' to go to the contact page where full contact details are given as well as a option to send a message to the site owner | Multiple contact details are provided | As expected |

15. As a **user** I can **send a message to the trainer** so that I **ask questions if I want to**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Contact Me | Scroll down the home page to the contact section and click on 'Let's talk' or from the nav bar click on 'Talk' to go to the contact page where the option to send a message to the site owner | A validated messaging form is provided | As expected |

16. As a **user** I can **see location information for the trainer** so that I **know where to go for sessions**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Footer | Scroll to the bottom of any page, address details and a google map are provided | Location details are easy to find | As expected |

17. As a **user** I can **find the trainers social media accounts** so that I **follow their accounts**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Footer | Scroll to the bottom of any page, in the bottom footer section links to the site owners social media accounts are displayed | All social media accounts are linked to the site | As expected |

18. As a **site admin** I can **display a welcoming home screen** so that **users will want to see the sessions and blogs I offer**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Welcome Page | The home page has clear and consistent styling and shows blog, session and contact information | A detailed welcome page is shown | As expected |

19. As a **site admin** I can **create, delete, and edit sessions** so that **I can tailor the information available to users**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Admin Section | append /admin to the root web address and log in as a superuser.  Click on 'sessions' from the left menu and use the intuitive interface to perform the desired option | Full CRUD functionality is available | As expected |

20. As a **site admin** I can **add diary entries** so that **users can book sessions**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Admin Section | append /admin to the root web address and log in as a superuser.  Click on 'appointments' from the left menu and use the intuitive interface to perform the desired option | Full CRUD functionality is available  | As expected |

21. As a **site admin** I can **receive booking emails** so that **I am informed when users book with me**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Session Booking | When a booking is made an email is sent to the site owner to inform them about the booking | An email is received by the site owner | As expected |

22. As a **site admin** I can **create, delete, and edit blogs** so that **I can produce new blog content and maintain it as needed**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Admin Section | append /admin to the root web address and log in as a superuser.  Click on 'posts' from the left menu and use the intuitive interface to perform the desired option | Full CRUD functionality is available  | As expected |

23. As a **site admin** I can **add blogs in a draft state** so that **they are only public when I want them to be**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Admin Section | append /admin to the root web address and log in as a superuser.  Click on 'posts' from the left menu.  When you edit or create a post you can toggle its state between draft and published | A post can be put in a draft or published state | As expected |

24. As a **site admin** I can **allow users to comment on blog posts** so that **they can engage with the post**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Blog Listing | A user mst be logged in to access this functionality.  They navigate to the blog listing page, once there they click a blog to see the full blog.  They scroll to the bottom to the comment section and add a comment.  A notification will appear on the homepage to inform you a comment is awaiting approval. | Full comment functionality is available | As expected |

25. As a **site admin** I can **approve comments** so that **ensure that only appropriate comments are published**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Admin Section | Log in to admin and select 'comments' from the left menu.  Any comments that are not approved will be indicated as such.  Click on a comment to alter its state to approved. | Full comment functionality is available | As expected |

26. As a **site admin** I can **get comment notifications** so that **I am aware when a comment needs to be approved**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Blog Comment Notification | When a comment has been submitted a notification will appear on the homepage to inform you a comment is awaiting approval. Log in to admin and follow the procedure for comment approval. | Unapproved comment notifications are provided | As expected |

27. As a **site admin** I can **receive questions and comments submitted from my contact page** so that I can **answer user queries**

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Contact Me | When a user submits a message via the contact me form an email is sent to the site owner with details of the user and their message | An email is received by the site user with all relevant details | As expected |

##### Back to [top](#table-of-contents)<hr> 

### Automated testing

- Testing was done using the built in Django module, unittest.  The focus of texting was the view files for each module.  Testing these elements helps ensure that all business logic is being correctly applied.
- All tests passed

#### Blog

<details><summary> See summary</summary>

![blog](/static/document_images/tests_blog.png)
</details>

#### Booking

<details><summary> See summary</summary>

![blog](/static/document_images/tests_booking.png)
</details>

#### Contact

<details><summary> See summary</summary>

![contact](/static/document_images/tests_contact.png)
</details>

#### Welcome

<details><summary> See summary</summary>

![welcome](/static/document_images/tests_welcome.png)
</details>

### Device Testing & Browser compatibility

The website was tested on the these browsers:

- Google Chrome
- Apple Safari
- Mozilla Firefox

The website was tested on the these devices:

- Macbook Pro
- Windows PC with a variety of monitor sizes
- Ipad air
- Iphone 12

In addition, using chrome dev tools, the website was checked to ensure that it was fully responsive from a width of 320px upwards.

No issues were identified during these tests.

##### Back to [top](#table-of-contents)<hr> 

## Bugs

All bugs identified were fixed during development

##### Back to [top](#table-of-contents)<hr>

## Deployment

### Heroku Deployment

[Official Page](https://devcenter.heroku.com/articles/git) (Ctrl + click)

This application has been deployed from GitHub to Heroku. A guide to deploying to Heroku can be found [here](https://devcenter.heroku.com/articles/github-integration)
Here are the steps to deployment

- Login or create an account at [Heroku](https://dashboard.heroku.com/)

<details><summary> See images</summary>

![deploy_1](/static/document_images/deploy_1.png)
</details>

- Click on New > Create new app in the top right of the screen.

- Add an app name and select location, then click 'create app'.

<details><summary> See images</summary>

![deploy_2](/static/document_images/deploy_2.png)
</details>

- Under the deploy tab of the next page, select connect to GitHub.

- Log in to your GitHub account when prompted.

- Select the repository that you want to be connected to the Heroku app.

<details><summary> See images</summary>

![deploy_3](/static/document_images/deploy_3.png)
</details>

- Click on the settings tab.

<details><summary> See images</summary>

![deploy_4](/static/document_images/deploy_4.png)
</details>

- Scroll down to the config vars section, and add 4 config vars:
    1. Key: CLOUDINARY_URL Value: API details for your Cloudinary account
    2. Key: DATABASE_URL Value: API details for your ElephantSWL account
    3. Key: EMAIL_API_KEY Value: API details for your email provider
    4. Key: SECRET KEY Value: The secret key you generated
  
  All of these details are stored in the env.py in your application files.

- Navigate to the deploy tab.

- Select automatic deploys to allow Heroku to build the site with new changes each time changes are pushed to GitHub.

- In the 'manual deploy' section beneath this, make sure the branch selected is 'main' and click deploy branch.

<details><summary> See images</summary>

![deploy_5](/static/document_images/deploy_5.png)
</details>

<hr>

### Clone Repository

You can clone the repository by following these steps:

1. Go to the GitHub repository
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone.

##### Back to [top](#table-of-contents)<hr>

## Credits

### Code  

- Code Institute for the blog app as a basis for my blog app

### Media

- Sam Pierce agreed to create the blue/orange images for the site and the hero image
[Sam Pierce](https://www.sampiercephotography.com/)

### Text Content

- You.com was used to generate most of the text blocks on the site.
[you.com](https://www.you.com/)

##### Back to [top](#table-of-contents)<hr>

## Acknowledgements

### Special thanks to the following:
- My Mentor Mo Shami for his excellent guidance and valuable advice 
- Code Institute Slack Community
