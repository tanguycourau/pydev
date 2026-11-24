test de doc rst2pdf
===================

.. sectnum::
.. contents:: Sommaire
   :depth: 3


Introduction
------------

rst2pdf permet de gérer des références bibliographiques. Par exemple,
la méthode décrite par Knuth `[1] <ref1_>`_ reste une référence importante.

On peut également citer plusieurs sources `[1] <ref1_>`_  `[2] <ref2_>`_.


On peut faire des maths en ligne :math:`e^{i\pi}+1=0` et également des équations


.. math::

   \sin^2+\cos^2=1

|

.. class:: rouge

   Ceci est un paragraphe en rouge qui peut
   
   s'étaler sur plusieurs lignes !

.. _tableaux:

Tableaux
--------


.. _tab-voiliers:

.. table:: Table 1 - Comparatif de voiliers


   +-----------+--------+--------+
   | Modèle    | LC (m) | TE (m) |
   +===========+========+========+
   | Dufour 34 | 10.28  | 1.90   |
   +-----------+--------+--------+
   | X-37      | 11.35  | 2.10   |
   +-----------+--------+--------+
   | Salona 37 | 11.29  | 2.28   |
   +-----------+--------+--------+	
	   




Voir le tableau `[1] <tab-voiliers_>`_ qui est décrit à la section   `[2] <tableaux_>`_ 

Codeblock
---------

.. code-block:: python

   gv = 35.0      # Grand-voile (m²)
   foc = 28.0     # Foc (m²)

   surface_totale = gv + foc

   print(f"Surface totale : {surface_totale:.1f} m²")


.. raw:: pdf

   PageBreak

   
Un joli saut de page



Références
----------

.. _ref1:

[1] Knuth, D. E. The TeXbook. Addison-Wesley, 1984.

.. _ref2:

[2] Lamport, L. LaTeX: A Document Preparation System. Addison-Wesley, 1994.


.. rst2pdf exemple.rst --footer="Page ###Page###" -s mystyle -l fr -v
