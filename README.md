# <h1>système de contrôle d'accès</h1>


<br>
<p>
Nous allons essayer dans ce projet de concevoir et réaliser un système de détection et reconnaissance d’objet en temps réel.<br>
Dans ce cadre, nous projetons dans une première étape de se familiariser avec des nouveaux concepts tels que :<br>
<ul>
<li> Le Deep Learning ou l’apprentissage profond.</li>
<li>Les réseaux de neurones artificiels classique (ANN) et réseaux de neurones convolutive (CNN) et leurs impacts sur l’amélioration des
    performances de la reconnaissance d’objets.</li>
<li>Le Transfer Learning, en vue d’utiliser un modelé pré-entrainé pour l’adapter à notre tâche cible).</li> </ul> 
</p>
NB:Vous pouvez me contacter par email pour envoyer la première partie<br> 

<p>
Dans une deuxième étape pratique le travail demandé consiste à :<br>
<ul>
<li>Adapter (ré-entraîner) un modèle d’apprentissage automatique</li> 
      - Détection et reconnaissance de visage à l’entrée de l’établissement pour les personnes.<br>
      - Détection et reconnaissance du logo de faculté pour les voitures.<br>
<li>Déployer le modèle obtenu sur une application web et sur un système embarqué (Raspberry) </li>
</p>
<h3>1. Détection et reconnaissance de logo</h3>
<p aligne="center">
<img src="https://github.com/Y0unes17/systeme-de-contr-le-d-acces/blob/master/D%C3%A9tection%20et%20reconnaissance%20de%20logo/images/Capture.PNG?raw=true" width="480" higth="480" />
<img src="https://github.com/Y0unes17/systeme-de-contr-le-d-acces/blob/master/D%C3%A9tection%20et%20reconnaissance%20de%20logo/images/Capture9849.PNG?raw=true" width="480" higth="480" />
</p>
<p>
la présence d’un véhicule devant la barrière sera détectée automatiquement par la raspberry plus clairement la cam et la raspberry sont <br>
connectées entre elles de façon que Stream de la cam il est présent dans la raspberry.On arriver alors à la partie intelligente,<br>
le raspberry sera détecte la présence de la logo FSM ou non
<ul><li> Si le cas (logo FSM sur la vitre de véhicule) alors le mouvement mécanique sera effectué (ouverture de barrière)</li>
<li>Si non (logo FSM n’existe pas sur la vitre de véhicule) le trafic n’est pas disponible etaucun mouvement de barrière ne sera effectué.</li>
</p>
<p align="center">
<img src="https://github.com/Y0unes17/systeme-de-contr-le-d-acces/blob/master/D%C3%A9tection%20et%20reconnaissance%20de%20logo/images/20200603_124159.jpg?raw=true" width="200" higth="200" />
<img src="https://github.com/Y0unes17/systeme-de-contr-le-d-acces/blob/master/D%C3%A9tection%20et%20reconnaissance%20de%20logo/images/20200603_130900.jpg?raw=true" width="200" higth="200" />
<img src="https://github.com/Y0unes17/systeme-de-contr-le-d-acces/blob/master/D%C3%A9tection%20et%20reconnaissance%20de%20logo/images/20200603_130918.jpg?raw=true" width="200" higth="200" />
<img src="https://github.com/Y0unes17/systeme-de-contr-le-d-acces/blob/master/D%C3%A9tection%20et%20reconnaissance%20de%20logo/images/20200603_131203.jpg?raw=true" width="332" higth="400" />
</p>

<p>
<h3>2. Détection et reconnaissance faciale </h3>
<p align ="center">
<img src="https://github.com/Y0unes17/systeme-de-contr-le-d-acces/blob/master/D%C3%A9tection%20et%20reconnaissance%20faciale/images/2.PNG?raw=true" width="400" higth="400" />
</p>
<p>
Le schéma explique la relation entre les éléments de notre système ainsi que les interactions entre eux, au démarrage de caméra de surveillance
nous allons prendre le Stream et l’envoyer vers un serveur flask où nous avons mis notre modèle de détection et reconnaissance, après avoir applique
la détection la partie programmation vas retourner le Stream avec la classification 
</p>
<br>
<p align ="center">
<img src="https://github.com/Y0unes17/systeme-de-contr-le-d-acces/blob/master/D%C3%A9tection%20et%20reconnaissance%20faciale/images/Screenshot%20(19).png?raw=true" width="400" higth="400" />
<img src="https://github.com/Y0unes17/systeme-de-contr-le-d-acces/blob/master/D%C3%A9tection%20et%20reconnaissance%20faciale/images/UntitledYT.png?raw=true" width="480" higth="600" />
</p>

<br>
<hr>
<h3>contributors</h3>
<strong>Chaaouri Jaafar   </strong>&nbsp;&nbsp;&nbsp;&nbsp;         <a href>Jaafar.Chaaouri@fsm.rnu.tn</a> <br>
<strong>Ben salah younes</strong>&nbsp;&nbsp;               <a href>younesbensalah17@gmail.com </a><br>
<strong>Jabnou Jihed    </strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   <a href>jihed.jabnoun@gmail.com</a >

