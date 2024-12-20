# src/app.py

from ui.gym_management_ui import GymManagementApp
from ui.workout_zone_ui import WorkoutZoneManagementApp
from ui.member_ui import MemberManagementApp
from ui.appointment_ui import AppointmentManagementApp
from ui.payment_ui import PaymentManagementApp
from ui.subscription_plan_ui import SubscriptionPlanManagementApp
from ui.dashboard_ui import DashboardApp
import tkinter as tk

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("St Mary's Fitness Management System")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Welcome to St Mary's Fitness Management System", font=("Helvetica", 16)).pack(pady=20)

        tk.Button(self.root, text="Gym Management", width=30, command=self.open_gym_management).pack(pady=10)
        tk.Button(self.root, text="Workout Zone Management", width=30, command=self.open_workout_zone_management).pack(pady=10)
        tk.Button(self.root, text="Member Management", width=30, command=self.open_member_management).pack(pady=10)
        tk.Button(self.root, text="Appointment Management", width=30, command=self.open_appointment_management).pack(pady=10)
        tk.Button(self.root, text="Payment Management", width=30, command=self.open_payment_management).pack(pady=10)
        tk.Button(self.root, text="Subscription Plan Management", width=30, command=self.open_subscription_plan_management).pack(pady=10)
        tk.Button(self.root, text="Staff Dashboard", width=30, command=self.open_dashboard).pack(pady=10)
        tk.Button(self.root, text="Exit", width=30, command=self.root.quit).pack(pady=10)

    def open_gym_management(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = GymManagementApp(self.new_window)

    def open_workout_zone_management(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = WorkoutZoneManagementApp(self.new_window)

    def open_member_management(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = MemberManagementApp(self.new_window)

    def open_appointment_management(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = AppointmentManagementApp(self.new_window)

    def open_payment_management(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = PaymentManagementApp(self.new_window)

    def open_subscription_plan_management(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = SubscriptionPlanManagementApp(self.new_window)

    def open_dashboard(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = DashboardApp(self.new_window)

if __name__ == "__main__":
    root = tk.Tk()
    main_app = MainApp(root)
    root.mainloop()