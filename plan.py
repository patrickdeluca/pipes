import datetime
import json

class TaskPlannerPipeline:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date, priority):
        task = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "priority": priority,
            "status": "pending",
            "created_at": datetime.datetime.now().isoformat()
        }
        self.tasks.append(task)
        return task

    def list_tasks(self):
        return self.tasks

    def update_task(self, task_id, **kwargs):
        for task in self.tasks:
            if task["id"] == task_id:
                for key, value in kwargs.items():
                    if key in task:
                        task[key] = value
                return task
        return None

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        return self.tasks

    def get_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def save_tasks(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.tasks, file)

    def load_tasks(self, file_path):
        with open(file_path, 'r') as file:
            self.tasks = json.load(file)

# Example usage
if __name__ == "__main__":
    planner = TaskPlannerPipeline()
    planner.add_task("Complete report", "Finish the quarterly report", "2024-07-01", "high")
    planner.add_task("Team meeting", "Discuss project updates", "2024-06-25", "medium")
    planner.save_tasks("tasks.json")

    # Load tasks from file
    planner.load_tasks("tasks.json")
    print(planner.list_tasks())
