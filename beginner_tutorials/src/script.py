#!/usr/bin/env python
# -*-coding:Latin-1 -*
#importation des bibliotheques 
import rospy
from geometry_msgs.msg import Twist
import sys  
# definir une fonction move

def move():                               
     Vitesse= input("Saisir la vitesse:")    # demander à l'utilisateur de saisir une valeur
     Vitesse_max=rospy.get_param("vitesse_max") # importer le parametre vitesse_max de fichier configuration.yaml
     Vitesse_min=rospy.get_param("vitesse_min") # importer le parametre vitesse_min de meme fichier 
     if (Vitesse > Vitesse_max): # si la valeur saisie depasse le vitesse maximal
       print("valeur de vitesse depasse le max !")
       sys.exit() # stop de script 
     elif (Vitesse < Vitesse_min): # si la valeur saisie inferieur au VMin
       print("valeur saisie est inferieur au VM !")
       sys.exit()
     else :
      rospy.init_node('keyboard', anonymous=True)  #creation d'un noeud
      velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) # publication de noeud sur le topic turtle1/cmd_vel
      rate = rospy.Rate(10); # frequence
      vel_msg = Twist()  # appel au fct Twist() pour definir la structure de msg (geometry_msg: linear , angular)
      vel_msg.linear.x=Vitesse # attribuer la vitesse  au point de mvt sur l'axe X   
      vel_msg.linear.y=0     
      vel_msg.linear.z=0
      vel_msg.angular.x = 0
      vel_msg.angular.y = 0
      while not rospy.is_shutdown(): # tant que le noeud est n'est pas interrompu      
       velocity_publisher.publish(vel_msg) #publication de nouveau msg
       #sys.exit() 
       rate.sleep() # temps de pause avant de lancer une autre tentative
          
if __name__ == '__main__': # main
  try:
   move()  # appel de fct move()
  except rospy.ROSInterruptException:  # interruption ave Ctrl+C     
     pass     
