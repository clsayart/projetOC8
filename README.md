# LitReview project
## __*book reviews*__
___
___
### Description
___
This application allows you to share opinions on literary works. 

It is possible to create a user account to access the application and then request reviews. 

Finally, it is also possible to share reviews and respond to requests for reviews from people to whom the user is subscribed. 

It is possible to subscribe to a user by entering their username.

## Prérequis : 
[![made-with-python](
https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](
https://www.python.org/)
[![Python badge](https://img.shields.io/badge/Python->=3.9.9-blue.svg)](
https://www.python.org/)
***
## Environnement Virtuel :
création de l'environnement virtuel
```shell
python3 -m venv [nom_de_votre_environnement_virtuel] 
```
activation de l'environnement virtuel
### Mac/Linux
````shell
source [nom_de_votre_environnement_virtuel]/bin/activate
````
### Windows
````shell
[nom_de_votre_environnement_virtuel]\Scripts\activate
````

---
After that, install the requirement.txt with using this command : `pip install -r requirements.txt`

Then, go to the project folder, named litreview, and run the following command: 

---
    ../litreview> py manage.py runserver
---

It will be start the server to this address : [127.0.0.1:8080](http://127.0.0.1:8080)

#### _* Login view *_
___
This is the page that is displayed as long as no user is logged in. 

From this page you can : 
- Create a new account
- Log in with an existing account. 


___
#### _* Create new account *_
___

If you click the button `s'inscrire`, a new page is displayed, allowing you to create a new user account.
You can then enter a user name, a password and a confirmation password. 

If the username is already in use, the password is not complex enough and/or the password and its confirmation do not 
match, an error message is displayed. 

In the opposite case, a message displays the success of the account creation, and you can return to the login 
page to log in.
___
#### _* Home view - Flow_*
___

On login, the first page that appears is the `Flux` page. 

In the navigation bar, you can go to the pages `Flux`, `Posts`, `Abonnements`. You can also click on 
your username to change your password, and click on `Déconnexion` to log out.

On this page appear : 
- your tickets and reviews 
- the tickets and reviews of people you follow
- a `Demander une critique` button
- a `Créer une critique` button

On your tickets and those of the people you follow, if no reviews have been posted, you can post a review by clicking on
the `Créer une critique` button.
1. New ticket view

When you click on the `Demander une critique` button, a new page ticket create is displayed 

You must then fill in a Title, a Description and you can also upload an image to illustrate your review request. 
Once you have completed the form, click on the `Envoyer` button to post your request.

You will then be directly redirected to the `Posts` page, which allows you to manage your publications 
2. New review view

When you click on the `Créer une critique` button, a new page review create is displayed 

You must then fill in a Title, a Description and you can also upload an image to illustrate your review request. 
And after, you have to give a rate, with a Headline and a comment for publish your review.

Once you have completed the form, click on the `Envoyer` button to post your request.

You will then be directly redirected to the `Posts` page, which allows you to manage your publications 

3. New review on an existing ticket

When you click on the `Créer une critique` button, a new page review create is displayed 

The ticket is displayed before the review form.
You have to give a rate, with a Headline and a comment for publish your review.

Once you have completed the form, click on the `Envoyer` button to post your request.

You will then be directly redirected to the `Posts` page, which allows you to manage your publications 

___
#### _* Posts view_*
___
This page allows you to see the publications you have made. 

All the reviews and tickets you have written. 
You can edit or delete any post you have made. 

_*Please note that if you delete a ticket, the related review will automatically be deleted with it.*_

1. Change Ticket

When you click on the button `Modifier Ticket`, a page with a ticket form opens, the form is pre-filled.  
Once you have made your changes, click on the `Envoyer` 
button to save your changes. You will be redirected to your posts page.

2. Change Review

When you click on the button `Modifier Critique`, a page with a review form opens, the form is pre-filled.  
Once you have made your changes, click on the `Envoyer` 
button to save your changes. You will be redirected to your posts page.

3. Delete Ticket / review

When you click on the `Supprimer Critique / Supprimer Ticket` button, a popup asks for confirmation of deletion. 
If you accept, the ticket/critique will be deleted from the database.

___
#### _* Subscription view_*
___
The page `Abonnements`allows you to manage your subscriptions. You can see which users are subscribed to you, 
see which users you follow, and add new user following.

1. New user follow

You can subscribe to a new user by entering their username. Please note that this is case sensitive. 
Once you have entered the username, click on the `Envoyer` button to subscribe. If the username does not exist, or if you
have already subscribed to that user, a message will inform you.

2. User followed by you

All users to whom you are subscribed appear here. You can unsubscribe by clicking on the `Supprimer` button.  
A confirmation popup will appear to prevent accidental deletion.

3. User following you

All users who follow you appear here. 