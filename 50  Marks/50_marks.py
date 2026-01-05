# Import the class from your Packages folder
from py_compile import main
from Packages import Fitness_Tracker
tracker = Fitness_Tracker.FitnessTracker()
    
while True:
    print("=========================")
    print("\n--- FITNESS TRACKER ---")
    print("=========================")
    print("=========================")
    print("1. Add Activity")
    print("2. View Stats")
    print("3. View Charts")
    print("4. Save Activities")
    print("5. Save Visualizations")
    print("6. Exit")
    print("=========================")
    
    print("=========================")
    choice = int(input("Enter Your Options :-  "))
    print("=========================")
    
    if choice == 1:
        print("=========================")
        tracker.Sample()
        print("=========================")
        
        tracker.add_activity()
        print("=========================")
    
    elif choice == 2:
        print("=========================")
        tracker.show_stats()
        print("=========================")
    elif choice == 3:
        tracker.show_charts()
    elif choice == 4:
        tracker.save_activities()
    elif choice == 5:
        tracker.save_visualizations()
    elif choice == 6:
        break
    else:
        print("Invalid choice.")

