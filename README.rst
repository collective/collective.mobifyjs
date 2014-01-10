*******************
collective.mobifyjs
*******************

.. image:: https://saucelabs.com/buildstatus/collective_mobifyjs
    :alt: Selenium Test Status
    :target: https://saucelabs.com/u/collective_mobifyjs

.. contents::

Introduction
============

``collective.mobify.js`` is a package which uses `Mobify.js`_ to provide responsive
images. This is done by loading the images thru an image resizing API which
automatically resizes and compresses the images.

.. _`Mobify.js`: http://www.mobify.com/mobifyjs


What's this responsive image thing?
===================================

When viewing web pages on small devices images aren't optimized. Often images
are the biggest resources on a page.

This packages uses the Mobify.js library to manipulate the DOM before any
images are loaded. Before the images are loaded the location to the images in
the :code:`src` tag are rewritten to an image resizing API.

Images are resized using Mobify's resizing service, this service is free to
use for a limited amount of requests. ``collective.mobify.js`` has the
option to use a different image resizing service.

The inspiration for the package ``collective.mobify.js`` came from this
article `Automate Your Responsive Images With Mobify.js`_.

.. _`Automate Your Responsive Images With Mobify.js`: http://mobile.smashingmagazine.com/2013/10/24/automate-your-responsive-images-with-mobify-js/

Installation
============

To enable this package in a buildout-based installation:

#. Edit your buildout.cfg and add add the following to it::

    [buildout]
    ...
    eggs =
        collective.mobifyjs

After updating the configuration you need to run ''bin/buildout'', which will
take care of updating your system.

Go to the 'Site Setup' page in a Plone site and click on the 'Add-ons' link.


Check the box next to ``collective.mobifyjs`` and click the 'Activate' button.

How to use mobify.js
====================

After activation thru the Add-ons page ``collective.mobify.js`` is active and
images are resized via the Mobify.js API.

This resizing API has a limit to the amount of images which can be converted,
more details can be found on `Mobify cloud pricing`_ page.

.. _`Mobify cloud pricing`: https://cloud.mobify.com/mps/

``collective.mobify.js`` has the following settings which can be changed in the
 Add-on Configuration in the Site Setup.

*Mobify.js library URL'*
    The URL to the Mobify.js library, defaults to Mobify's CDN.

*Resize backend URL*
    The URL to the resizing service, defaults to Mobify's resizing service.

