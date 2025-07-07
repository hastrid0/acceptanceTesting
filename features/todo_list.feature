Feature: To-Do List Management

    @addTask
    Scenario: Adding a task
        Given the To-Do list is empty
        When the user adds a task "Workshop"
        Then the to-do list should contain "Workshop"
    @ListingTask
    Scenario: Listing all de tasks
        Given the To-Do list with 3 tasks
        When the user list the task
        Then the system display the 3 task with their id, title, description,completed_status
    @MarkTaskComplete
    Scenario: Mark a task as completed
        Given the To-List with a task "Workshop IS2"
        When the user gives the task "Workshp IS1"'s id
        Then the to-do list should change the value of changed to "true"
    @CleanToDoList
    Scenario: Delete all the task
        Given the To-Do list with multiple tasks
        When the user clean the list
        Then all the task should be deleted
    @CountTask
    Scenario: Count completed and not completed task
        Given the To-Do list has 1 task completed and 2 task not completed
        When the user request the task summary
        Then the to-do list should show 1 task completed and 2 task not completed
        
    @ExportJSON
    Scenario: Export the to-do List to JSON file
        Given the To-Do list with 1 task
        When the user export the to-do list to a JSON file
        Then a file named "tareas_exportadas.json" file should be created
