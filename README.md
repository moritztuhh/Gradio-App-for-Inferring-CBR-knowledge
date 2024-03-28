# Gradio-App-for-Inferring-CBR-knowledge

## Description

This project is an interactive application for inferring Case-Base-Reasoner's knowledge based on the work of Murena and Al-Ghossein ("Inferring Case-Based Reasoner's Knowledge to Enhance Interactivity", 2021).
This app let's a user take tests on given data, calculates a score and showcases the results of the inferrence-process in form of tables.
Gradio was used for the creation of the interfaces and layouts. You can find the Gradio documentation here:
[Gradio](https://www.gradio.app/docs/interface)

## Functionality

- pip install -r requirements.txt
- uvicorn app:app --reload

Before using the code, please make sure that you have a local instance of MySqlServer running.
Maybe the connection part has to be adjusted depending on the Server.
The Server should have a Database named CaseDB.

## TODO

- displaying a second score after redoing the tests. So far only the first score is displayed.
- It also displays the score of the last run (not the current). But Score is calculated correctly.
  -->Fix: function to calculate score must be on button click to get latest run_id
- starting a new run via the "quit-button" instead of reloading the application.
- create visual themes for individual applications.
- remove duplicates from database
- find a way to display all letters
