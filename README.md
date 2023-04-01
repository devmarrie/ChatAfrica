# Chat Africa
This repository contains our end of foundations project called **ChatAfrica** which is a web-based chatbot application that allows one to know more about the African culture and its diversity. The application uses GPT-3 to generate responses and renders it to the user in text format. Other resources used to train the data are found in the folder named [content](https://github.com/devmarrie/ChatAfrica/tree/master/content).

Additional **applications** and **dependencies** used are listed in the [requirement.txt](https://github.com/devmarrie/ChatAfrica/blob/master/requirements.txt) file. The [backend](https://github.com/devmarrie/ChatAfrica/tree/master/backend) folder houses all the tasks carried out at the backend level.

# Overview


https://user-images.githubusercontent.com/71446962/223570647-06a146eb-8e5e-41f8-9312-d5b53f25a8af.mp4


## Installation
* Clone this repository: `git clone "https://github.com//devmarrie/ChatAfrica.git"`
* Access ChatAfrica directory: `cd ChatAfrica`

# File Description 
## [Backend](https://github.com/devmarrie/ChatAfrica/tree/master/backend)
It contains the endpoints connecting various parts of the application including the database, frontend and the GPT-3 api.
These endpoints are stored in the following files or folders:

#### [`api`](https://github.com/devmarrie/ChatAfrica/tree/master/backend/api)
This folder contains the following files:

- [**auth.py**](https://github.com/devmarrie/ChatAfrica/tree/master/backend/api/auth.py) - It contains the google authentication implementation and the login routes used by the user to login or signup and access various parts of the application.
Once the user logs in he/she is directed to the chat page.

- [**views.py**](https://github.com/devmarrie/ChatAfrica/tree/master/backend/api/views.py) - contains an implementation of the chats, user and questions  routes. 

#### [`chat_engine`](https://github.com/devmarrie/ChatAfrica/tree/master/backend/chat_engine)
This folder contains the code implementation of how we trained the GPT-3 api with content exclusive to Africa and its connection with our backend.

- [**content**](https://github.com/devmarrie/ChatAfrica/tree/master/backend/chat_engine/content) - this folder contains all the data we used to train our model.
- [**ask_ChatAfrica.py** ](https://github.com/devmarrie/ChatAfrica/tree/master/backend/chat_engine/ask_ChatAfrica.py)- generates the responses to user's questions.
- [**construct_index.py**](https://github.com/devmarrie/ChatAfrica/tree/master/backend/chat_engine/construct_index.py) - constructs an index of text documents using GPT (Generative Pre-trained Transformer) models.
- [**index.json**](https://github.com/devmarrie/ChatAfrica/tree/master/backend/chat_engine/indx.json) - contains the data used to train gpt-3 continuously and test if it is working perfectly.

#### [`models`](https://github.com/devmarrie/ChatAfrica/tree/master/backend/models) 
It contains classes used for creating orms used to define the database tables of this project:
- [**base_model.py**](https://github.com/devmarrie/ChatAfrica/tree/master/backend/models/base_model.py) - defines an abstract table which is inherited by all the other tables
- [**chat.py**](https://github.com/devmarrie/ChatAfrica/tree/master/backend/models/chat.py) - defines the chat table
- [**db_storage.py**](https://github.com/devmarrie/ChatAfrica/tree/master/backend/models/db_storage.py) - testing the database and bringing the tables to life.
- [**question.py**](https://github.com/devmarrie/ChatAfrica/tree/master/backend/models/question.py) - used to create the question table in the database.
- [**response.py**](https://github.com/devmarrie/ChatAfrica/tree/master/backend/models/response.py) - used to create the response table.
- [**user.py**](https://github.com/devmarrie/ChatAfrica/tree/master/backend/models/user.py) - used to create the user table.
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
From the home page, click on the **login button** to either sign up or sign in to use the ChatAfrica application. Sign up & sign in is very easy as it is automated with Google authentication (You don't need to stress in imputing your name, password or the likes :) ).
![room](https://user-images.githubusercontent.com/71446962/223571854-b8038c50-d0cb-43d1-b173-cd50434933dd.png)

After successful login, input a room name in the container. The name could be anything; a nickname, a question, an expression, etc. Then click on **create** to create a room and begin your conversation with ChatAfrica.

![Chat room and chat history](https://user-images.githubusercontent.com/71446962/223572097-b24567f9-9dc7-4674-97fc-00fe460ab316.png)

ChatAfrica has the ability of retaining your conversation with it. Once you are done, click on the **logout** button to exit the room. You can always log back in, select your created room and view your conversations with the bot. Alternatively, you can continue your chat or create a new room to start another conversation with ChatAfrica.

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
- Janeth Oluebube Eni - [Github](https://github.com/EninetJanice) / [Twitter](https://twitter.com/eninetjanice) / [LinkedIn](https://www.linkedin.com/in/janeth-eni-22a00b135)
- Uchechukwu Samuel Ottah - [Github](https://github.com/coderboy-exe) / [Twitter](https://twitter.com/coderboy-exe) / [LinkedIn](https://www.linkedin.com/in/uchechukwu-ottah-92968a162)
- Marriane Ojuang' - [Github](https://github.com/devmarrie) / [Twitter](https://twitter.com/devmarrie) / [LinkedIn](https://www.linkedin.com/in/marriane-akeyo)
                               
