Exmple de document rst2pdf
==========================

**Author :** Jean Dupont

**Date :** 24 novembre 2026 

.. sectnum::
.. contents:: Sommaire
   :depth: 3

.. role:: rouge

.. footer:: ###Page###
   
	   
Introduction
------------

rst2pdf permet de gérer des références bibliographiques. Par exemple,
la méthode décrite par Knuth `[1] <ref1_>`_ reste une référence importante.

On peut également citer plusieurs sources `[1] <ref1_>`_  `[2] <ref2_>`_.


On peut faire des maths en ligne :math:`e^{i\pi}+1=0` et également des équations : 


.. math::

   \sin^2\theta+\cos^2\theta=1



.. |pi|  unicode:: U+03A0   

Les math en ligne produisent des images et c'est pas très joli, il est préférable d'utiliser l'alphabet grec quand c'est possible : e\ :sup:`i Π` +1=0 


.. note::

   Il y a un problème avec pi dont l'unicode est : U+03C0 et qui renvoie π avec ``rst2pdf`` alternativement le caractère majuscule |pi| s'affiche également via l'unicode U+03A0.  

|



.. class:: rouge

   Ceci est un paragraphe en rouge qui peut
   
   s'étaler sur plusieurs lignes !

On peut aussi ecrire des mots :rouge:`en rouge` sous réserve d'avoir déclaré dans le fichier ``rst`` ::

  ..role:: rouge

et d'avoir créé un fichier style ``mystyle`` qui contient :

.. code-block:: yaml

   styles:
     rouge:
      textColor: red   



et enfin un fichier de config ``~/.rsr2pdf/config`` qui contient :

.. code-block:: ini

   [general]
   # Language to be used for hyphenation support
   language="fr"


Tout cela permet de traduire le fichier ``exemple.rst`` à l'aide de la commande : ``rst2pdf exemple.rst -s mystyle -v``


Une liste énumérée automatiquement

 #. Un
 #. Deux
 #. Trois


Compteurs
---------

Il est possible de définir un compteur tels que l'initialisation du compteur Figure :counter:`figures`, on peut y référer à l'aide du
lien `Figure 1 <#figures-1>`_. Si on créee une seconde figure, alors le compteur s'incrémente automatiquement Figure :counter:`figures`
et on peut y référeer  à l'aide du lien `Fig. 2 <#figures-2>`_.

.. note::
   Le lien vers un compteur doit préciser la valeur du compteur, il n'est pas mis à jour automatiquement.


.. _tablesec:

Tableaux
--------

.. table:: Table :counter:`tables:3` - Comparatif de voiliers


   +-----------+--------+--------+
   | Modèle    | LC (m) | TE (m) |
   +===========+========+========+
   | Dufour 34 | 10.28  | 1.90   |
   +-----------+--------+--------+
   | X-37      | 11.35  | 2.10   |
   +-----------+--------+--------+
   | Salona 37 | 11.29  | 2.28   |
   +-----------+--------+--------+	
	   


Le référence à `Tab. 3 <#tables-3>`_  utilise un compteur  initialisé à 3 en l'occurence. 


    
     

   
Codeblock
---------

.. code-block:: python
   :linenos:

   gv = 35.0      # Grand-voile (m²)
   foc = 28.0     # Foc (m²)

   surface_totale = gv + foc

   print(f"Surface totale : {surface_totale:.1f} m²")


.. raw:: pdf

   PageBreak

.. note::

   Une petite note !

.. warning::

   Un joli saut de page suivi d'un trait


============   

Et encore un lien vers le tableau `3  <#tables-3>`_ pour fin de test, on peut également accéder à la `Sec. 2 <tablesec_>`_.  



Références
----------

.. _ref1:

[1] Knuth, D. E. The TeXbook. Addison-Wesley, 1984.

.. _ref2:

[2] Lamport, L. LaTeX: A Document Preparation System. Addison-Wesley, 1994.


.. rst2pdf exemple.rst  -s mystyle  -v
