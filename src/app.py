from flask import Flask, render_template, request
import vehiclecounter

app = Flask(__name__)


def predict_label(img_path):
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
			img = request.files['my_image']
			img_path = "static/" + img.filename
			img.save(img_path)
			print(img_path)
			p = predict_label(img_path)
			print(p)
			return render_template("index.html", prediction1=p, img_path1=img_path)
		except:
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