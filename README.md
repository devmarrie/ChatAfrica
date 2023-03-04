# Chat Africa
This repository contains our end of foundations project called ChatAfrica which is a web-based chatbot application that allows one to know more about the African culture and its diversity.
First, we prepare the MySQL server for the project and create a database called chat_africa.

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

