async function addTodo() {
  const input = document.getElementById("todo-input");
  const title = input.value.trim();
  if (!title) return;

  const res = await fetch("/add", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title })
  });
  const data = await res.json();

  if (data.success) {
    input.value = "";
    const t = data.todo;
    const list = document.getElementById("todo-list");
    const empty = document.querySelector(".empty-msg");
    if (empty) empty.remove();

    const li = document.createElement("li");
    li.className = "todo-item";
    li.id = `item-${t.id}`;
    li.innerHTML = `
      <input type="checkbox" onchange="toggleTodo(${t.id})"/>
      <div class="todo-text">
        <span class="title">${t.title}</span>
        <span class="date">${t.created_at}</span>
      </div>
      <button class="delete-btn" onclick="deleteTodo(${t.id})">✕</button>
    `;
    list.prepend(li);
  }
}

async function toggleTodo(id) {
  await fetch(`/toggle/${id}`, { method: "POST" });
  document.getElementById(`item-${id}`).classList.toggle("done");
}

async function deleteTodo(id) {
  await fetch(`/delete/${id}`, { method: "DELETE" });
  document.getElementById(`item-${id}`).remove();
}

document.getElementById("todo-input").addEventListener("keydown", e => {
  if (e.key === "Enter") addTodo();
});
