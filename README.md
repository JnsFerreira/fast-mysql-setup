# How to fast setup a MySQL + Python enviroment

Perhaps all of us , least once, need to setup a development eviroment in our machine. As we know, it can be a quite difficult and time consuming.

This repository will show you how to fast setup MySQL + Python enviroment using docker. I won't focust-on how docker works, so if you've some trouble to understand the steps, i advice you to check this [video](https://www.youtube.com/watch?v=3c-iBn73dDE&ab_channel=TechWorldwithNana).

Here we are using the tech stack mentioned above, but with this concepts, you can create a lot of solutions to your daily develoment process.

## Getting Started


### Instalation

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

**Tip**: You can get more docker images at [DockerHub]()

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
- `-p3001:3306` is the way to link the container port to a port on your computer. the basic syntax is `-p<container_port>:<local_port>`

We are done! Now, let's connect to this database using Python 3.

### Usage



