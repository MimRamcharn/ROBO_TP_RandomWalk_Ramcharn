# ROBO_TP_RandomWalk_Ramcharn

# Random Walk

## But du projet
Réaliser une random walk dans un espace restreint et de le visualiser dans RVIZ.

## Pour l'utiliser, il faut cloner ce repertoire git sur votre terminal en faisant : 
```sh
git clone https://github.com/MimRamcharn/ROBO_TP_RandomWalk_Ramcharn.git

```
## Comment utiliser?
Créer un marker et l'afficher dans RVIZ - 
Il faudra tout d'abord faire ```source "chemin vers le le fichier setup.bash"```. Donner les droits exécution du noeud publish_marker.py en faisant ```chmod u+x publish_marker.py```.
Sur un autre terminal, apres le source du fichier setup.bash, faire un ```roscore```.
Sur un nouveau terminal, sourcer le fichier setup.bash et faire ```rosrun marker_visualizer publish_marker.py```
Et finalement, sur un dernier terminal faire ```rosrun rviz rviz```. Cela ouvrera une application ```RViz```. Choisir map pour fixed frame, cliquer sur Add-By topic-(le nom du marker): /marker_test-et l'objet: Marker et cliquer sur OK.
RViz nous affiche le sphere.
