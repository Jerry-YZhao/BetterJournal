from datetime import date
from django.shortcuts import render
from .models import Goal, Progress

def add_completed_tasks_to_progress(completed_tasks):
    goal_name_to_id = {goal.goal_name: goal.id for goal in Goal.objects.all()}

    for goal_name in completed_tasks:
        if goal_name in goal_name_to_id:
            Progress.objects.create(date=date.today(), goal_id=goal_name_to_id[goal_name], progress_value=1)
        else:
            new_goal = Goal.objects.create(goal_name=goal_name)
            goal_name_to_id[goal_name] = new_goal.id
            Progress.objects.create(date=date.today(), goal_id=new_goal.id, progress_value=1)

def get_completed_days_for_task(goal_id):
    current_date = date.today()
    completed_days = Progress.objects.filter(goal_id=goal_id, progress_value=1, date__lte=current_date).values_list('date', flat=True)
    return list(completed_days)

def task_completion_view(request):
    if request.method == 'POST':
        # Assuming the completed tasks are submitted as a list of task names
        completed_tasks = request.POST.getlist('completed_tasks')

        # Call the function to add completed tasks to the progress table
        add_completed_tasks_to_progress(completed_tasks)

    # Additional view logic and rendering here
    # ...

    return render(request, 'task_completion.html')
