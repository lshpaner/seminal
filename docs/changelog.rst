Changelog
=========

Version 0.0.0a2 (2026-11-20)
----------------------------

- README corrections: pre-release badge, install note, affiliation, the
  reproduced exclusion rule and the matching Chicago numbers.
- ``dcurves`` added to the ``data`` extras for the reproduction notebook.
- Full journal title in the package description.
- Documentation site and Zenodo archiving. No changes to the equations.

Version 0.0.0a1 (2026-11-20)
----------------------------

- First alpha release.
- ``azoospermia_fsh``: probability of azoospermia from serum FSH alone, the
  quadratic of Fig. 1 in Tradewell et al. (2022), clipped to [0, 1] by default.
- ``azoospermia_lr``: the five-variable logistic regression of Table 3, with
  ``explain=True`` returning the linear predictor and each input's log-odds
  contribution.
- ``add_azoospermia_risk_cols``: both probabilities for every row of a
  DataFrame, ``NaN`` for incomplete rows.
- ``data_gen.py`` and ``preprocessing.py`` rebuild the paper's three cohorts
  from the CC0 Dataverse deposit; the test suite checks the external AUCs
  against the paper when the data are present.
- Notebooks: quickstart, and a full reproduction of the paper (cohort,
  Table 1, refit, calibration, decision curves, recalibration).
- Tested on Python 3.8 to 3.13.
