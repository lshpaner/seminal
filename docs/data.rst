The Data
========

The study data are public under CC0 on Harvard Dataverse
(`doi:10.7910/DVN/EQFMCM <https://doi.org/10.7910/DVN/EQFMCM>`_): one Excel
file with a sheet per site (Miami 1,070 rows, Milan 1,955, Chicago 643) and a
key. The repository never commits data; ``data/`` is gitignored.

Download and harmonize
----------------------

.. code-block:: bash

   make data_gen      # python data_gen.py      -> data/raw/      (one Parquet per sheet)
   make preprocess    # python preprocessing.py -> data/processed/tradewell_2022.parquet

``data_gen.py`` only fetches and saves. ``preprocessing.py`` renames each
site's columns to the five model inputs, applies the exclusions, builds the
outcome, labels the testis volume method per site, median-imputes LH,
testosterone and testis volume within site, and adds the FSH / LH /
testosterone / volume categories used in the paper's Table 1. Options:

.. code-block:: text

   --exclusions reproduced|stated   which exclusion rule (default reproduced)
   --no-impute                      leave missing hormones as NaN
   --csv                            also write a CSV copy
   --raw-dir / --out-dir            paths

The output has one row per man with ``site``, the five inputs,
``azoospermia`` (0/1), ``included`` (passes the exclusion rule),
``testis_volume_method`` and the Table 1 bin columns.

Two exclusion rules
-------------------

Applying the exclusions exactly as the paper states them (prior vasectomy, Y
chromosome microdeletion, solitary testis, testosterone or steroid use) gives
Miami 943 and Chicago 614, not the paper's 946 and 596. The paper's counts are
recovered exactly by:

- **not** excluding Y microdeletions,
- reading solitary testis from the absence-reason codes 1 to 3 in Miami (code
  4 is kept) and from a zero testis volume in Chicago,
- defining azoospermia in Chicago as sperm concentration below 0.01 M/mL
  (three cryptozoospermic rows), rather than exactly zero.

``preprocessing.py`` applies this reproduced rule by default and the literal
rule with ``--exclusions stated``. The choice does not change the AUCs or the
calibration summaries. Milan (1,955) matches either way.

Things to know
--------------

- **Chicago testis volumes are not volumes.** The Chicago sheet carries
  ultrasound long-axis lengths in cm (median 4.5), while Miami and Milan carry
  orchidometer volumes in mL (median 14 to 15). The paper's Table 1 reports a
  Chicago median of 14.8 mL; the conversion it used is not recoverable from the
  deposit. ``preprocessing.py`` labels the method per site and does not
  convert. The reported Chicago AUC is unaffected (a monotone rescaling of one
  predictor barely moves discrimination), but the Chicago intercept is: with
  lengths in cm the model happens to be calibrated-in-the-large, and with
  volumes in mL it would under-predict by about +0.85 on the log-odds scale.
- **Milan's FSH bins use Milan's own cutoff.** The Table 1 FSH categories for
  Milan use high FSH ≥ 12.5 IU/L, not the Miami reference range used for the
  other sites. ``add_reference_bins`` in ``preprocessing.py`` uses the paper's
  reference ranges for all sites, so one Milan cell differs from the paper.
- **No patient identifier.** Rows are semen analyses; men with more than one
  analysis cannot be identified, so the sensitivity analysis to one row per
  man is not possible.
- **Outcome definitions differ by sheet.** Miami and Chicago carry sperm
  concentration; Milan carries an explicit azoospermia flag plus
  obstructive / non-obstructive type.
- **Coefficients are rounded.** Table 3 prints one or two significant figures.
  The refit in :doc:`_notebooks/01_reproduce_tradewell` recovers full
  precision; the library keeps the published values.
