import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class FitnessTracker:
    def __init__(self):
        self.activities = []

    def Sample(self): 
        s = []
        print("Example Function")
        print("This is a sample function inside the FitnessTracker class.")

        a = [
            "=========================",
            "Date :- 2023-10-01",
            "Activity :- Running",
            "Duration :- 30 mins",
            "Calories :- 200 kcal",
            "=========================",
            
            "\n=========================",
            "Date :- 2023-10-02",
            "Activity :- Cycling",
            "Duration :- 45 mins",
            "Calories :- 300 kcal",
            "=========================",
        ]

        s.append(a)

        for i in s:
            for j in i:
                print(j)

        return s

        
    def add_activity(self):
        try:
            date = input("Enter Date (YYYY-MM-DD): ").strip()
            datetime.strptime(date, "%Y-%m-%d")

            name = input("Enter Activity Name (Ex. Running, Gym): ").strip().capitalize()
            if not name:
                print("Invalid activity name")
                return

            duration = float(input("Duration (mins): "))
            calories = float(input("Calories burned: "))

            if duration <= 0 or calories <= 0:
                print("Duration and calories must be positive values")
                return

            self.activities.append({
                "date": date,
                "activity": name,
                "duration": duration,
                "calories": calories
            })

            print(" Activity added successfully")

        except ValueError:
            print("Invalid input! Use correct date format and numeric values.")

    def save_activities(self, filename='activities.csv'):
        df = pd.DataFrame(self.activities)
        df.to_csv(filename, index=False)
        print(f"Activities saved to {filename}")
    def show_stats(self):
        if len(self.activities) == 0:
            print("\nNo data found")
            return

        df = pd.DataFrame(self.activities)
        print("\nSTATISTICS")
        print("Total Sessions:", len(df))
        print("Total Calories:", df['calories'].sum())
        print("Avg Duration:", df['duration'].mean())


    def save_visualizations(self):
        if not self.activities:
            print("No data to visualize")
            return
        df = pd.DataFrame(self.activities)
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        df.groupby('activity')['calories'].sum().plot(kind='bar')
        plt.title('Calories')
        plt.subplot(1, 2, 2)
        df_sorted = df.sort_values('date')
        
        plt.plot(df_sorted['date'], df_sorted['duration'])
        plt.title('Trends')
        plt.tight_layout()
        plt.savefig("visualization.png")
        plt.close()

        plt.plot(df_sorted['date'], df_sorted['activity'])
        plt.title('Trends')
        plt.tight_layout()
        plt.savefig("visualization.png")
        plt.close()

        plt.plot(df_sorted['activity'], df_sorted['duration'])
        plt.title('Trends')
        plt.tight_layout()
        plt.savefig("visualization.png")
        plt.close()

        plt. plot(df_sorted['activity'], df_sorted['calories'])
        plt.title('Trends')
        plt.tight_layout()  
        plt.savefig("visualization.png")
        plt.close()
        
        plt.plot(df_sorted['date'], df_sorted['calories'])
        plt.title('Trends')
        plt.tight_layout()
        plt.savefig("visualization.png")
        plt.close()

        print("Visualization saved successfully")
    
    def show_charts(self):
        if not self.activities:
            print("\nNo data to plot")
            return

        df = pd.DataFrame(self.activities)
        plt.figure(figsize=(10, 5))

        plt.subplot(1, 2, 1)
        df.groupby('activity')['calories'].sum().plot(kind='bar')
        plt.title('Calories')

        plt.subplot(1, 2, 2)
        df_sorted = df.sort_values('date')
        plt.plot(df_sorted['date'], df_sorted['duration'])
        plt.title('Trends')

        plt.tight_layout()
        plt.show()
