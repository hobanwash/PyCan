from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello():
    # Create a simple DataFrame
    data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
    df = pd.DataFrame(data)

    # Perform some calculation
    df['C'] = df['A'] + df['B']  # Adding two columns

    # Convert the DataFrame to HTML and return it
    return df.to_html()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

