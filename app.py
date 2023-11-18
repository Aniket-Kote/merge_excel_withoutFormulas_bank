from flask import Flask, request, send_file
import pandas as pd
import io

from main import file_processing

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'xlsx', 'xls'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/process_excel', methods=['POST'])
def process_excel():
    try:
        if 'file' not in request.files:
            return "No file part in the request", 400

        file = request.files['file']

        if file.filename == '':
            return "No selected file", 400

        if file and allowed_file(file.filename):
            # Perform operations on the Excel file (using pandas or any other libraries)
            # df = pd.read_excel(file)

            file_name='Final_processed.xlsx'
            file_path='./processed/'+file_name
            # Perform your operations on the dataframe here
            file_processing(file,file_path)
            # Create a BytesIO object to store the processed file in memory
            # output_stream = io.BytesIO()

            # # Example: Save the dataframe to the BytesIO object
            # # df.to_excel(output_stream, index=False)
            # # Seek to the beginning of the BytesIO stream
            # output_stream.seek(0)
            # Return the processed file as a response
            return send_file(
                file_path, as_attachment=True, download_name=file_name, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                
            )

        else:
            return "Invalid file format. Allowed formats are: xlsx, xls", 400
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
