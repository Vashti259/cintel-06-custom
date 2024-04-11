import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly

ui.page_opts(title="NBA OUTLOOK ON LaBron James", fillable=True)
with ui.layout_columns():
    from shiny.express import ui

with ui.sidebar(bg="#f8f8f8"):
    "Vashti's Module 6 App demonstrate LeBron James Progress 2023-2024"

"Main Content"

# Create a deque by passing in a list with values
from collections import deque

temp_deque_A = deque([25, 7, 8])
len(temp_deque_A)
msft_Temperature = deque(maxlen=3)
print(temp_deque_A)

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
print("LeBron James Stats (2023):")
for key, value in lebron_stats_2023.items():
    print(f"{key}: {value}")

print("\nLeBron James Stats (2023-24):")
for key, value in lebron_stats_2024.items():
    print(f"{key}: {value}")

# Add UI card display
ui.page_opts(fillable=True)

with ui.layout_columns():
    with ui.card():
        "Points per game 25.4"
    with ui.card():
        "Rebounds per game 7.3"
    with ui.card():
        "Assist per game 8.1"


# Import Python as Shiny packages Needed
import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly

# Add a title UI Title Page

from shiny.express import ui

ui.panel_title("NBA Lebron James Stat", "Window Title")
from shiny.express import ui

# Add a sidebar
with ui.sidebar(position="left", bg="#f8f8f8"):
    "Vashti's Module 6 App"

"Demonstration of progress"
# Add Stat for Lebron James and duration

lebron_stats_2024 = {
    "Season": "2023-24",
    "Points per game": 25.4,
    "Rebounds per game": 7.3,
    "Assists per game": 8.1,
    "Field Goal Percentage": 53.6,
}

# Print the stats
print("LeBron James Stats (2023-24):")

# Create a deque by passing in a list with values
from collections import deque

temp_deque_A = deque([25, 7, 53])
len(temp_deque_A)
msft_Temperature = deque(maxlen=3)
print(temp_deque_A)


# Define the Shiny UI Page layout - Page Options

# Call the ui.page_opts() function
# Set title to a string in quotes that will appear at the top
# Set fillable to True to use the whole page width for the UI

ui.page_opts(title="NBA Express: Live Data (Basic)", fillable=True)

# Define the Shiny UI Page layout - Sidebar

with ui.sidebar(open="open"):
    ui.h2("Vashti's Antarctic Live Data", class_="text-center")

    ui.p(
        "A demonstration of real-time changes in temperature readings in Antarctica.",
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




