
def GetStyleStartPage():
    return """
        h1 {
            text-align: center;
            display:block;
            margin-top: 1em;
            font-size: 10em;
        }
        p {
            text-align: center;
            font-size: 3em;
            display:block; 
        }
        #continue_button {
            margin: auto;
            width: 35%;
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
        }
        """


def GetStyleRulesPage():
    return """
        h1 {
            text-align: center;
            display:block;
            margin-top: 0.5em;
            font-size: 3em;
        }
        p {
            text-align: center;
            font-size: 2em;
            display:block; 
        }
        #continue_button {
            margin: auto;
            width: 35%;
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
        }
        """


def GetStyleTestsPage():
    return """
        h1 {
            text-align: center;
            display:block;
            margin-top: 0.5em;
            font-size: 3em;
        }
        p {
            text-align: center;
            font-size: 2em;
            display:block; 
        }
        #continue_button {
            margin: auto;
            width: 35%;
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
        }
        """


def GetStyleScorePage():
    return """
        h1 {
            text-align: center;
            display:block;
            margin-top: 0.5em;
            font-size: 3em;
        }
        p {
            text-align: center;
            font-size: 2em;
            display:block; 
        }
        #continue_button {
            margin: auto;
            width: 35%;
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
        }
        """


def GetStyleRecommendationPage():
    #TODO find a way to change the size of the buttons (normal sizing does not work,
    # since the buttons are in a gradio row). maybe change gradio row size?
    return """
        h1 {
            text-align: center;
            display:block;
            margin-top: 0.5em;
            font-size: 3em;
        }
        p {
            text-align: center;
            font-size: 2em;
            display:block; 
        }
        #continue_button {
            margin: auto;
            width: 30%;
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
        }
        #go_back_button {
            margin: auto;
            width: 30%;
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
        }
        """


def GetStyleEstimationPage():
    #TODO find a way to change the size of the buttons (normal sizing does not work,
    # since the buttons are in a gradio row). maybe change gradio row size?
    return """
        h1 {
            text-align: center;
            display:block;
            margin-top: 0.5em;
            font-size: 3em;
        }
        p {
            text-align: center;
            font-size: 2em;
            display:block; 
        }
        #continue_button {
            margin: auto;
            width: 30%;
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
        }
        #go_back_button {
            margin: auto;
            width: 30%;
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
        }
        """
