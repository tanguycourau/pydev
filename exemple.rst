test de bibliographie avec rst2pdf
==================================

.. sectnum::
.. contents:: Sommaire
   :depth: 3


Introduction
------------

rst2pdf permet de gérer des références bibliographiques. Par exemple,
la méthode décrite par Knuth `[1] <ref1_>`_ reste une référence importante.

On peut également citer plusieurs sources `[1] <ref1_>`_  `[2] <ref2_>`_.


On peut faire des maths également :math:`e^{i\pi}+1=0` !

.. raw:: pdf

   PageBreak

   
Un joli saut de page

Références
----------

.. _ref1:

[1] Knuth, D. E. The TeXbook. Addison-Wesley, 1984.

.. _ref2:

[2] Lamport, L. LaTeX: A Document Preparation System. Addison-Wesley, 1994.



.. rst2pdf exemple.rst --footer="Page ###Page###"
