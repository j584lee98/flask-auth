const deleteTodo = (todoId) => {
  todoId = parseInt(todoId);
  fetch("/delete", {
    method: "POST",
    body: JSON.stringify({ todoId }),
  }).then((res) => {
    window.location.href = "/";
  });
};
