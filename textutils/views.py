from django.shortcuts import render

def home(request):
    return render(request,'home.html',)

def analyze(request):


    analyse_me = request.POST.get('text', 'default')    # To get the entered text

    punc_remove = request.POST.get('removepunc' , 'off')      # To get status of removepunc checkbox

    to_remove_newline = request.POST.get('newline_remove' , 'off')      # To get status of newline_remove checkbox

    to_capital = request.POST.get('capitalise','off')   # To get status of capitalise checkbox

    to_countchar = request.POST.get('countchar','off')   # To get status of Count characters checkbox
    characters=0
    purpose=""


    if punc_remove =="on" :
       punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
       analysed_text = ""

       for char in analyse_me:

           if char not in punctuations:

               analysed_text = analysed_text + char
       purpose += " | removed punctuations"
       analyse_me=analysed_text
       parameters = {'purpose':purpose , 'analysedd':analyse_me ,'counted_char':characters}




    if (to_remove_newline == "on") :

        analysed_text = ""

        for char in analyse_me:

            if not(char == '\n'and char == '\r') :

                analysed_text = analysed_text + char

        purpose += " | capitalising the text"
        analyse_me=analysed_text
        parameters = {'purpose' :purpose , 'analysedd':analyse_me , 'counted_char':characters}




    if to_capital == "on":

        analysed_text = ""

        analysed_text = analyse_me.upper()

        purpose += " | capitalising the text"
        analyse_me = analysed_text
        parameters = {'purpose' :purpose, 'analysedd':analyse_me , 'counted_char':characters}



    if to_countchar == "on":
        analysed_text = 0
        analysed_text = len(analyse_me)

        characters = analysed_text
        parameters = {'purpose' :purpose, 'analysedd':analyse_me , 'counted_char':characters}



    return render(request,'analyse.html', parameters)


def about_us(request):

    return render(request,'about.html')
