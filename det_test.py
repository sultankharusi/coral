import os
import pathlib
from pycoral.utils import edgetpu
from pycoral.utils import dataset
from pycoral.adapters import common
from pycoral.adapters import detect
from PIL import Image



class detector:

	def __init__(self, model, label):
	# Specify the TensorFlow model, labels, and image
	
	self.model = model
	self.label = os.path.join(script_dir, 'coco_labels.txt')
	self.threshold = 0.65
	

	def inter_init(self):
	# Initialize the TF interpreter
	self.interpreter = edgetpu.make_interpreter(self.model)
	self.interpreter.allocate_tensors()

	def imglaod(self, img_file= image_file):
		#Resize the image
		size = common.input_size(interpreter)
		image = Image.open(image_file).convert('RGB').resize(size, Image.ANTIALIAS)

		return image

	def inference(self, image_file):
		image = self.imglaod(image_file)
		# Run an inference
		common.set_input(self.interpreter, image)
		self.interpreter.invoke()
		return interpreter
		
	def getclas(self):
		classes = detect.get_objects(self.interpreter, score_threshold=self.threshold)
		return classes


	def results(self, label_file, classes):
		# Print the result
		labels = dataset.read_label_file(label_file)
		
		for c in classes:
			print('%s: %.5f' % (labels.get(c.id, c.id), c.score))