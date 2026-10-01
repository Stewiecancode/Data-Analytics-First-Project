# Student Performance Analysis

A data analysis project exploring how school absences, study time, home internet access, and other student characteristics relate to academic performance.

The project uses real student data to practise Python, data cleaning, exploratory analysis, and visualisation.

## Project status

In development. The dataset is available; the analyses and dashboard below are project goals. No findings are claimed until the analysis has been completed.

## Objectives

- Inspect and validate the dataset.
- Explore the distribution of final grades and school absences.
- Compare grades across study-time categories and home internet access.
- Compare average grades across school periods and between schools.
- Present findings with charts and a simple Streamlit dashboard.

## Dataset

The project uses the Portuguese-language course file (`student-por.csv`) from the **UCI Student Performance** dataset, saved locally as `student_performance_real.csv`.

- **Records:** 649 student course records.
- **Columns:** 33, including 30 input attributes and three grade columns.
- **Location:** Two secondary schools in Portugal.
- **Collection:** School reports and questionnaires.
- **Format:** CSV with semicolon (`;`) separators.
- **Source:** [UCI Student Performance](https://archive.ics.uci.edu/dataset/320/student+performance).
- **Dataset DOI:** [10.24432/C5TG7T](https://doi.org/10.24432/C5TG7T).

This is historical Portuguese education data. Findings should be interpreted within that context rather than assumed to describe South African learners.

### Key columns

| Column | Description |
|---|---|
| `school` | School code: GP or MS |
| `age` | Student age |
| `absences` | Number of school absences |
| `studytime` | Weekly study-time category |
| `failures` | Coded number of previous class failures |
| `internet` | Internet access at home: yes or no |
| `schoolsup` | Extra educational support: yes or no |
| `G1` | First period grade, out of 20 |
| `G2` | Second period grade, out of 20 |
| `G3` | Final grade, out of 20 |

### Study-time categories

| Value | Weekly study time |
|---|---|
| 1 | Less than 2 hours |
| 2 | 2–5 hours |
| 3 | 5–10 hours |
| 4 | More than 10 hours |

Treat `studytime` as an ordered category, not an exact number of hours. The source page provides definitions for all columns.

## Tools

- **Python:** Data processing and analysis.
- **pandas:** Loading, cleaning, grouping, and summarising data.
- **Matplotlib:** Charts.
- **Jupyter Notebook:** Documenting analysis.
- **Streamlit:** Planned interactive dashboard.

## Getting started

### 1. Prepare your project folder

Place `README.md` and `student_performance_real.csv` in the same project folder. Open a terminal in that folder.

If the CSV is unavailable, download the ZIP from the UCI source page, extract the nested `student.zip`, and rename `student-por.csv` to `student_performance_real.csv`.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install pandas matplotlib jupyter streamlit
```

### 4. Open Jupyter

```bash
jupyter notebook
```

Create a Python notebook in the project folder and run:

```python
import pandas as pd

df = pd.read_csv("student_performance_real.csv", sep=";")

print(df.head())
print("Rows and columns:", df.shape)
print(df.dtypes)
print("Missing values:", df.isna().sum().sum())
```

The expected shape is `(649, 33)`. If everything appears in one column, check that `sep=";"` is included.

## First analysis: absences and final grades

```python
import matplotlib.pyplot as plt

print("Average final grade:", round(df["G3"].mean(), 2))
print("Average absences:", round(df["absences"].mean(), 2))

df.plot.scatter(x="absences", y="G3", alpha=0.5)
plt.title("School absences and final grades")
plt.xlabel("Number of absences")
plt.ylabel("Final grade (out of 20)")
plt.tight_layout()
plt.show()
```

Inspect the chart before drawing conclusions. Record the pattern, unusual observations, and what remains uncertain.

## Analysis questions

| Question | Suggested visual |
|---|---|
| How are absences associated with final grades? | Scatter plot |
| How do grade distributions differ across study-time categories? | Box plot |
| How do grades differ by home internet access? | Box plot |
| How do average grades change across G1, G2, and G3? | Line chart |
| How do final grades compare between the two schools? | Box plot |

Include group sizes alongside comparisons. Check duplicate rows, but do not automatically delete them: matching attributes do not necessarily identify the same student.

## Planned dashboard

- Total student records.
- Average final grade and average absences.
- Filters for school and study-time category.
- Grade distributions and group comparisons.
- Short explanations of findings and limitations.

After creating an `app.py` dashboard, run it with:

```bash
streamlit run app.py
```

## Interpretation limits

- Associations do not establish cause and effect.
- School and group comparisons may reflect differences in student backgrounds.
- Study time is categorised and cannot be interpreted as precise hours.
- G1 and G2 are earlier grades. If predicting G3, choose inputs according to when the prediction would be made; an early-year model cannot use grades that are not yet available.
- This exploratory project does not establish that an intervention improves student outcomes.

## Completion checklist

- [ ] Load and inspect the dataset.
- [ ] Validate missing values, categories, and numeric ranges.
- [ ] Produce at least three useful charts.
- [ ] Write observations supported by the analysis.
- [ ] Build the Streamlit dashboard.
- [ ] Add screenshots and reproducible run instructions.
- [ ] Document limitations and credit the dataset.

## Dataset attribution and licence

Cortez, P. (2008). *Student Performance* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5TG7T.

The dataset is licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). Preserve this attribution when sharing the data or publishing the project.

## Author

**Tshireletso Selemela**

[GitHub](https://github.com/Stewiecancode)

