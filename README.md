# Awwward

A web application that rates uploaded projects.

## By Wilstan Onditi
A student at Moringa School and an aspiring software developer.


## Description
Awwards is a site where users can upload projects, they can view projects uploaded by other users, rate projects according to design, usability and content and the average rate is displayed for each.   

## Specifications
* Users can view projects
* Users can search projects
* Users can upload projects they have done
* Users can rate other projects based on design, content and usability
* Users can sign up and login in


### Behaviour-Driven Development
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| View Home | Click Home | Loads the home page with projects displayed |
| View User Profile  | view profile  | Profile page with users information |
| Visit actual site | Project url link | Actual project|
| Rate other projects | Ratings based on number | Result of the average rate|
## Setup and installations

#### Prerequisites
1. [Python3.6](https://www.python.org/downloads/)
2. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
3. [Pip](https://pip.pypa.io/en/stable/installing/)

#### Technologies used
   - Python 3.6
   - HTML
   - Bootstrap 4
   - Heroku
   - Postgresql
   - Django
## Application link
https://wil-awards.herokuapp.com/
#### Clone the Repo and rename it to suit your needs.
bash
git clone https://github.com/wilsenock220/award

#### Initialize git and add the remote repository
bash
git init
bash
git remote add origin <your-repository-url>

## Setup/Installation Requirements
Follow the following commands to run the project
* git clone/download ```https://github.com/wilsenock220/award.git```
* cd Awwwards
* Install required files in requirements.txt
* Run ```python3.6 manage.py runserver```
`

#### Create and activate the virtual environment
bash
python3.6 -m virtualenv virtual
bash
source virtual/bin/activate

#### Setting up environment variables
Create a .env file and paste paste the following filling where appropriate:
SECRET_KEY='342s(s(!hsjd998sde8$=o4$3m!(o+kce2^97kp6#ujhi'
DEBUG=True #set to false in production
DB_NAME='awards'
DB_USER='user'
DB_PASSWORD='password'
DB_HOST='127.0.0.1'
MODE='dev' #set to 'prod' in production
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1

#### Install dependancies
Install dependancies that will create an environment for the app to run
pip install -r requirements.txt#

## Support and contact details
In case of clarification email me at wilsenock220@gmail.com


#### Run chmod a+x start.py
bash
chmod a+x start.py

#### Run the app
bash
./start.sh
#### Access the application through localhost:5000
Open [localhost:8000](http://127.0.0.1:8000/)
## Contributing
Please read this [comprehensive guide](https://opensource.guide/how-to-contribute/) on how to contribute. Pull requests are welcome :slightly_smiling_face:
## Bugs
Create an issue mentioning the bug you have found
#### Known bugs
- N/A
## Support and contact details
Contact [Wilstan  Enock](wilsenock@gmail.com) for further help/support
### License
[MIT](https://github.com/wilsenock220/award/blob/master/LICENSE)
Copyright (c)2019 **Wilstan  Enock**