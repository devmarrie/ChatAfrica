# Chat Africa
This repository contains our end of foundations project called **ChatAfrica** which is a web-based chatbot application that allows one to know more about the African culture and its diversity. The application uses GPT-3 to generate responses and renders it to the user in text format. Other resources used to train the data are found in the folder named [content](https://github.com/devmarrie/ChatAfrica/tree/master/content).

Additional **applications** and **dependencies** used are listed in the [requirement.txt](https://github.com/devmarrie/ChatAfrica/blob/master/requirements.txt) file. The [backend](https://github.com/devmarrie/ChatAfrica/tree/master/backend) folder houses all the tasks carried out at the backend level.

To set up the database, we prepare the MySQL server for the project and create a database called chat_africa.

```
# Run the following coomand and put your password to automate database creation then veiw if it is present.
cat setup_mysql_chat_africa.sql | mysql -hlocalhost -uroot -p
```


Environment variables will be your best friend for this project!

    HBNB_ENV: running environment. It can be “dev” or “test” for the moment (“production” soon!)
    HBNB_MYSQL_USER: the username of your MySQL
    HBNB_MYSQL_PWD: the password of your MySQL
    HBNB_MYSQL_HOST: the hostname of your MySQL
    HBNB_MYSQL_DB: the database name of your MySQL
    HBNB_TYPE_STORAGE: the type of storage used. It can be “file” (using FileStorage) or db (using DBStorage)


## Authors
Janeth Oluebube Eni - [Github](https://github.com/EninetJanice) / [Twitter](https://twitter.com/eninetjanice) / [LinkedIn](https://www.linkedin.com/in/janeth-eni-22a00b135)
Uchechukwu Samuel Ottah - [Github](https://github.com/coderboy-exe) / [Twitter](https://twitter.com/coderboy-exe) / [LinkedIn](https://www.linkedin.com/in/uchechukwu-ottah-92968a162)
Marriane Ojuang' - [Github](https://github.com/devmarrie) / [Twitter](https://twitter.com/devmarrie) / [LinkedIn](https://www.linkedin.com/in/marriane-akeyo)
                                
                               
