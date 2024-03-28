# Gradio-App-for-Inferring-CBR-knowledge
## Description
This project is an interactive application for inferring Case-Base-Reasoner's knowledge based on the work of Murena and Al-Ghossein ("Inferring Case-Based Reasoner's Knowledge to Enhance Interactivity", 2021). 
This app let's a user take tests on given data, calculates a score and showcases the results of the inferrence-process in form of tables.
---
## Functionality
- pip install requirements.txt
- uvicorn app:app --reload

Before using the code, please make sure that you have a local instance of MySqlServer running.
Maybe the connection part has to be adjusted depending on the Server.
The Server should have a Database named CaseDB.
---
## TODO
- displaying a second score after redoing the tests. So far only the first score is displayed.
- starting a new run via the "quit-button" instead of reloading the application. 
- create visual themes for individual applications.

