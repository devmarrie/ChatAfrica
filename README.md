# Chat Africa
This repository contains our end of foundations project called **ChatAfrica** which is a web-based chatbot application that allows one to know more about the African culture and its diversity. The application uses GPT-3 to generate responses and renders it to the user in text format. Other resources used to train the data are found in the folder named [content](https://github.com/devmarrie/ChatAfrica/tree/master/content).

# image 

Additional **applications** and **dependencies** used are listed in the [requirement.txt](https://github.com/devmarrie/ChatAfrica/blob/master/requirements.txt) file. The [backend](https://github.com/devmarrie/ChatAfrica/tree/master/backend) folder houses all the tasks carried out at the backend level.

## Installation
* Clone this repository: `git clone "https://github.com//devmarrie/ChatAfrica.git"`
* Access ChatAfrica directory: `cd ChatAfrica`

# File Description 
## Backend
It contains the endpoints connecting various parts of the application including the database, frontend and the GPT-3 api.
These endpoints are stored in the following files or folders:

#### `api`
This folder contains the following files:
**auth.py** - It contains the google authentication implementation and the login routes used by the user to login or signup and access various parts of the application.
Once the user logs in he/she is directed to the chat page.

**views.py** - contains an implementation of the chats, user and questions  routes. 

#### `chat_engine`
This folder contains the code implementation of how we trained the GPT-3 api with content exclusive to Africa and its connection with our backend.

**content** - this folder contains all the data we used to train our model.
**ask_ChatAfrica.py** - generates the responses to user's questions.
**construct_index.py** - constructs an index of text documents using GPT (Generative Pre-trained Transformer) models.
**index.json** - contains the data used to train gpt-3 continuously and test if it is working perfectly.

#### `models` 
It contains classes used for creating orms used to define the database tables of this project:
**base_model.py** - defines an abstract table which is inherited by all the other tables
**chat.py** - defines the chat table
**db_storage.py** - testing the database and bringing the tables to life.
**question.py** - used to create the question table in the database.
**response.py** - used to create the response table.
**user.py** - used to create the user table.
### static
#### `templates/` directory that contains the frontend files of this project
** setup_mysql_chat_africa.sql
** __init__.py

## Content
## Instance
## venv
## main.py:
This file is the entry point of our application. It starts the Flask application.

# Usage
landing
login
create room with image
Start chatting with image
logout

# Examples
"What is the capital of Kenya?"
"Got any creative ideas about Nigerian Afrobeats?"
"How do I go to Ghana from here?"

# Capabilities
Remembers what user said earlier in the conversation
Allows user to provide follow-up corrections
Trained to decline inappropriate requests

# Limitations
May occasionally generate incorrect information
May occasionally produce harmful instructions or biased content
Limited knowledge of world and events after 2022

# Featured Blog Posts

## Authors
Janeth Oluebube Eni - [Github](https://github.com/EninetJanice) / [Twitter](https://twitter.com/eninetjanice) / [LinkedIn](https://www.linkedin.com/in/janeth-eni-22a00b135)
Uchechukwu Samuel Ottah - [Github](https://github.com/coderboy-exe) / [Twitter](https://twitter.com/coderboy-exe) / [LinkedIn](https://www.linkedin.com/in/uchechukwu-ottah-92968a162)
Marriane Ojuang' - [Github](https://github.com/devmarrie) / [Twitter](https://twitter.com/devmarrie) / [LinkedIn](https://www.linkedin.com/in/marriane-akeyo)
                               
