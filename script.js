document.addEventListener('DOMContentLoaded', (event) => {
            const taskForm = document.getElementById('taskForm');
            const taskTitle = document.getElementById('taskTitle');
            const viewTasksButton = document.getElementById('viewTasksButton');

            // Function to view all tasks
            function viewTasks() {
                console.log("Fetching tasks...");
                fetch('/tasks')
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Network response was not ok');
                        }
                        return response.json();
                    })
                    .then(data => {
                        console.log("Tasks fetched:", data);
                        let tasksList = document.getElementById('tasks');
                        tasksList.innerHTML = '';
                        data.forEach(task => {
                            let li = document.createElement('li');
                            li.textContent = `${task.title} (Completed: ${task.completed})`;

                            let deleteButton = document.createElement('button');
                            deleteButton.textContent = 'Delete';
                            deleteButton.onclick = function() {
                                deleteTask(task.id);
                            };

                            li.appendChild(deleteButton);
                            tasksList.appendChild(li);
                        });
                    })
                    .catch(error => console.error('Error:', error));
            }