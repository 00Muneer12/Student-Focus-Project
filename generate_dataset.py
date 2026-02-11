import pandas as pd
import random
from datetime import datetime, timedelta

# Number of records you want
NUM_RECORDS = 30

start_date = datetime(2026, 2, 1)

data = []

for i in range(NUM_RECORDS):
    date = start_date + timedelta(days=i)

    # Random study start times
    start_time = random.choice(["06:30", "07:00", "08:00", "20:30", "21:00", "22:00"])

    # Study duration
    duration_min = random.choice([30, 45, 60, 75, 90])

    # Phone usage logic
    phone_used = 1 if start_time in ["20:30", "21:00", "22:00"] else random.choice([0, 1])

    # Mood level (1–5)
    mood = random.randint(2, 5)

    # Focus calculation logic
    focus_level = 5

    if phone_used == 1:
        focus_level -= 2

    if mood <= 2:
        focus_level -= 1

    if duration_min < 45:
        focus_level -= 1

    focus_level = max(1, min(5, focus_level))

    data.append([
        date.strftime("%Y-%m-%d"),
        start_time,
        duration_min,
        phone_used,
        mood,
        focus_level
    ])

# Create dataframe
df = pd.DataFrame(
    data,
    columns=[
        "date",
        "start_time",
        "duration_min",
        "phone_used",
        "mood",
        "focus_level"
    ]
)

# Save dataset
df.to_csv("student_focus_data.csv", index=False)

print("Dataset generated successfully!")
