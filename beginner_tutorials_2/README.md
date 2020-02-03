
Beginner_tutorials_2
=====================
Cette activité consiste à executer une patrouille, à partir d'un fichier de configuration «config3. yaml » en format JSON contenant les différents points à atteindre. 


Environnements de travail
=========================
OS : Ubuntu 14.04 Trusty
ROS: Indigo


Démarrage
============

ATTENTION ! : Il faut copier les contenus de 2 dossier ( src/Act_2.py et config/config3.yaml ) respectivement dans les destinations suivantes :
 -beginner_tutorials/src
  
 -beginner_tutorials/config
            


Lancez Trois terminales :

1/- Au niveau de premier ,lancez le "Master" :
  roscore

2/-Au niveau de deuxime , executez les commandes suivantes :
   rosrun turtlesim turtlesim_node

3/-Au niveau de la troisieme :
   rosrun beginner_tutorials Act_2.py
