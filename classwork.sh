#!/bin/bash


adduser(){
echo "Tell me a user id to add"
read USER

echo "Tell me a password"
read PASS

echo "Tell me a group name"
read GROUP
useradd -p $PASS $USER 
usermod -aG $GROUP $USER
}
repeat='y'
while [ $repeat = 'y' ]
do 
    adduser
    echo "Do you want to create a new user"
    read repeat 
done 



                                 
