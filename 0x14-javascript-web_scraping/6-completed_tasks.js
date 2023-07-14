#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2]; // Read the API URL from the command line arguments

request(apiUrl, { json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (res.statusCode !== 200) {
    console.error(`Error: ${res.statusCode} - ${res.statusMessage}`);
    return;
  }

  // Filter the tasks for completed tasks
  const completedTasks = body.filter((task) => task.completed);

  // Compute the number of completed tasks per user ID
  const completedTasksCount = {};
  completedTasks.forEach((task) => {
    const userId = task.userId;
    completedTasksCount[userId] = completedTasksCount[userId] ? completedTasksCount[userId] + 1 : 1;
  });

  // Print the number of completed tasks per user ID
  Object.entries(completedTasksCount).forEach(([userId, count]) => {
    console.log(`User ID: ${userId} - Completed Tasks: ${count}`);
  });
});
