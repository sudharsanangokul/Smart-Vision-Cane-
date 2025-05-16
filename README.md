# Smart-Vision-Cane

### **1.Structure of project directory:**

```
smart-vision-cane/
│
├── yolov5/                      # Cloned YOLOv5 repo
│   ├── detect.py
│   ├── train.py
│   └── ...
├── dataset/                     # Your training dataset (optional in repo)
│   ├── images/
│   ├── labels/
│   └── data.yaml
├── best.pt                      # Trained model weights
├── picamera_detect.py          # Your live detection script
├── requirements.txt            # Required Python packages
├── README.md                   # Project overview and usage guide
├── LICENSE                     # Optional license file
└── web/                        # Web streaming server (if implemented)
    ├── app.py
    └── templates/
        └── index.html
```

---

### **2. Create a GitHub Repository**

1. Go to [GitHub](https://github.com) and create a new repository (e.g., `smart-vision-cane`).
2. Don’t initialize it with a README or license (you’ll add these manually).

---

### **3. Initialize Git Locally**

```bash
cd ~/smart-vision-cane  # Navigate to your project folder
git init
git remote add origin https://github.com/your-username/smart-vision-cane.git
```

---

### **4. Create a `.gitignore` File**

Inside your root folder, create a `.gitignore` file:

```bash
touch .gitignore
```

Add the following content:

```plaintext
__pycache__/
*.pyc
*.pt
*.zip
dataset/
.env
yolo5-env/
```

---

### **5. Add Project Files to Git**

```bash
git add .
git commit -m "Initial commit - Smart Vision Cane project"
```

---

### **6. Push to GitHub**

```bash
git branch -M main
git push -u origin main
```

---

### **7. Add a Descriptive README.md**

Make sure your `README.md` includes:

* 🔹 Project title
* 🔹 Short description
* 🔹 Hardware used (Raspberry Pi, camera module, ultrasonic sensor, etc.)
* 🔹 Model details (YOLOv5, dataset size, classes)
* 🔹 How to install dependencies
* 🔹 How to run `picamera_detect.py`
* 🔹 Optionally, link to demo videos

---

### **8. Optional: Upload `best.pt` to Google Drive and Share**

If the model is large, upload `best.pt` to Google Drive and just place the download link in your `README.md`.

---
