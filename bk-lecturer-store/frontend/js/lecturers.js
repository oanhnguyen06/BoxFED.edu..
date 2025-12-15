const data = [
  {
    name: "PGS.TS. Lê Hiếu Học",
    role: "Trưởng khoa",
    unit: "Khoa KH&CN Giáo dục, ĐHBK Hà Nội",
    img: "assets/img/le_hieu_hoc.jpg"
  },
  {
    name: "PGS.TS. Phạm Thị Thanh Hải",
    role: "Phó Trưởng khoa, GV cao cấp",
    unit: "Khoa KH&CN Giáo dục, ĐHBK Hà Nội",
    img: "assets/img/thanh_hai.jpg"
  },
  {
    name: "TS. Nguyễn Thị Huyền",
    role: "Giảng viên / GĐ CTĐT",
    unit: "CN Giáo dục, ĐHBK Hà Nội",
    img: "assets/img/nguyen_thi_huyen.jpg"
  },
  {
    name: "ThS. Bùi Ngọc Sơn",
    role: "Giảng viên",
    unit: "Viện Sư phạm KT, ĐHBK Hà Nội",
    img: "assets/img/bui_ngoc_son.jpg"
  }
];

const list = document.getElementById("lecturer-list");

data.forEach(l => {
  list.innerHTML += `
    <div class="card">
      <img src="${l.img}">
      <h3>${l.name}</h3>
      <div class="role">${l.role}</div>
      <div class="unit">${l.unit}</div>
    </div>
  `;
});

