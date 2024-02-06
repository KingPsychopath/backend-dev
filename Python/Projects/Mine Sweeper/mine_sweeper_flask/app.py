from flask import Flask, render_template, request, redirect, url_for, session
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mine_sweeper_final import mine_sweeper
 
# Testing if same directory - import works
#board = mine_sweeper.Board(10, 10)
#board.play(True)

app = Flask(__name__)
app.secret_key = 'secret_key' # used to sign session cookies


@app.route('/', methods=['GET', 'POST'])
def index():
    error = session.pop('error', None)
    board = mine_sweeper.Board(3, 1)


    if 'board' not in session:
        session['board'] = board.to_html()

    if request.method == 'POST':
        # process the move and update the board
        # ...

        try:
            col = int(request.form.get('col'))
            row = int(request.form.get('row'))
            action = request.form.get('action')

            if action == 'flag':
                board.flag_cell(col, row)  # Replace this with your actual flagging logic
            elif action == 'reveal':
                board.reveal_cell(col, row)  # Replace this with your actual revealing logic
            # process the move and update the board
            # ...
            session['board'] = board.to_html()
        except ValueError as e:
            session['error'] = str(e), 'Please enter a valid number'
        except Exception as e:
            session['error'] = str(e)

    return render_template('index.html', board=session['board'], error=error)

if __name__ == "__main__":
    app.run(debug=True) # debug allows reloading + detailed error messages