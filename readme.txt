Welcome to the 
Incident Clustering Analysis Tool!
------------------------------------
------------------------------------

What's new?

With the development of a new front-end interface, 
users no longer have to directly interact with the codebase to run the model as the app now offers a more user-friendly interface, 
facilitating the transition from a technical notebook to a user-oriented experience.

------------------------------------
------------------------------------

Reminders for installation & running the model

1. Install the VSCode Python Extension 
2. Install C++ Builder Tools: https://visualstudio.microsoft.com/visual-cpp-build-tools/
3. Make sure to $ pip install -r requirements.txt
4. Once all of these are done, you can run the model $ streamlit run run_model.py

------------------------------------
------------------------------------

Common Issues & Watch-outs

1. Running the "train_model_ul.ipynb" Notebook and you get an ‘SSLCertVerificationError' error, 
    This may be a Network issue especially if you are working from home, 
        (a) you may want to run the Notebook in the office connected to P&G Network 
        (b) or disable Zscaler but this will need a code from network team

2. 'Unpickling error' - 
    This means that the pkl file for the model was corrupted options
        (a) retrain the model in 'train_model_ul.ipynb'
        (b) download the model from: https://pgone.sharepoint.com/:u:/s/FY2324PHInternship-LexUy/EQUUmLCjJfRMv4b9ntZuBUoBKPVft4KaE-YcbmGwEdC7WA?e=O9iapD
            then replace the pkl file in this folder.

------------------------------------
------------------------------------

Want to know more? Have questions/concerns? Contact:
Alvin Religioso - religioso.ad@pg.com
Lexine Uy - uy.lr@pg.com