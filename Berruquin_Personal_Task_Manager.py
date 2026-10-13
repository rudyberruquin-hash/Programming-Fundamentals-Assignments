"""
Personal Task Manager
Tier Level: Base Level
ADate: October 11, 2026
Description: A SQLite-based task management system that allows users to add, 
             retrieve, update, and delete tasks with persistent storage.

"""

import sqlite3


def create_connection(db_file):
    """
    Opens or creates a SQLite database connection.
    
    Arguments:
        db_file: String filename for the database
        
    Returns:
        Connection object if successful, None if error occurs
    """
    try:
        # Attempt to connect to the database file
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        # Print descriptive error message if connection fails
        print(f"Error connecting to database: {e}")
        return None


def setup_database(conn):
    """
    Creates the tasks table if it does not already exist.
    
    Arguments:
        conn: Active database connection object
    """
    try:
        # Create a cursor to execute SQL statements
        cursor = conn.cursor()
        
        # Define the tasks table schema
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            priority TEXT DEFAULT 'Medium',
            status TEXT DEFAULT 'Pending',
            due_date TEXT,
            project_id INTEGER
        )
        """
        
        # Execute CREATE TABLE statement
        cursor.execute(create_table_sql)
        
    except sqlite3.Error as e:
        print(f"Error setting up database: {e}")


def add_task(conn, title, description, priority, due_date):
    """
    Inserts a new task into the tasks table.
    
    Arguments:
        conn: Active database connection
        title: Task title (required)
        description: Task description (optional)
        priority: Priority level (High, Medium, Low)
        due_date: Due date in YYYY-MM-DD format
        
    Returns:
        ID of newly created task, or None if error occurs
    """
    try:
        cursor = conn.cursor()
        
        # Use parameterized query with ? placeholders
        insert_sql = """
        INSERT INTO tasks (title, description, priority, status, due_date, project_id)
        VALUES (?, ?, ?, 'Pending', ?, ?)
        """
        
        # Pass None for project_id at Base Level
        cursor.execute(insert_sql, (title, description, priority, due_date, None))
        
        # Commit the transaction to save changes
        conn.commit()
        
        # Return the auto-generated ID of the new row
        return cursor.lastrowid
        
    except sqlite3.Error as e:
        print(f"Error adding task: {e}")
        return None


def get_all_tasks(conn):
    """
    Retrieves all tasks ordered by priority and due date.
    
    Arguments:
        conn: Active database connection
        
    Returns:
        List of task tuples, or empty list if error/no data
    """
    try:
        cursor = conn.cursor()
        
        # Select all columns, ordered by priority then due date
        select_sql = "SELECT * FROM tasks ORDER BY priority, due_date"
        cursor.execute(select_sql)
        
        # Fetch all rows as a list of tuples
        return cursor.fetchall()
        
    except sqlite3.Error as e:
        print(f"Error retrieving tasks: {e}")
        return []


def get_tasks_by_status(conn, status):
    """
    Retrieves all tasks with a specific status.
    
    Arguments:
        conn: Active database connection
        status: Status string to filter by (Pending, In Progress, Done)
        
    Returns:
        List of matching task tuples
    """
    try:
        cursor = conn.cursor()
        
        # Use parameterized WHERE clause for filtering
        select_sql = "SELECT * FROM tasks WHERE status = ? ORDER BY priority"
        cursor.execute(select_sql, (status,))
        
        return cursor.fetchall()
        
    except sqlite3.Error as e:
        print(f"Error retrieving tasks by status: {e}")
        return []


def update_task_status(conn, task_id, new_status):
    """
    Updates the status of a specific task.
    
    Arguments:
        conn: Active database connection
        task_id: ID of the task to update
        new_status: New status value
        
    Returns:
        True if a row was updated, False otherwise
    """
    try:
        cursor = conn.cursor()
        
        # Use parameterized UPDATE with WHERE clause
        update_sql = "UPDATE tasks SET status = ? WHERE id = ?"
        cursor.execute(update_sql, (new_status, task_id))
        
        # Commit the change
        conn.commit()
        
        # Check if any row was actually modified
        return cursor.rowcount > 0
        
    except sqlite3.Error as e:
        print(f"Error updating task status: {e}")
        return False


def delete_task(conn, task_id):
    """
    Deletes a task from the database.
    
    Arguments:
        conn: Active database connection
        task_id: ID of the task to delete
        
    Returns:
        True if a row was deleted, False otherwise
    """
    try:
        cursor = conn.cursor()
        
        # Use parameterized DELETE with WHERE clause
        delete_sql = "DELETE FROM tasks WHERE id = ?"
        cursor.execute(delete_sql, (task_id,))
        
        # Commit the deletion
        conn.commit()
        
        # Check if any row was actually deleted
        return cursor.rowcount > 0
        
    except sqlite3.Error as e:
        print(f"Error deleting task: {e}")
        return False


def display_tasks(tasks):
    """
    Displays a formatted table of tasks.
    
    Arguments:
        tasks: List of task tuples from database query
    """
    # Check if the list is empty
    if not tasks:
        print("No tasks found.")
        return
    
    # Print header row with column labels
    print(f"{'ID':<5} {'Title':<25} {'Priority':<10} {'Status':<12} {'Due Date':<12}")
    print("-" * 70)
    
    # Print each task row with proper formatting
    for task in tasks:
        task_id = task[0]
        # Truncate title to 25 characters
        title = task[1][:25] if len(task[1]) > 25 else task[1]
        priority = task[3] if task[3] else "N/A"
        status = task[4] if task[4] else "N/A"
        due_date = task[5] if task[5] else "N/A"
        
        # Use f-string format specifiers for column alignment
        print(f"{task_id:<5} {title:<25} {priority:<10} {status:<12} {due_date:<12}")


# Main Program*********

if __name__ == "__main__":
    # Step 1: Create database connection
    conn = create_connection("tasks.db")
    
    if conn is None:
        print("Failed to create database connection. Exiting.")
        exit(1)
    
    # Step 2: Set up the database schema
    setup_database(conn)
    
    # Step 3: Add six sample tasks with varied priorities and due dates
    print("Adding tasks...")
    task2_id = add_task(conn, "Install new fire extinguishers in characterized controlled areas", "Perform pre-job survey to confirm characterization ", "Low", "2026-10-17")
    print(f"Task added with ID: {task2_id}")

    task3_id = add_task(conn, "Week 7 programming assignment", "Write a draft programming script", "High", "2026-10-08")
    print(f"Task added with ID: {task3_id}")

    task4_id = add_task(conn, "Administer pets meds", "Pick-up Zula and Alaska’s meds", "High", "2026-10-10")
    print(f"Task added with ID: {task4_id}")

    task5_id = add_task(conn, "Team meeting prep", "Prepare safety talk for weekly meeting ", "Medium", "2026-10-18")
    print(f"Task added with ID: {task5_id}")

    task6_id = add_task(conn, "Long run", "Get ready to run 7.5 miles", "Low", "2026-10-13")
    print(f"Task added with ID: {task6_id}")
    
    print()
    
    # Step 4: Display all tasks
    print("=== All Tasks ===")
    all_tasks = get_all_tasks(conn)
    display_tasks(all_tasks)
    print()
    
    # Step 5: Display only Pending tasks
    print("=== Pending Tasks ===")
    pending_tasks = get_tasks_by_status(conn, "Pending")
    display_tasks(pending_tasks)
    print()
    
    # Step 6: Update status of one task
    print("Updating task status...")
    success = update_task_status(conn, task3_id, "In Progress")
    print(f"Status updated for task {task3_id}: {success}")
    print()
    
    # Step 7: Delete one task
    print("Deleting task...")
    deleted = delete_task(conn, task6_id)
    print(f"Task {task6_id} deleted: {deleted}")
    print()
    
    # Step 8: Display all tasks again to show changes
    print("=== All Tasks (After Updates) ===")
    final_tasks = get_all_tasks(conn)
    display_tasks(final_tasks)
    print()
    
    # Step 9: Close the database connection
    conn.close()
    print("Database connection closed.")