from flask import Flask, render_template
from flask import request, url_for
from flask_cors import CORS, cross_origin
from trainingModel import trainModel
import flask_monitoringdashboard as dashboard
from predictionFromModel import prediction

app = Flask(__name__)
dashboard.bind(app)
CORS(app)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index3.html')


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRouteClient():
    try:
        if request.method == 'POST':
            res_type = ", ".join(request.form.getlist('rest_type'))
            user_form_dict = {'name': request.form['name'], 'online_order': request.form['online_order'],
                              'book_table': request.form['book_table'], 'votes': request.form['votes'],
                              'location': request.form['location'], 'rest_type': res_type,
                              'cuisines': request.form['cuisines'], 'cost': request.form['cost'],
                              'menu_item': request.form.getlist('menu_item'), 'city': request.form['city']}
            prediction_of_user_data = prediction()
            predicted_data = prediction_of_user_data.predictionFromModel(user_form_dict)
            if predicted_data < 0:
                return render_template('index3.html', prediction_texts="Sorry no rating available.")
            else:
                return render_template('index3.html',
                                       prediction_text="Restaurant Rating is: {}".format(predicted_data[0]))

        else:
            return render_template('index3.html')
    except Exception as e:
        raise e


@app.route("/training", methods=['POST'])
@cross_origin()
def trainingModel():
    try:
        train_model = trainModel()
        model = train_model.trainingModel()
        return model
    except Exception as e:
        raise e


if __name__ == "__main__":
    app.run(debug=True)
