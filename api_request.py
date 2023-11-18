from flask import Flask,request,jsonify
from main import file_processing


app=Flask(__name__)

@app.route("/process_excel")
def home():
    status=""
    try:
        
        file_processing('unprocessed/Final Updated_Master File Cluster Head Dashboard - 20.06.23.xlsx','processed/Final_processed.xlsx')
        status="Completed"
    except:
        status="Not COmpleted"
    return status

if __name__=='__main__':
    app.run(debug=True)