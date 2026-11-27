Exmple de document rst2pdf
==========================

**Author :** Tanguy Courau

**Date :** |thedate|

.. sectnum::
.. contents:: Sommaire
   :depth: 3

.. role:: rouge

.. footer:: ###Page###

.. |thedate| date:: %d/%m/%Y

============

|


Introduction
------------

L'utilitaire ``rst2pdf`` permet de taduire documents au format ``rst`` vers le format ``pdf``.
C'est moins riche que latex ou sphinx mais c'est pas mal et très direct.

Le présent document  montre un certains nombre de possibilités de l'outil, à commencer par la gestion des références bibliographiques.



Bibliographie
-------------

Par exemple, la méthode décrite par Knuth `[1] <ref1_>`_ reste une référence importante.

On peut également citer plusieurs sources [`1 <ref1_>`_, `2 <ref2_>`_].



Math
----

On peut faire des  ``:math:`` inline : :math:`e^{i\pi}+1=0` et également des équations :


.. math::

   \sin^2\theta+\cos^2\theta=1 \quad \mathrm{ et } \quad \int_0^1 xdx=1/2


.. |pi|  unicode:: U+03C0
.. |Delta| unicode:: U+0394
.. |phi|  unicode:: U+03A6
.. |varphi| unicode:: U+03C6		    

La directive ``:math:``  produit des images et ce n'est pas très joli, il est préférable d'utiliser l'alphabet grec quand c'est possible : e\ :sup:`iπ` +1=0, avec  |pi| > 1.



.. note::

   Il y a un problème avec (\\pi, \\Delta, \\phi, \\varphi)  : π, Δ, Φ, φ  ou (|pi|, |Delta|, |phi|, |varphi|) selon l'environnement informatique et le choix
   de la fonte associée à ``matplotlib.font_manager``.


   La fonte **georgia** est satisfaisante, la commande ``pdffont exemple.pdf`` permet d'identifier les fontes dans un document pdf.



Formattage et configuration
---------------------------


On peut forcer les espaces verticaux entre des lignes à l'aide du caractère ``|``.

|


et insérer des sauts de page avec la directive ::

   .. raw:: pdf

      PageBreak


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
     base:
      fontName: georgia
      fontSize: 11


et enfin un fichier de config ``~/.rsr2pdf/config`` qui contient :

.. code-block:: ini

   [general]
   # Language to be used for hyphenation support
   language="fr"


Tout cela permet de traduire le fichier ``exemple.rst`` à l'aide de la commande : ``rst2pdf exemple.rst -s mystyle -v``


.. raw:: pdf

   PageBreak


Listes
------


Des listes imbriquées

 - Ligne 1
 - Ligne 2
 - Ligne 3

    + Sous item 1
    + Sous item 2

|


Une liste *énumérée* **automatiquement**

 #. Un
 #. Deux
 #. Trois







Hyperliens
----------

- La page web `github <https://gist.github.com/jwodder/5a9264db8c3c81dad4c01e082515a9f1#intra-document-links>`_ explicite la gestion des liens en détail.

- Les titres de section du document sont accessibles directement : `Hyperliens`_, il n'est donc pas necessaire de créer une référence interne telle que  ::

    .. _hyperliensec:


Compteurs
---------

Il est possible de définir un compteur tels que l'initialisation du compteur Figure :counter:`figures`, on peut y référer à l'aide du
lien `Figure 1 <#figures-1>`_. Si on créee une seconde figure, alors le compteur s'incrémente automatiquement Figure :counter:`figures`
et on peut y référeer  à l'aide du lien `Fig. 2 <#figures-2>`_.

.. note::
   Le lien vers un compteur doit préciser la valeur du compteur, il n'est pas mis à jour automatiquement.



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



Note et Warning
---------------

.. note::

   Une petite note !

.. warning::

   Un joli saut de page suivi d'un trait





Et encore un lien vers le tableau `3  <#tables-3>`_ pour fin de test, on peut également accéder à la section `8 <Tableaux_>`_.

-------------------------

Références
----------

.. _ref1:

[1] Knuth, D. E. The TeXbook. Addison-Wesley, 1984.

.. _ref2:

[2] Lamport, L. LaTeX: A Document Preparation System. Addison-Wesley, 1994.


.. rst2pdf exemple.rst  -s mystyle  -v
