import plotly.express as px
import pandas as pd

schools = ["Brown", "NYU", "Notre Dame", "Cornell", "Tufts", "Yale",
           "Dartmouth", "Chicago", "Columbia", "Duke", "Georgetown",
           "Princeton", "U.Penn", "Stanford", "MIT", "Harvard"]
n_schools = len(schools)

women_salary = [72, 67, 73, 80, 76, 79, 84, 78, 86, 93, 94, 90, 92, 96, 94, 112]
men_salary = [92, 94, 100, 107, 112, 114, 114, 118, 119, 124, 131, 137, 141, 151, 152, 165]

df = pd.DataFrame(dict(school=schools*2, salary=men_salary + women_salary,
                       gender=["Men"]*n_schools + ["Women"]*n_schools))

# Use column names of df for the different parameters x, y, color, ...
fig = px.scatter(df, x="salary", y="school", color="gender",
                 title="Gender Earnings Disparity",
                 labels={"salary":"Annual Salary (in thousands)"} # customize axis label
                )

fig.show(renderer="json")