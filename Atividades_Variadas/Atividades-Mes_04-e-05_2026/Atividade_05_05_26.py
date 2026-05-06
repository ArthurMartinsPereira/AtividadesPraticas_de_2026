# Atividade Sistema de Recomendação de Hábitos Inteligente:

PERIOD_MAP = {
    "manha": 0,
    "tarde": 1,
    "noite": 2
}


class Activity:
    def __init__(self, name, category, energy_required):
        self.name = name
        self.category = category
        self.energy_required = energy_required

    def __repr__(self):
        return f"Activity(name={self.name}, energy={self.energy_required})"


class LogEntry:
    def __init__(self, activity, period_of_day, mood, energy, duration):
        if period_of_day not in PERIOD_MAP:
            raise ValueError(f"Período inválido: {period_of_day}")

        self.activity = activity
        self.period_of_day = period_of_day
        self.mood = mood
        self.energy = energy
        self.duration = duration

    def get_numeric_period(self):
        return PERIOD_MAP[self.period_of_day]

    def __repr__(self):
        return f"{self.activity.name} | {self.period_of_day} | mood={self.mood} | energy={self.energy}"


class HabitTracker:
    def __init__(self):
        self.logs = []

    def add_entry(self, log):
        self.logs.append(log)

    def get_all_entries(self):
        return self.logs

    def to_dataset(self):
        X = []
        y = []
        activity_map = {}
        current_id = 0

        for log in self.logs:
            activity_name = log.activity.name

            if activity_name not in activity_map:
                activity_map[activity_name] = current_id
                current_id += 1

            activity_id = activity_map[activity_name]

            features = [
                log.energy,
                log.mood,
                log.get_numeric_period()
            ]

            X.append(features)
            y.append(activity_id)

        return X, y, activity_map

    def __repr__(self):
        return f"HabitTracker(total_logs={len(self.logs)})"

    def __len__(self):
        return len(self.logs)


# Criando atividades
activity1 = Activity("Estudar", "Produtivo", 7)
activity2 = Activity("Treinar", "Saúde", 8)
activity3 = Activity("Ler", "Lazer", 4)

# Criando logs
log1 = LogEntry(activity1, "noite", 6, 7, 60)
log2 = LogEntry(activity2, "manha", 8, 9, 45)
log3 = LogEntry(activity1, "noite", 7, 8, 90)
log4 = LogEntry(activity3, "tarde", 5, 4, 30)

# Criando tracker
tracker = HabitTracker()
tracker.add_entry(log1)
tracker.add_entry(log2)
tracker.add_entry(log3)
tracker.add_entry(log4)

# Exibindo logs
print("=== LOGS ===")
for log in tracker.get_all_entries():
    print(log)

# Dataset para ML
X, y, activity_map = tracker.to_dataset()

print("\n=== DATASET ===")
print("X:", X)
print("y:", y)
print("Activity Map:", activity_map)
