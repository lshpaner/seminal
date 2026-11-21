Usage Guide
===========

FSH alone: ``azoospermia_fsh``
------------------------------

``azoospermia_fsh`` returns the probability (0 to 1) from serum FSH only. It
accepts a scalar or an array.

.. code-block:: python

   import numpy as np
   from seminal import azoospermia_fsh

   azoospermia_fsh(5.7)                       # 0.0892
   azoospermia_fsh(np.array([2, 10, 20, 35])) # array([0.0870, 0.1375, 0.44, 1.0])

The published quadratic is unbounded and exceeds 100% above roughly 30 IU/L.
By default the output is clipped to [0, 1]; pass ``clip=False`` to reproduce
the raw polynomial, which is what the paper's own validation tables carry.

Full model: ``azoospermia_lr``
------------------------------

``azoospermia_lr`` returns the probability from the five-variable logistic
regression. All five inputs are required.

.. code-block:: python

   from seminal import azoospermia_lr

   azoospermia_lr(age=36, fsh=5.7, lh=4.5, testosterone=429, testis_volume=15)
   # 0.086

Explaining a prediction
~~~~~~~~~~~~~~~~~~~~~~~

Pass ``explain=True`` to get a breakdown instead of a single number:

.. code-block:: python

   out = azoospermia_lr(age=40, fsh=18, lh=9, testosterone=280,
                        testis_volume=9, explain=True)

   out["risk"]              # 0.557
   out["intercept"]         # -1.9
   out["linear_predictor"]  # 0.23  (log-odds)
   out["contributions"]     # {'fsh': 2.34, 'age': 0.8, 'testis_volume': -0.72, ...}

Each value in ``contributions`` is that input's term in the log-odds,
``coefficient × value``, listed largest first. The terms are raw, not centered,
so they carry each variable's scale: testosterone has a small coefficient on a
large number, and age contributes 0.02 per year from zero. Compare patients
by the difference in their terms rather than reading one patient's terms as
"effect sizes".

Cohorts: ``add_azoospermia_risk_cols``
--------------------------------------

``add_azoospermia_risk_cols`` adds both probabilities to a DataFrame.

.. code-block:: python

   from seminal import add_azoospermia_risk_cols

   scored = add_azoospermia_risk_cols(
       df,
       age_col="age", fsh_col="fsh", lh_col="lh",
       testosterone_col="testosterone", testis_volume_col="testis_volume",
       lr_col="azoo_lr", fsh_model_col="azoo_fsh",
       copy=True,
   )

The arguments shown are the defaults, so a DataFrame that already uses these
column names needs only ``add_azoospermia_risk_cols(df)``.

The function:

- coerces each column to numeric; anything unparseable becomes ``NaN``
- returns ``NaN`` in ``azoo_lr`` for any row missing one of the five inputs,
  rather than guessing
- fills ``azoo_fsh`` for every row that has an FSH value
- returns a copy by default (``copy=True``) and leaves the input unchanged

A worked example on the paper's validation cohorts, with ROC, precision-recall
and calibration curves per site, is in :doc:`_notebooks/00_quickstart`.
