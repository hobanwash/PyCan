import os
import subprocess
from flask import Flask, render_template_string
import tempfile

app = Flask(__name__)

@app.route('/')
def run_python_script():
    # Specify the path to the Python script you want to run
    script_path = 'your_script.py'  # Change this to the path of your script
    
    try:
        # Run the external Python script using subprocess
        result = subprocess.run(['python', script_path], capture_output=True, text=True)

        # Check if there was any error in running the script
        if result.returncode != 0:
            # If error occurs, return the error message
            return f"Error running the script: {result.stderr}"

        # Otherwise, return the standard output of the script
        return render_template_string("""
            <h1>Python Script Output</h1>
            <pre>{{ output }}</pre>
        """, output=result.stdout)
    
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
