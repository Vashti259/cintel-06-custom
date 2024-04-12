# Import Packages as needed for Python and Pyshiny Packages.

import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render
import pandas as pd
from shiny.express import ui, input, render
import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly


# Import Packages as needed for Python and Pyshiny Packages.
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render
import pandas as pd
from shiny.express import ui, input, render
import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import csv

# Add a UI Title Page And Sidebar with data information.

ui.page_opts(title="NBA outlook on LeBron James 2023-2024", fillable=True)
with ui.layout_columns():
    from shiny.express import ui

with ui.sidebar(bg="#f8f8f8"):
    "Vashti's Module 6 App demonstrates LeBron James Progress 2023-2024"

"LeBron James Stats and Progress"

# Define LeBron James's stats for the 2023 and 2023-24 NBA seasons
lebron_stats_2023 = {
    "Season": "2023",
    "Points per game": 28.9,
    "Rebounds per game": 8.3,
    "Assists per game": 6.8,
    "All-Star Games": 19,
}

lebron_stats_2024 = {
    "Season": "2023-24",
    "Points per game": 25.4,
    "Rebounds per game": 7.3,
    "Assists per game": 8.1,
    "Field Goal Percentage": 53.6,
}

print("LeBron James Stats (2023-24):")
for key, value in lebron_stats_2023.items():
    print(f"{key}: {value}")

# Add UI cards display
ui.page_opts(fillable=True)

with ui.layout_columns():
    with ui.card():
        "Points per game 25.4, 28.9"
    with ui.card():
        "Rebounds per game 7.3, 8.3"
    with ui.card():
        "Assist per game 8.1, 6.8"

# Add a Plot to visualize data input
import matplotlib.pyplot as plt
import numpy as np

from shiny.express import input, render, ui

ui.input_slider("obs", "Number of bins:", min=10, max=100, value=30)


@render.plot
def distPlot():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)

    fig, ax = plt.subplots()
    ax.hist(x, input.obs(), density=True)
    return fig


# Install Shiny Themes Package

from shinyswatch import theme
from shiny.express import render, ui

theme.darkly()





# Add a UI Title Page And Sidebar with data information.

ui.page_opts(title="NBA OUTLOOK ON LeBron James", fillable=True)
with ui.layout_columns():
    from shiny.express import ui

with ui.sidebar(bg="#f8f8f8"):
    "Vashti's Module 6 App demonstrates LeBron James Progress 2023-2024"

"LeBron James Stats and Progress"


# Add a histogram to visualize data input
@render.plot(alt="A histogram")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)
    plt.hist(x, input.n(), density=True)


# Define LeBron James stats for the 2023 and 2023-24 NBA seasons
lebron_stats_2023 = {
    "Season": "2023",
    "Points per game": 28.9,
    "Rebounds per game": 8.3,
    "Assists per game": 6.8,
    "All-Star Games": 19,
}

lebron_stats_2024 = {
    "Season": "2023-24",
    "Points per game": 25.4,
    "Rebounds per game": 7.3,
    "Assists per game": 8.1,
    "Field Goal Percentage": 53.6,
}

# Print the stats
print("LeBron James Stats (2023-24):")
for key, value in lebron_stats_2023.items():
    print(f"{key}: {value}")

# Add UI card display
ui.page_opts(fillable=True)

with ui.layout_columns():
    with ui.card():
        "Points per game 25.4, 28.9"
    with ui.card():
        "Rebounds per game 7.3, 8.3"
    with ui.card():
        "Assist per game 8.1, 6.8"

# Define the Shiny UI Page layout - Page Options

# Call the ui.page_opts() function
# Set title to a string in quotes that will appear at the top
# Set fillable to True to use the whole page width for the UI

ui.page_opts(title="NBA Express: Stat Data (Update)", fillable=True)

# Define the Shiny UI Page layout - Sidebar

with ui.sidebar(open="open"):
    ui.h2("Vashti's Module 6 App", class_="text-center")

    ui.p(
        "A demonstration of an NBA Player's Progress.",
        class_="text-center",
    )

    ui.hr()

    ui.h6("Links:")

    ui.a(
        "GitHub Source",
        href="https://https://github.com/Vashti259/cintel-05-cintel",
        target="_blank",
    )

    ui.a(
        "GitHub App",
        href="https://https://vashti259.github.io/cintel-05-cintel//",
        target="_blank",
    )

    ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank")


