# google_forms_questionnaires
Facilitate creating long questionnaires in google forms by importing questions from an excel file

Save your time by automating forms:

1. Prepare an excel file with your questionnaire. Order your questions in one row in the very first column so that one cell corresponds to one question (don't split your questions). Make sure that your column with questions is entitled 'question' (otherwise adjust the .py scripts) - that means your A1 cell should contain text that says 'question'
2. Place the excel file that you created in your working directory
3. Make sure that you put files client_secrets.json and token.json in your working directory (you get this files when you set up your google API credentials)
4. Run .py scripts in your working directory
