<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Tính GPA CTUT</title>
  <link rel="icon" type="image/png" href="logo.png">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">

  <style>
    body {
      font-family: 'Poppins', sans-serif;
      background: #1E1E2F;
      min-height: 100vh;
      padding: 20px;
      color: #E4E4E7;
    }
    h1 {
      color: #7A5AF5;
      font-weight: 700;
      text-shadow: 0px 0px 8px rgba(122, 90, 245, 0.6);
    }
    .subject-container {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 20px;
      margin-top: 20px;
    }
    .subject-card {
      background: #2C2C3A;
      color: #E4E4E7;
      border-radius: 20px;
      padding: 20px;
      min-width: 240px;
      max-width: 260px;
      text-align: center;
      flex: 1;
      box-shadow: 0 4px 12px rgba(0,0,0,0.5);
      transition: transform 0.2s ease;
    }
    .subject-card:hover {
      transform: translateY(-5px);
    }
    .subject-card input {
      margin-top: 10px;
      text-align: center;
      border-radius: 10px;
      border: none;
      padding: 10px;
      background: #1E1E2F;
      color: white;
    }
    .btn-custom {
      background: linear-gradient(135deg, #7A5AF5, #E86F2C);
      border: none;
      padding: 10px 25px;
      border-radius: 12px;
      font-weight: 600;
      color: white;
      box-shadow: 0 4px 12px rgba(122,90,245,0.4);
      transition: all 0.2s ease-in-out;
    }
    .btn-custom:hover {
      transform: scale(1.05);
      box-shadow: 0 6px 16px rgba(232,111,44,0.5);
    }
    .result-card {
      background: #2C2C3A;
      border-left: 6px solid #7A5AF5;
      color: #fff;
      border-radius: 20px;
      padding: 25px;
      margin-top: 30px;
      text-align: left;
      font-weight: 500;
      font-size: 1rem;
      box-shadow: 0 4px 14px rgba(0,0,0,0.6);
      display: none;
    }
    .highlight {
      color: #FBCB4A;
      font-weight: 700;
    }
    .gpa {
      color: #4AD991;
      font-weight: 700;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1 class="text-center">🎓 Tính GPA (CTUT)</h1>
    <img src="logo.png" alt="Ảnh GPA" width="100" class="d-block mx-auto my-3">

    <div class="mb-3 text-center">
      <label for="numSubjects" class="form-label fw-bold">Nhập số môn học:</label>
      <input type="number" id="numSubjects" class="form-control w-25 d-inline-block" min="1" max="20" value="3">
      <button class="btn btn-custom ms-2" onclick="createForm()">Tạo Form</button>
    </div>

    <div class="subject-container" id="gpaForm"></div>

    <div class="text-center mt-3">
      <button class="btn btn-custom" onclick="calcGPA()">👇 Tính GPA</button>
    </div>

    <div class="result-card" id="result"></div>
  </div>

  <script>
    function getGradeCTUT(score10) {
      score10 = Math.round(score10 * 10) / 10; 
      if (score10 >= 9.5) return ["A+", 4.0];
      else if (score10 >= 8.5) return ["A", 3.8];
      else if (score10 >= 8.0) return ["B+", 3.5];
      else if (score10 >= 7.0) return ["B", 3.0];
      else if (score10 >= 6.5) return ["C+", 2.5];
      else if (score10 >= 5.5) return ["C", 2.0];
      else if (score10 >= 5.0) return ["D+", 1.5];
      else if (score10 >= 4.0) return ["D", 1.0];
      else if (score10 >= 0.0) return ["F", 0.0];
      return [null, null];
    }

    function createForm() {
      const num = document.getElementById("numSubjects").value;
      const form = document.getElementById("gpaForm");
      form.innerHTML = "";

      for (let i = 0; i < num; i++) {
        form.innerHTML += `
          <div class="subject-card">
            <h5>Môn ${i+1}</h5>
            <input type="text" name="name_${i}" class="form-control" placeholder="Tên môn">
            <input type="number" name="credits_${i}" step="0.5" min="1" class="form-control" placeholder="Số tín chỉ">
            <input type="number" name="mid_${i}" step="0.1" min="0" max="10" class="form-control" placeholder="Điểm giữa kỳ">
            <input type="number" name="final_${i}" step="0.1" min="0" max="10" class="form-control" placeholder="Điểm cuối kỳ">
          </div>
        `;
      }
    }

    function calcGPA() {
      const form = document.getElementById("gpaForm");
      const inputs = form.getElementsByTagName("input");
      let subjects = [];

      for (let i = 0; i < inputs.length; i++) {
        if (inputs[i].name.startsWith("name_")) {
          let idx = inputs[i].name.split("_")[1];
          let name = inputs[`name_${idx}`]?.value || `Môn ${parseInt(idx)+1}`;
          let credits = parseFloat(inputs[`credits_${idx}`]?.value) || 0;
          let mid = parseFloat(inputs[`mid_${idx}`]?.value) || 0;
          let final = parseFloat(inputs[`final_${idx}`]?.value) || 0;

          let total = 0.4 * mid + 0.6 * final;
          let [grade, gpa4] = getGradeCTUT(total);

          subjects.push({name, credits, mid, final, total, grade, gpa4});
        }
      }

      let totalCredits = subjects.filter(s => s.grade).reduce((a, s) => a + s.credits, 0);
      if (totalCredits === 0) {
        document.getElementById("result").style.display = "block";
        document.getElementById("result").innerHTML = "⚠️ Bạn chưa nhập đầy đủ dữ liệu.";
        return;
      }

      let avg10 = subjects.reduce((a, s) => a + s.total * s.credits, 0) / totalCredits;
      let avg4 = subjects.reduce((a, s) => a + s.gpa4 * s.credits, 0) / totalCredits;

      let html = `<h4>📑 Kết quả học kỳ:</h4>`;
          subjects.forEach(s => {
            if (s.grade) {
              html += `<p><b>${s.name}</b> (${s.credits} TC): 
                Điểm 10 = <span class="highlight">${s.total.toFixed(1)}</span>, 
                Điểm chữ = <span class="fw-bold">${s.grade}</span>, 
                GPA4 = <span class="gpa">${s.gpa4.toFixed(1)}</span></p>`;
            }
          });
          html += `<hr>`;
          html += `<p><b>Điểm trung bình (thang 10):</b> <span class="highlight">${avg10.toFixed(1)}</span></p>`;
          html += `<p><b>GPA trung bình (thang 4):</b> <span class="gpa">${avg4.toFixed(2)}</span></p>`;

      document.getElementById("result").style.display = "block";
      document.getElementById("result").innerHTML = html;
    }
  </script>
</body>
</html>
