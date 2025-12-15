const API_BASE = "http://localhost:8000";

/* ===== THÊM GIẢNG VIÊN ===== */
document.getElementById("lecturer-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const data = {
    name: document.getElementById("name").value,
    title: document.getElementById("title").value,
    role: document.getElementById("role").value,
    unit: document.getElementById("unit").value,
    major: document.getElementById("major").value,
    image: document.getElementById("image").value
  };

  const res = await fetch(`${API_BASE}/admin/add-lecturer`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  const result = await res.json();
  document.getElementById("status").innerText = result.message;
});

/* ===== UPLOAD CSV ===== */
async function uploadCSV() {
  const fileInput = document.getElementById("csvFile");
  if (!fileInput.files.length) {
    alert("Vui lòng chọn file CSV");
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  const res = await fetch(`${API_BASE}/admin/upload-csv`, {
    method: "POST",
    body: formData
  });

  const result = await res.json();
  document.getElementById("status").innerText = result.status;
}

