# Flask application is set to provide a UI based demonstration of how the system will work
# in the practical environment. Each time the image is submitted via a form (implies the process 
# of taking image from the camera) it is processed and a suitable timer is sent back to the front-end.
# This process would be similar to displaying countdown in a traffic system.

from flask import Flask, render_template, request
import vehiclecounter

app = Flask(__name__)

def predict_label(img_path):
# Function which takes image file name and returns the countdown
# The number of vehicles will be stored in x
# If the number of vehicles is less than 7, the countdown will be 15
# If it is more than 7 and less than 15, the countdown will be 30
# If it is more than 15, the countdown will be 60

	x = vehiclecounter.count_vehicle(img_path)
	if x < 7:
		return 15
	elif x < 15:
		return 30
	else:
		return 60


# Routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/submit", methods = ['GET', 'POST'])
# This is the endpoint through which images are fed into the system
# Processing and response is sent from this function
def get_output():
	if request.method == 'POST':
		try:
			# This handles the images from side 1
			img = request.files['my_image']
			img_path = "static/" + img.filename
			img.save(img_path)
			print(img_path)
			p = predict_label(img_path)
			print(p)
			return render_template("index.html", prediction1=p, img_path1=img_path)
		
		except:
			# This handles the images from side 2
			img = request.files['my_image1']
			img_path = "static/" + img.filename
			img.save(img_path)
			print(img_path)
			p = predict_label(img_path)
			print(p)
			return render_template("index.html", prediction2 = p, img_path2 = img_path)


if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)