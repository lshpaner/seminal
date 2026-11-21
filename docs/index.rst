Welcome to the seminal Python Library Documentation!
====================================================

.. note::

   This documentation is for ``seminal`` version |version_str|.

``seminal`` is a Python library of published risk equations in andrology and
male reproductive health, implemented with the coefficients exactly as printed
in the source papers and checked against the authors' own validation data.

The first release implements the two azoospermia prediction models of
Tradewell et al. (*World J Mens Health* 2022): a quadratic in serum FSH alone,
and a logistic regression on age, FSH, LH, total testosterone and mean testis
volume. Both estimate the probability that a man presenting for infertility
evaluation has no sperm in the ejaculate, without a semen analysis.

The library scores single patients or entire cohorts, explains each patient's
risk term by term, and ships with the scripts and notebooks that rebuild the
paper's cohort from the public data deposit and reproduce its external
validation.

.. important::

   ``seminal`` is not affiliated with the original authors. It is an
   independent implementation of published equations, intended for research
   use. It is not a medical device and should not be used to make clinical
   decisions.

Prerequisites
-------------

- **Python**: 3.8 or higher
- **numpy**: 1.20 or higher
- **pandas**: 1.3 or higher

Installation
------------

.. code-block:: bash

   pip install --pre seminal

``--pre`` is needed while the package is in alpha.

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   getting_started
   _notebooks/00_quickstart

.. toctree::
   :maxdepth: 2
   :caption: Documentation

   usage_guide
   inputs
   model
   data
   _notebooks/01_reproduce_tradewell
   api

.. toctree::
   :maxdepth: 2
   :caption: About seminal

   contributors
   acknowledgements
   citing
   changelog
   references
