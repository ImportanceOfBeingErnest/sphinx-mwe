Sphinx-mwe
==========

This is a minimal working example for sphinx
including autodoc, autosummary, and sphinx-gallery.

The sphinx-mwe-bug folder includes a bug. This is due
to an Alias class being created in the module. 

Sphinx-upperlowercase
=====================

This is a minimal example showing a bug with upper and lowercase, i.e.
creating a documentation from a python file like

::

    class Colorbar():
         # ...

    def colorbar():
         # ...
         
where two objects differ just between upper and lower case leads to an error.