# Detect the language of the unknown string based on the dictionary values.

language_data = {'French': ('Le monde de la réalité a ses limites; le monde de l\'imagination est sans frontières '
                            'L\’avenir est entre les mains de ceux qui explorent '
                            'Le monde est un livre dont chaque pas nous ouvre une page une page '
                            'Dans la vie on ne fait pas ce que l\’on veut mais on est responsable de ce que l\’on est '),

                 'English': ('This above all to thine own self be true '
                             'Did my heart love till now? Forswear it, sight! For I never saw true beauty till this night '
                             'Another page of this missing book called the happiest moment of life'),

                 'German': ('Ein jeder kehr’ vor seiner Tür, und rein ist jedes Stadtquartier'
                            'Zwei Dinge sind unendlich, das Universum und die menschliche Dummheit, '
                            'aber bei dem Universum bin ich mir noch nicht ganz sicher'
                            'Was mich nicht umbringt, macht mich stärker'),
                 }



# Method: Trying to find the most recurring language
french = 0
english = 0
german = 0
unknown_string = 'this is a page'  # English
str_list = unknown_string.split()

for i in language_data:
    j = 0
    while(j < len(str_list)):
        if(str_list[j] in language_data[i].lower()):
            if(i == 'French'):
                french += 1
            if(i == 'English'):
                english += 1
            if(i == 'German'):
                german += 1
        j += 1

if(french > english and french > german):
    print("The language is French.")
elif(english > french and english > french):
    print("The language is English")
elif(german > french and german > english):
    print("The language is German")
else:
    print("Language Not Detected")
