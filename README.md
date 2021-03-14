# Ciberc
 CiberC test

## Instalation

### Install dependencies
```console
pip install -r requirements.txt
```
### Create .env file
Create a file with _.env_ name in the main folder
<br/>

├─── inventory <br/>
├─── main <br/>
│ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─── _**.env**_ <br/>
├─── uploads <br/>
└─── excel_test.xlsb <br/>

This file must to have DEBUG, SECRET_KEY and DATABASE_URL like this.
```
DEBUG=<on/off>
SECRET_KEY=<your_secret_key
DATABASE_URL=mysql://<user>:<password>@<your_database_host>:<your_port>/<your_database_name>
```
For example:
```
DEBUG=on
SECRET_KEY=b^mnet94t_w&%_xe1jwkzk-0hf9m#ne)0g7ksh=g1i63b0y=vl
DATABASE_URL=mysql://root:@127.0.0.1:3306/ciberc
```
### Migrate
Only one step left.
```console
python manage.py migrate
python manage.py runserver
```

## Test
You need create a super user.
```
python manage.py createsuperuser
```
And type a username, email and password. Ready? Now go to localhost or your domain and introduce your username and password. 
<br/><br/>
I maked for you a excel of test in the project root. You can test the functionality with it. Its name is _**[/excel_test.xlsb](excel_test.xlsb)**_   
