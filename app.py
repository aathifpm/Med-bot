from flask import Flask, render_template, request, jsonify
import os
import json
from werkzeug.utils import secure_filename
from gpt import med_bot,wound_bot,tab_bot

app = Flask(__name__)

UPLOAD_FOLDER = 'uploaded_images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

wound_dict = {
    'Abrasions': 'Abrasions',
    'Bruises': 'Bruises',
    'Burns': 'Burns',
    'Cut': 'Cut',
    'Ingrown_nails': 'Ingrown Nails',
    'Laceration': 'Laceration',
    'Stab_wound': 'Stab Wound'
}
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/chat', methods=['POST'])
def chat():
    if request.content_type == 'application/json':
        user_message = request.json.get('message')
        bot_message = med_bot(user_message=user_message)
        print(bot_message)
        return bot_message
    else:
        print("Hi")
        print(request.json.get('message'))
        return jsonify({"response": "Unsupported media type"}), 415


@app.route('/wound-detection', methods=['POST'])
def wound_detection():
    # Ensure that the Content-Type is multipart/form-data
    if 'multipart/form-data' in request.content_type:
        user_message = request.form.get('message')
        image_file = request.files.get('image')

        if image_file and allowed_file(image_file.filename):
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(image_path)
            from main import predict_image
            image_data = predict_image()
            list_of_aids = wound_bot(wounds=image_data)

            bot_message = (
                f"The Image is Recognised as:{wound_dict[image_data]}\n The First Aid Steps are:\n"
                f"{list_of_aids[0]}\n"
                f"{list_of_aids[1]}\n"
                f"{list_of_aids[2]}\n"
                f"{list_of_aids[3]}\n"
                f"{list_of_aids[4]}"
            )

        else:
            bot_message = "No valid image uploaded. Processing wound detection..."

        return jsonify({"response": bot_message})
    else:
        return jsonify({"response": "Unsupported media type"}), 415

@app.route('/custom-feature', methods=['POST'])
def custom_feature():
    if request.content_type == 'application/json':

        user_message = request.form.get('message')
        response = tab_bot(user_message)
        medicines=response['Medicines']
        precaution = response['Precautions']
        workout = response['Workout Recommendation']
        diet = response['Diet']
        print(response)
        bot_message = (
            f"Necessary Medication \n\n 1.{medicines[0]}\n"
            f"2.{medicines[1]}\n"
            f"3.{medicines[2]}\n"
            f"4.{medicines[3]}\n\n"
            f"Precaution Needs to be Taken\n\n1.{precaution[0]}\n"
            f"2.{precaution[1]}\n"
            f"3.{precaution[2]}\n"
            f"4.{precaution[3]}\n\n"
            f"WorkOut Plans\n\n1.{workout[0]}\n"
            f"2.{workout[1]}\n"
            f"3.{workout[2]}\n"
            f"4.{workout[3]}\n\n"
            f"Dietary Plans\n\n1.{diet[0]}\n"
            f"2.{diet[1]}\n"
            f"3.{diet[2]}\n"
            f"4.{diet[3]}\n"


        )
        return jsonify({"response": bot_message})

    else:

        return jsonify({"response": "Unsupported media type"}), 415

if __name__ == '__main__':
    app.run(debug=True)
