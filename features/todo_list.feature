Feature: To-Do List Management

    @addTask
    Scenario: Adding a task
        Given the To-Do list is empty
        When the user adds a task "Workshop"
        Then the to-do list should contain "Workshop"
    @ListingTask
    Scenario: Listing all de tasks
        Given the To-Do list with 3 tasks
        When the user lists the tasks
        Then the system display the 3 task with their id, title, description,completed_status
    @MarkTaskComplete
    Scenario: Mark a task as completed
        Given the To-Do list has a task titled "Workshop IS2" with the id "{id}"
        When the user gives the task "Workshop IS2"s id
        Then the task "Workshop IS2" should be marked as completed
    @CleanToDoList
    Scenario: Delete all the task
        Given the To-Do list has multiple tasks
        When the user clears the to-do list
        Then the to-do list should be empty
    @CountTask
    Scenario: Count completed and not completed task
        Given the to-do list has 3 tasks and 1 is completed
        When the user requests the task summary
        Then the system should show 1 completed and 2 pending tasks
        
    @ExportJSON
    Scenario: Export the to-do List to JSON file
        Given the To-Do list has 1 task
        When the user exports the to-do list to a JSON file
        Then a file named "tareas_exportadas.json" file should be created with 1 task inside
