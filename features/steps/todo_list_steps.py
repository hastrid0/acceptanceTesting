to_do_list = []
#Feature 1
@given('the To-Do list is empty')
def step_impl(context):
    global to_do_list
    to_do_list = []

@when('the user adds a task "{task}"')
def step_impl(context, task):
    global to_do_list
    to_do_list.append(task)
    
@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    assert task in to_do_list, f'Task "{task}" not found in the to-do list'


#Feature 2
@given('the To-Do list has 3 tasks')
def step_impl(context):
    global to_do_list
    to_do_list = [
        {"id":"1","title": "Task 1", "description": "Desc 1", "completed": False},
        {"id":"2","title": "Task 2", "description": "Desc 2", "completed": False},
        {"id":"3","title": "Task 3", "description": "Desc 3", "completed": False}

    ]

@when('the user lists the tasks')
def step_impl(context):
    # Simulación, no hace nada, solo valida el paso
    pass

@then('the system display 3 tasks with their id, title, description,completed_status')
def step_impl(context):
    assert len(to_do_list) == 3
    for task in to_do_list:
        assert "id" in task and "title" in task and "description" in task
        
#Feature 3
@given('the To-Do list has a task titled "Workshop IS2" with the id "{id}"')
def step_impl(context):
    global to_do_list
    to_do_list = [
        {"id":"1","title": "Workshop IS2", "description": "Organize and vacuum", "completed": False}
    ]

@when('the user gives the task "Workshop IS2"s "{id}"')
def step_impl(context):
    for task in to_do_list:
        if task["id"] == "1":
            task["completed"] = True

@then('the task "Workshop IS2" should be marked as completed')
def step_impl(context):
    task = next((t for t in to_do_list if t["id"] == "1"), None)
    assert task is not None
    assert task["completed"] is True
    
#Feature 4
@given('the To-Do list has multiple tasks')
def step_impl(context):
    global to_do_list
    to_do_list = [
        {"id":"1","title": "One", "description": "", "completed": False},
        {"id":"2","title": "Two", "description": "", "completed": True}
    ]

@when('the user clears the to-do list')
def step_impl(context):
    global to_do_list
    to_do_list = []

@then('the to-do list should be empty')
def step_impl(context):
    assert len(to_do_list) == 0

#Feature 5
@given('the to-do list has 3 tasks and 1 is completed')
def step_impl(context):
    global to_do_list
    to_do_list = [
        {"id":"1","title": "T1", "description": "", "completed": True},
        {"id":"2","title": "T2", "description": "", "completed": False},
        {"id":"2","title": "T3", "description": "", "completed": False}
    ]

@when('the user requests the task summary')
def step_impl(context):
    context.completed = sum(t["completed"] for t in to_do_list)
    context.pending = len(to_do_list) - context.completed

@then('the system should show 1 completed and 2 pending tasks')
def step_impl(context):
    assert context.completed == 1
    assert context.pending == 2
    
#Feature 6
@given('the To-Do list has 1 task')
def step_impl(context):
    global to_do_list
    to_do_list = [
        {"id":"1","title": "Export 1", "description": "", "completed": False},
    ]

@when('the user exports the to-do list to a JSON file')
def step_impl(context):
    with open("tareas_exportadas.json", "w", encoding="utf-8") as f:
        json.dump(to_do_list, f, indent=4, ensure_ascii=False)

@then('a file named "tareas_exportadas.json" should be created with 1 task inside')
def step_impl(context):
    assert os.path.exists("exportadas_tareas.json")
    with open("tareas_exportadas.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        assert isinstance(data, list)
        assert len(data) == 2