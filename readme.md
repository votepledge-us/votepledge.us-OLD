## Votepledge.us

This is the source code for Votepledge.us.


### Setup:
You will need to have JavaScript 5 or 6, Python 2.7, npm, and pip installed on your machine.
1. Clone the repository from Github. 
2. Open the Terminal. Enter the repository using `cd [filepath]`. You can go step by step using `ls` to see what is in the directory you are currently in and then cd into the next one until you are in the correct repository (which should be the one you cloned from Github).
3. Once in the directory, create a Python virtual environment using the command `virtualenv .venv`. Now you need to enter the environment with the command `source .venv/bin/activate`. You will see '(.venv)' appear before the command line. You will have to source the .venv every time you run the app if you have closed the terminal window since hte last time you ran it. 
4. Then, to install the necessary libraries for the Flask backend, enter `pip install -r requirements.txt` into the command line. You should only need to do this once, unless someone has updated the requirements since you last ran it. Running it again will not install redundant copies of any of the packages, so it's always okay to do this when in doubt. 
5. Now run `npm install` to install the frontend requirements. Ditto the last two sentences of step 4.
6. You now need to "build" the frontend React app using Webpack. Webpack basically creates a tree model of how all your different files are connected and combines them accordingly into a single "bundle.js". This allows you to make a single request to the server and load the whole frontend at once while also keeping all of your files modular and compact. To build, simply run `webpack` in the terminal. Keep in mind that if you make any chances to any .js or .css/.scss files, you will have to run this again.
7. Now run `python server.py` in the Terminal and go to localhost:5000 in your browser. Voilà app!