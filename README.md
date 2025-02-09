<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Image Name Maker</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    h1 {
      text-align: center;
    }
    .controls {
      margin-bottom: 10px;
      text-align: center;
    }
    #canvas {
      display: block;
      margin: 20px auto;
      border: 1px solid #ccc;
      max-width: 100%;
    }
    button {
      margin: 5px;
      padding: 10px 20px;
      font-size: 1em;
    }
  </style>
</head>
<body>
  <h1>Image Name Maker</h1>
  
  <!-- Image Upload -->
  <div class="controls">
    <label>
      Select Image: 
      <input type="file" id="imageInput" accept="image/*">
    </label>
  </div>
  
  <!-- Name Input -->
  <div class="controls">
    <label>
      Your Name: 
      <input type="text" id="nameInput" placeholder="Enter your name">
    </label>
  </div>
  
  <!-- Font Color Picker -->
  <div class="controls">
    <label>
      Font Color: 
      <input type="color" id="colorInput" value="#ffffff">
    </label>
  </div>
  
  <!-- Font Size Selection -->
  <div class="controls">
    <label>
      Font Size: 
      <select id="fontSizeInput">
        <option value="20">20px</option>
        <option value="30" selected>30px</option>
        <option value="40">40px</option>
        <option value="50">50px</option>
        <option value="60">60px</option>
      </select>
    </label>
  </div>
  
  <!-- Font Style Selection -->
  <div class="controls">
    <label>
      Font Style: 
      <select id="fontStyleInput">
        <option value="Arial" selected>Arial</option>
        <option value="Courier New">Courier New</option>
        <option value="Georgia">Georgia</option>
        <option value="Times New Roman">Times New Roman</option>
        <option value="Verdana">Verdana</option>
      </select>
    </label>
  </div>
  
  <!-- Buttons to Generate and Download -->
  <div class="controls">
    <button id="generateBtn">Generate Image</button>
    <button id="downloadBtn" style="display:none;">Download Image</button>
  </div>
  
  <!-- Canvas where image and text will be rendered -->
  <canvas id="canvas"></canvas>
  
  <script>
    // Get references to DOM elements
    const imageInput = document.getElementById('imageInput');
    const nameInput = document.getElementById('nameInput');
    const colorInput = document.getElementById('colorInput');
    const fontSizeInput = document.getElementById('fontSizeInput');
    const fontStyleInput = document.getElementById('fontStyleInput');
    const generateBtn = document.getElementById('generateBtn');
    const downloadBtn = document.getElementById('downloadBtn');
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');

    let uploadedImage = new Image();

    // When an image is selected, read it in as a data URL
    imageInput.addEventListener('change', function(e) {
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(event) {
        uploadedImage.src = event.target.result;
      }
      reader.readAsDataURL(file);
    });

    // When "Generate Image" is clicked, draw the image and text on the canvas
    generateBtn.addEventListener('click', function() {
      if (!uploadedImage.src) {
        alert('Please upload an image first.');
        return;
      }
      // Ensure the image is loaded
      uploadedImage.onload = function() {
        // Set canvas dimensions to match the uploaded image
        canvas.width = uploadedImage.width;
        canvas.height = uploadedImage.height;
        
        // Draw the uploaded image onto the canvas
        ctx.drawImage(uploadedImage, 0, 0);

        // Prepare text properties
        const fontSize = fontSizeInput.value;
        const fontStyle = fontStyleInput.value;
        ctx.font = `${fontSize}px ${fontStyle}`;
        ctx.fillStyle = colorInput.value;
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';

        // Get the text (name) to overlay
        const text = nameInput.value;
        if (!text) {
          alert('Please enter a name.');
          return;
        }
        
        // Calculate center position of the canvas
        const x = canvas.width / 2;
        const y = canvas.height / 2;

        // (Optional) Add a shadow effect for a more stylish look
        ctx.shadowColor = 'rgba(0, 0, 0, 0.5)';
        ctx.shadowOffsetX = 2;
        ctx.shadowOffsetY = 2;
        ctx.shadowBlur = 4;
        
        // Draw the text on the canvas
        ctx.fillText(text, x, y);

        // Reveal the download button
        downloadBtn.style.display = 'inline-block';
      }
      
      // If the image is already loaded, call onload immediately
      if (uploadedImage.complete) {
        uploadedImage.onload();
      }
    });

    // Download the final image as a PNG file
    downloadBtn.addEventListener('click', function() {
      const link = document.createElement('a');
      link.download = 'image-with-name.png';
      link.href = canvas.toDataURL();
      link.click();
    });
  </script>
</body>
</html>
