from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import vehiclecounter

app = Flask(__name__)

def predict_label(img_path):

# function which takes image file name and returns the countdown
# the number of vehicles will be stored in x
# if the number of vehicles is less than 7, the countdown will be 15
# if it is more than 7 and less than 15, the countdown will be 30
# if it is more than 15, the countdown will be 60

	x = vehiclecounter.count_vehicle(img_path)
	if x < 7:
		return 15
	elif x < 15:
		return 30
	else:
		return 60


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		try:
			#this handles the images from side 1
			img = request.files['my_image']
			img_path = "static/" + img.filename
			img.save(img_path)
			print(img_path)
			p = predict_label(img_path)
			print(p)
			return render_template("index.html", prediction1=p, img_path1=img_path)
		except:
			#this handles the images from side 2
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