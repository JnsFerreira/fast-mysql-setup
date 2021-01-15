# How to fast setup a MySQL + Python enviroment

Perhaps all of us , least once, need to setup a development eviroment in our machine. As we know, it can be a quite difficult and time consuming.

This repository will show you how to fast setup MySQL + Python enviroment using docker. I won't focust-on how docker works, so if you've some trouble to understand the steps, i advice you to check this [video](https://www.youtube.com/watch?v=3c-iBn73dDE&ab_channel=TechWorldwithNana).

Here we are using the tech stack mentioned above, but with this concepts, you can create a lot of solutions to your daily develoment process.

## Getting Started


### Installation

All the installation process was made with on Ubuntu (A linux based system, that you should use). For windows instalation of docker, please follow [this](https://docs.docker.com/docker-for-windows/install/) documentation
 

Open your terminal (CTRL+ALT+T) and type:


1. Installing docker

```
$ sudo apt-get install docker docker.io
```

2. Get your MySQL docker image

```
$ sudo docker pull mysql
```

**Tip**: You can get more docker images at [DockerHub](https://hub.docker.com/)

3. Check available images

```
$ sudo docker images
```

4. Create a container with MySQL image

```
$ sudo docker run -e MYSQL_ROOT_PASSWORD=dockerIsAwesome --name my_mysql_container  -p3001:3306 mysql
```

- `MYSQL_ROOT_PASSWORD` is the root password to access the database
- `--name` is the name of container. It can be useful to easily start and stop the container.
- `-p3001:3306` is the way to link the container port to a port on your computer. The basic syntax is `-p<container_port>:<local_port>`

We are done! Now, let's connect to this database using Python 3.

### Usage

1. Clone this repository to your computer

```
$ git clone https://github.com/JnsFerreira/fast-mysql-setup.git
```

2. Go to repo directory

```
$ cd fast-mysql-setup
```

3. Create a virtualenv 

```
$ virtualenv mysql_env
```

If you haven't virtualenv, install it with `pip3 install virtualenv`


4. Activate the enviroment

```
$ souce mysql_env/bin/activate
```

5. Install the requirements

```
$ pip3 install -r requirements.txt
```

6. Test the connection with MySQL Database

I already wrote a small class that makes the connection to the database.
You can implement new methods, such as executing queries, etc.

In the file `src/conn_example.py`, we have a small demonstration of how to consume the class, where you basically have to supply the connection information.

Edit the file, if needed

```
params = {'user': 'root',
          'password': 'dockerIsAwesome',
          'host': 'localhost',
          'port':'3001',
          'raise_on_warnings': True}
```
Now, just execute the python file

```
python3 src/conn_example.py
```

If the connection was successful, you will see somenthing like this:

```
<mysql.connector.connection_cext.CMySQLConnection object at 0x7f09f7de9d00>
```

Now, you're able to create tables, insert data, etc.


Last and not least, to stop your container at end of day:

```
$ sudo docker stop my_mysql_container
```

To start your work again:

```
$ sudo docker start my_mysql_container
```

Enjoy :)
