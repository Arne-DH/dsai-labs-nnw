---
title: "Chapter 4: Bivariate analysis of qualitative variables"
---

## Learning goals

- Dependent/independent variable

- Apply suitable analysis techniques for each combination of measurement
  levels

- Contingency tables and Cramér's $V$

- Visualization

---

## Overview: bivariate analysis techniques

| **Independent** | **Dependent** |  **Test/Metric**                |
| :---:           | :---:         | :---                            |
| Qualitative     | Qualitative   | $\chi^2$-test/Cramér's $V$      |
| Qualitative     | Quantitative  | two-sample $t$-test/Cohen's $d$ |
| Quantitative    | Quantitative  | -/Regression, correlation       |

---

## Overview: bivariate analysis - visualization

| **Independent** | **Dependent** |  **Plot**                                  |
| :---:           | :---:         | :---                                       |
| Qualitative     | Qualitative   | Grouped/stacked bar chart, mosaic plot     |
| Qualitative     | Quantitative  | Grouped boxplot, bar chart with error bars |
| Quantitative    | Quantitative  | Scatter plot, regression line              |

---

## Bivariate analysis

- ...is determining whether there is an association between two
  stochastic variables ($X$ and $Y$).

- **Association** = you can predict (to some extent) the value of $Y$
  from the value of $X$

    - $X$: Independent variable

    - $Y$: Dependent variable

- **Important!** Finding an association does **NOT** imply a causal relation!

---

## Example research questions

- Is there a difference in taste preference between two beverage brands?

- Is there a difference in spending at the campus restaurant between
  students and staff?

- Do smokers die more often of lung cancer than non-smokers?

- Do men and women have a different opinion on a survey question?

- ...

We will use [data/rlanders.csv](https://github.com/HoGentTIN/dsai-labs/blob/main/data/rlanders.csv) from the Github repo for lab assignments
to explore the last question.

---

