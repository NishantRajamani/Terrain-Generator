from PySide2.QtWidgets import *   
     
window = QWidget()
window.setGeometry(500,200,250,400)
window.setMaximumHeight(500)
window.setMaximumWidth(300)
window.setWindowTitle("Terrain Generator")

h1box = QVBoxLayout()

# Slider 1
lbscale = QLabel("Scale")
slider1 = QSlider()
slider1.setOrientation(Qt.Horizontal)
slider1.setTickPosition(QSlider.TicksBelow)
slider1.setTickInterval(10)
slider1.setMinimum(0)
slider1.setMaximum(10)
h1box.addWidget(lbscale)
h1box.addWidget(slider1)
window.setLayout(h1box)


# Slider 2
slider2 = QSlider()
lboct = QLabel("Octaves")
slider2.setOrientation(Qt.Horizontal)
slider2.setTickPosition(QSlider.TicksBelow)
slider2.setTickInterval(10)
slider2.setMinimum(0)
slider2.setMaximum(10)
h1box.addWidget(lboct)
h1box.addWidget(slider2)


# Slider 3
slider3 = QSlider()
lbper = QLabel("Persistence")
slider3.setOrientation(Qt.Horizontal)
slider3.setTickPosition(QSlider.TicksBelow)
slider3.setTickInterval(10)
slider3.setMinimum(0)
slider3.setMaximum(10)
h1box.addWidget(lbper)
h1box.addWidget(slider3)


# Slider 4
slider4 = QSlider()
lblac = QLabel("Lacunarity")
slider4.setOrientation(Qt.Horizontal)
slider4.setTickPosition(QSlider.TicksBelow)
slider4.setTickInterval(10)
slider4.setMinimum(0)
slider4.setMaximum(10)
h1box.addWidget(lblac)
h1box.addWidget(slider4)

# Generate Image button
GenImgBtn = QPushButton("Generate Image")
h1box.addWidget(GenImgBtn)

# Generate button
GenBtn = QPushButton("Generate")
h1box.addWidget(GenBtn)


window.show()