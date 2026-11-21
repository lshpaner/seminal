Getting Started
===============

FSH alone
---------

.. code-block:: python

   from seminal import azoospermia_fsh

   azoospermia_fsh(20)
   # 0.439  -> a 43.9% probability of azoospermia

The published curve is U-shaped: 10.1% at undetectable FSH, a minimum of about
8.4% at FSH 3.6 IU/L, and 100% from about 30 IU/L.

Full logistic model
-------------------

.. code-block:: python

   from seminal import azoospermia_lr

   azoospermia_lr(age=36, fsh=5.7, lh=4.5, testosterone=429, testis_volume=15)
   # 0.086

This is the median man from the paper's Table 1. Pass ``explain=True`` to also
get the linear predictor and each input's contribution to the log-odds.

Score a cohort
--------------

.. code-block:: python

   from seminal import add_azoospermia_risk_cols

   scored = add_azoospermia_risk_cols(df)   # adds "azoo_fsh" and "azoo_lr"

See :doc:`_notebooks/00_quickstart` for a worked example with output,
:doc:`usage_guide` for column mapping, and :doc:`inputs` for the expected
units.

Library overview
----------------

.. code-block:: python

   import seminal
   help(seminal)   # prints the logo and a summary of the library

Table of Contents
-----------------

**Getting Started**

- :doc:`index`
- :doc:`getting_started`
- :doc:`_notebooks/00_quickstart`

**Documentation**

- :doc:`usage_guide`
- :doc:`inputs`
- :doc:`model`
- :doc:`data`
- :doc:`_notebooks/01_reproduce_tradewell`
- :doc:`api`

**About seminal**

- :doc:`contributors`
- :doc:`acknowledgements`
- :doc:`citing`
- :doc:`changelog`
- :doc:`references`
