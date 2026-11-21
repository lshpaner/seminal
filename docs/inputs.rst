Input Requirements and Common Pitfalls
======================================

Inputs
------

.. list-table::
   :header-rows: 1
   :widths: 28 24 48

   * - Input
     - Argument (column default)
     - Units and notes
   * - Age
     - ``age``
     - years; the development cohort were adult men presenting for infertility evaluation
   * - Follicle-stimulating hormone
     - ``fsh``
     - IU/L (equivalently mIU/mL); the only input to the FSH-only model
   * - Luteinizing hormone
     - ``lh``
     - IU/L (mIU/mL)
   * - Total testosterone
     - ``testosterone``
     - ng/dL; multiply nmol/L by 28.84 to convert
   * - Mean testis volume
     - ``testis_volume``
     - mL (cm³), mean of left and right, Prader orchidometer in the development cohort

Reference ranges quoted in the paper, used only for context (the models do
not threshold on them): FSH 1.5 to 7.6 IU/L, LH 1.8 to 8.6 IU/L, total
testosterone 300 to 1000 ng/dL, mean testis volume 12.5 to 19 mL.

Common pitfalls
---------------

**Testosterone in nmol/L.** The model expects ng/dL. SI values are about 29
times smaller, which makes the testosterone term nearly vanish and raises the
predicted risk. Convert with ``ng/dL = nmol/L × 28.84``.

**Testis volume by ultrasound.** The coefficient was fit to orchidometer
volumes (median 15 mL in Miami and Milan). Ultrasound long-axis lengths in cm,
or ellipsoid volumes computed from ultrasound dimensions, are on a different
scale and shift the linear predictor. The Chicago validation sheet in the
public deposit carries lengths in cm (median 4.5), not volumes; see
:doc:`data`.

**Output is a fraction, not a percent.** Both functions return 0 to 1. The
paper's FSH-only equation is written in percent (``p(%) = 0.133·FSH² −
0.965·FSH + 10.1``); the library divides by 100.

**FSH above 30 IU/L.** The FSH-only quadratic exceeds 100% there. The default
``clip=True`` caps it at 1; the logistic model has no such problem.

**Rounded coefficients.** The logistic coefficients are printed to one or two
significant figures. At the extremes of age and testosterone this rounding
alone can move the log-odds by several tenths. A refit on the Miami data
recovers full-precision values (see :doc:`_notebooks/01_reproduce_tradewell`);
the library keeps the as-published numbers.

**Missing values in cohorts.** ``add_azoospermia_risk_cols`` returns ``NaN``
in ``azoo_lr`` for rows missing any of the five inputs. Count them before
summarizing, since complete-case results may not represent the full cohort.
``preprocessing.py`` median-imputes LH, testosterone and testis volume within
site by default (``--no-impute`` to turn that off), which is what the
validation numbers in these docs use.
