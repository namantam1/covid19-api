# covid19-api
This is an django rest framework by which we can get current status of corona cases in india, state and union territories wise along with their coordiantes.
The data is fetch from the official website https://www.mygov.in/covid-19.

## How this api works - 
when you send request this api then data is fetched from the website and a json object of data is created using web scaping and then it is send back as resonse. Beautifysoup is used for web scraping

## Installation and setup - 

clone this repositoy and then run the following commands to install required packages - 
``` bash
pip install -r requirements.txt
```
This will install all the required packages for this api. Now run the following commands to setup database

```bash


python3 manage.py makemigration
python3 manage.py migrate

```

Now everything is setted up. Its time to run the server and check if everything goes well - 

```bash
python3 manage.py runserver
```

 If server run successfully the everything went well. Now got to 127.0.0.1:8000/user and got to login page and login yourself if you have alredy created a superuser or go to register page 
 to register your self. Then after login go to features and create an authentication key.
 
 Now copy your key and send a get request to 127.0.0.1:8000/covid19 along with key as parameter and key name as **auth_token** to get the json response of covid 19 cases in india.
  
  Now if you are using a tool like curl the send the request as - 
  
  ```bash
  curl -X get http://127.0.0.1:8000/covid19?auth_token={{your_secret_key}}
 ```
 
Thats all.

## Bonus

This project is alredy live on heroku. So if you want to direct get the corona cases json in india the visit this link - http://covidapi121.herokuapp.com/user
