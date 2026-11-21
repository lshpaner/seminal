The Models
==========

Outcome
-------

Both models predict azoospermia: no spermatozoa in the ejaculate, confirmed on
at least two semen analyses with centrifugation of the pellet. The question
they answer is whether a man presenting for infertility evaluation can be told
his probability of azoospermia from a blood test, before or instead of a semen
analysis.

Development
-----------

Tradewell et al. (2022) developed both models on 946 men evaluated at the
University of Miami, after excluding prior vasectomy, solitary testis,
exogenous testosterone or anabolic steroid use, and Y chromosome
microdeletions. They then validated the models on 1,955 men from Milan (IRCCS
Ospedale San Raffaele) and 596 from Chicago (University of Illinois).

FSH-only quadratic
------------------

The Miami men were binned by FSH and the observed proportion azoospermic in
each bin was fit with a second-degree polynomial (Fig. 1 of the paper,
R² = 0.95):

.. math::

   p(\%) = 0.133\,\mathrm{FSH}^2 - 0.965\,\mathrm{FSH} + 10.1

The curve is U-shaped: 10.1% at FSH 0, a minimum of 8.35% at FSH 3.63 IU/L,
and 100% at 29.9 IU/L. ``azoospermia_fsh`` divides by 100 and clips to
[0, 1] by default.

Logistic regression
-------------------

.. math::

   p = \frac{1}{1 + e^{-\eta}}, \qquad
   \eta = \beta_0 + \sum_i \beta_i x_i

with the coefficients of Table 3, used exactly as printed:

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - Term
     - Units
     - Coefficient
   * - Intercept
     -
     - −1.9
   * - Age
     - years
     - 0.02
   * - FSH
     - IU/L
     - 0.13
   * - LH
     - IU/L
     - 0.03
   * - Total testosterone
     - ng/dL
     - −0.002
   * - Mean testis volume
     - mL (orchidometer)
     - −0.08

The paper prints the model form as ``1/exp[−(b₀ + bᵢXᵢ)]``, which is a
typesetting error (it exceeds 1 for any negative linear predictor). The
standard logistic form is used here.

What the reproduction shows
---------------------------

The notebook :doc:`_notebooks/01_reproduce_tradewell` rebuilds the paper from
the public deposit. In short:

- The cohort sizes (946 / 1,955 / 596) are reproduced exactly, with one
  departure from the stated exclusion rule (see :doc:`data`).
- A fresh logistic fit on the Miami rows recovers every Table 3 coefficient
  within one standard error.
- The external AUCs reproduce: Milan 0.786 / 0.786 and Chicago 0.718 / 0.707
  (logistic / FSH-only) against the paper's 0.79 / 0.78 and 0.72 / 0.71.
- Calibration, which the paper did not report, is where the models differ.
  The logistic model under-predicts in Milan (calibration-in-the-large +0.52
  on the log-odds scale, slope 0.73); the FSH-only quadratic is markedly
  over-confident on both sites (slope 0.23 to 0.34), and because it saturates
  at exactly 0 and 1 it cannot be recalibrated on the logit scale.
- An intercept-only recalibration fixes calibration-in-the-large per site. A
  logistic model in FSH alone, ``logit(p) = −3.17 + 0.145·FSH`` fit on Miami,
  matches the quadratic's discrimination and Brier score with far better
  calibration. That model is this reproduction's proposal, not part of the
  published paper, and is planned as a separately named function in a later
  release.

Discrimination
--------------

The paper reports AUCs of 0.79 (logistic) and 0.78 (FSH-only) in Milan and
0.72 and 0.71 in Chicago. ``tests/test_azoospermia.py`` checks the library
against these when ``data/processed/`` is present.

What is not implemented
-----------------------

- **Refit (full-precision) coefficients.** Recovered in the notebook but kept
  out of the package so that the package stays an implementation of the
  published equation.
- **Risk thresholds.** The paper does not define a cutoff for "high risk", so
  the package reports probabilities only.
- **Obstructive vs non-obstructive azoospermia.** The outcome is any
  azoospermia; the models do not distinguish cause.
