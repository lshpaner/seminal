API Reference
=============

Single patient
--------------

.. autofunction:: seminal.azoospermia_fsh

.. autofunction:: seminal.azoospermia_lr

Cohorts
-------

.. autofunction:: seminal.add_azoospermia_risk_cols

Constants
---------

``seminal.azoospermia.LR_COEFS``
   Table 3 coefficients on the log-odds scale: ``intercept``, ``age``,
   ``fsh``, ``lh``, ``testosterone``, ``testis_volume``.

``seminal.azoospermia.FSH_QUAD``
   Fig. 1 quadratic in percent: ``a`` (FSH²), ``b`` (FSH), ``c`` (constant).

``seminal.azoospermia.REFERENCE_RANGES``
   Reference limits quoted in the paper for FSH, LH, total testosterone and
   mean testis volume. Informational only; the models do not threshold on
   them.
