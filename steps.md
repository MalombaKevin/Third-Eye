# Instructions
### A user should be able to:
+ Sign in with the application to start using. (done)
+ Set up a profile about me and a general location and my neighborhood name.
+ Find a list of different businesses in my neighborhood.
+ Find Contact Information for the health department and Police authorities near my neighborhood.
+ Create Posts that will be visible to everyone in my neighborhood.*
+ Change My neighborhood when I decide to move out. *
+ Only view details of a single neighborhood. *

# Classes

# Neighborhood class
+ Neighbourhood Name
+ Neighborhood location
+ Occupants Count
+ Admin Foreign key

#### methods
create_neigborhood()
delete_neigborhood()
find_neigborhood(neigborhood_id)
update_neighborhood()
update_occupants()
<hr>

# User class
+ name.
+ id.
+ neighborhood id foreign key
+ email address

<hr>

# Business Class
+ Business name
+ User foreign key
+ neighborhood id foreign key
+ Business email address.

### methods
create_business()
delete_business()
find_business(business_id)
update_business()
<hr>

# Features
+ business search
+ admin dashboard
+ authentication
+ deployment to heroku
<hr>

# Steps
+ Create and activate virtual evironment
+ create a requirements.txt file, add dependencies and install them
+ create a .gitignore file, add .env file to it
+ Generate django-project
+ run server
+ Generate django-app
+ adds .env file and setup database
+ update prpject setting files
+ setup database
+ create templates folder and add templates; index.html
+ create a view function to render to template
+ create a urls.py file and add the urls
+ connect the urls of the app to the project urls.py
+ run server to confirm if the paths are working
+ create a static folder to hold images/css and js
+ create a navigation bar template
+ create an authentification system (Login/logout/signup)
+ create models for the database
+ make migrations
+ work on the user interface
+ retrieval of data from database (neighborhood, business, user)
+ deployment to heroku
+ Add license
+ Add readme


