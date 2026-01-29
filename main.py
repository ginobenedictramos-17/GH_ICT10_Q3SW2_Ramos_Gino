from pyscript import display, document
#to display image: document.getElementById('idname').innerHTML: = <img src ="#">
def team_identifier(e):
    document.getElementById('output').innerHTML = ' '
    Registration = document.getElementById('register').value
    Medcert = document.getElementById('certificate').value
    GrLevel = document.getElementById('levels').value
    Section = document.getElementById('sections').value

    if Registration == 'Yes' and Medcert == 'Yes' and GrLevel == '7' and Section == 'Emerald':
        display(f'You are a member of Blue Bears and are eligible to play', target='output')

    elif Registration == 'Yes' and Medcert == 'Yes' and GrLevel == '7' and Section == 'Ruby':
        display(f'You are a member of Green Hornets and are eligible to play', target='output')    

    elif Registration == 'Yes' and Medcert == 'Yes' and GrLevel == '7' and Section == 'Sapphire':
        display(f'You are a member of Yellow Tigers and are eligible to play.', target='output')     

    elif Registration == 'Yes' and Medcert == 'Yes' and GrLevel == '7' and Section == 'Topaz':
        display(f'You are a member of Red Bulldogs and are eligible to play.', target='output')

    elif Registration == 'Yes' and Medcert == 'No' and GrLevel == '7' and Section == 'Emerald':
        display(f'You are a member of Blue Bears, but please secure a medical certificate.', target='output')         
    elif Registration == 'Yes' and Medcert == 'No' and GrLevel == '7' and Section == 'Ruby':
        display(f'You are a member of Green Hornets, but please secure a medical certificate.', target='output')        

    elif Registration == 'Yes' and Medcert == 'No' and GrLevel == '7' and Section == 'Sapphire':
        display(f'You are a member of Yellow Tigers, but please secure a medical certificate.', target='output')            

    elif Registration == 'Yes' and Medcert == 'No' and GrLevel == '7' and Section == 'Topaz':
        display(f'You are a member of Red Bulldogs, but please secure a medical certificate.', target='output')            

    elif Registration == 'No' and Medcert == 'Yes' and GrLevel == '7' and Section == 'Emerald':
        display(f'You are a member of Blue Bears but please register online to be eligible for participation', target='output')   

    elif Registration == 'No' and Medcert == 'Yes' and GrLevel == '7' and Section == 'Ruby':
        display(f'You are a member of Green Hornets but please register online to be eligible for participation', target='output')       

    elif Registration == 'No' and Medcert == 'Yes' and GrLevel == '7' and Section == 'Sapphire':
        display(f'You are a member of Yellow Tigers but please register online to be eligible for participation', target='output')       

    elif Registration == 'No' and Medcert == 'Yes' and GrLevel == '7' and Section == 'Topaz':
        display(f'You are a member of Red Bulldogs but please register online to be eligible for participation', target='output')

    elif Registration == 'No' and Medcert == 'No' and GrLevel == '7' and Section == 'Emerald':
        display(f'Register first before being able to participate', target='output')   

    elif Registration == 'No' and Medcert == 'No' and GrLevel == '7' and Section == 'Ruby':
        display(f'Register first before being able to participate', target='output')    

    elif Registration == 'No' and Medcert == 'No' and GrLevel == '7' and Section == 'Sapphire':
       display(f'Register first before being able to participate', target='output')     

    elif Registration == 'No' and Medcert == 'No' and GrLevel == '7' and Section == 'Topaz':
        display(f'Register first before being able to participate', target='output')     

    elif Registration == 'Yes' and Medcert == 'Yes' and GrLevel == '8' and Section == 'Emerald':
        display(f'You are a member of Blue Bears and are eligible to play.', target='output')     

    elif Registration == 'Yes' and Medcert == 'Yes' and GrLevel == '8' and Section == 'Ruby':
        display(f'You are a member of Red Bulldogs and are eligible to play.', target='output') 

    elif Registration == 'Yes' and Medcert == 'Yes' and GrLevel == '8' and Section == 'Sapphire':
        display(f'You are a member of Green Hornets and are eligible to play.', target='output') 

    elif Registration == 'Yes' and Medcert == 'Yes' and GrLevel == '8' and Section == 'Topaz':
        display(f'You are a member of Yellow Tigers and are eligible to play.', target='output') 

    elif Registration == 'Yes' and Medcert == 'No' and GrLevel == '8' and Section == 'Emerald':
        display(f'You are a member of Blue Bears, but please secure a medical certificate.', target='output')         
    elif Registration == 'Yes' and Medcert == 'No' and GrLevel == '8' and Section == 'Ruby':
        display(f'You are a member of Red Bulldogs, but please secure a medical certificate.', target='output')        

    elif Registration == 'Yes' and Medcert == 'No' and GrLevel == '8' and Section == 'Sapphire':
        display(f'You are a member of Green Hornets, but please secure a medical certificate.', target='output')            

    elif Registration == 'Yes' and Medcert == 'No' and GrLevel == '8' and Section == 'Topaz':
        display(f'You are a member of Yellow Tigers, but please secure a medical certificate.', target='output')            

    elif Registration == 'No' and Medcert == 'Yes' and GrLevel == '8' and Section == 'Emerald':
        display(f'You are a member of Blue Bears but please register online to be eligible for participation', target='output')   

    elif Registration == 'No' and Medcert == 'Yes' and GrLevel == '8' and Section == 'Ruby':
        display(f'You are a member of Red Bulldogs but please register online to be eligible for participation', target='output')       

    elif Registration == 'No' and Medcert == 'Yes' and GrLevel == '8' and Section == 'Sapphire':
        display(f'You are a member of Green Hornets but please register online to be eligible for participation', target='output')       

    elif Registration == 'No' and Medcert == 'Yes' and GrLevel == '8' and Section == 'Topaz':
        display(f'You are a member of Yellow Tigers but please register online to be eligible for participation', target='output')

    elif Registration == 'No' and Medcert == 'No' and GrLevel == '8' and Section == 'Emerald':
        display(f'Register first before being able to participate', target='output')   

    elif Registration == 'No' and Medcert == 'No' and GrLevel == '8' and Section == 'Ruby':
        display(f'Register first before being able to participate', target='output')    

    elif Registration == 'No' and Medcert == 'No' and GrLevel == '8' and Section == 'Sapphire':
       display(f'Register first before being able to participate', target='output')     

    elif Registration == 'No' and Medcert == 'No' and GrLevel == '8' and Section == 'Topaz':
        display(f'Register first before being able to participate', target='output')  

    elif Registration == 'Yes' and Medcert == 'Yes' and GrLevel == '9' and Section == 'Emerald':
        display(f'You are a member of Green Hornets and are eligible to play', target='output')    

    elif Registration == 'Yes' and Medcert == 'Yes' and GrLevel == '9' and Section == 'Ruby':
        display(f'You are a member of Red Bulldogs and are eligible to play', target='output')   

    elif Registration == 'Yes' and Medcert == 'Yes' and GrLevel == '9' and Section == 'Sapphire':
        display(f'You are a member of Yellow Tigers and are eligible to play', target='output')        

    elif Registration == 'Yes' and Medcert == 'Yes' and GrLevel == '9' and Section == 'Topaz':
        display(f'You are a member of Blue Bears and are eligible to play', target='output')        

    elif Registration == 'Yes' and Medcert == 'No' and GrLevel == '9' and Section == 'Emerald':
        display(f'You are a member of Green Hornets, but please secure a medical certificate.', target='output')         
    elif Registration == 'Yes' and Medcert == 'No' and GrLevel == '9' and Section == 'Ruby':
        display(f'You are a member of Red Bulldogs, but please secure a medical certificate.', target='output')        

    elif Registration == 'Yes' and Medcert == 'No' and GrLevel == '9' and Section == 'Sapphire':
        display(f'You are a member of Yellow Tigers, but please secure a medical certificate.', target='output')            

    elif Registration == 'Yes' and Medcert == 'No' and GrLevel == '9' and Section == 'Topaz':
        display(f'You are a member of Blue Bears, but please secure a medical certificate.', target='output')            

    elif Registration == 'No' and Medcert == 'Yes' and GrLevel == '9' and Section == 'Emerald':
        display(f'Register online to be eligible for participation', target='output')   

    elif Registration == 'No' and Medcert == 'Yes' and GrLevel == '9' and Section == 'Ruby':
        display(f'Register online to be eligible for participation', target='output')        

    elif Registration == 'No' and Medcert == 'Yes' and GrLevel == '9' and Section == 'Sapphire':
        display(f'Register online to be eligible for participation', target='output')       

    elif Registration == 'No' and Medcert == 'Yes' and GrLevel == '9' and Section == 'Topaz':
        display(f'Register online to be eligible for participation', target='output')

    elif Registration == 'No' and Medcert == 'No' and GrLevel == '9' and Section == 'Emerald':
        display(f'Register first before being able to participate', target='output')   

    elif Registration == 'No' and Medcert == 'No' and GrLevel == '9' and Section == 'Ruby':
        display(f'Register first before being able to participate', target='output')    

    elif Registration == 'No' and Medcert == 'No' and GrLevel == '9' and Section == 'Sapphire':
       display(f'Register first before being able to participate', target='output')     

    elif Registration == 'No' and Medcert == 'No' and GrLevel == '9' and Section == 'Topaz':
        display(f'Register first before being able to participate', target='output')  

    elif Registration == 'Yes' and Medcert == 'Yes' and GrLevel == '10' and Section == 'Emerald':
        display(f'You are a member of Yellow Tigers and are eligible to play', target='output')    

    elif Registration == 'Yes' and Medcert == 'Yes' and GrLevel == '10' and Section == 'Ruby':
        display(f'You are a member of Blue Bears and are eligible to play', target='output')   

    elif Registration == 'Yes' and Medcert == 'Yes' and GrLevel == '10' and Section == 'Sapphire':
        display(f'You are a member of Green Hornets and are eligible to play', target='output')        

    elif Registration == 'Yes' and Medcert == 'Yes' and GrLevel == '10' and Section == 'Topaz':
        display(f'You are a member of Red Bulldogs and are eligible to play', target='output')

    elif Registration == 'Yes' and Medcert == 'No' and GrLevel == '10' and Section == 'Emerald':
        display(f'Please secure a medical certificate.', target='output')    

    elif Registration == 'Yes' and Medcert == 'No' and GrLevel == '10' and Section == 'Ruby':
        display(f'Please secure a medical certificate.', target='output')           

    elif Registration == 'Yes' and Medcert == 'No' and GrLevel == '10' and Section == 'Sapphire':
        display(f'Please secure a medical certificate.', target='output')        

    elif Registration == 'Yes' and Medcert == 'No' and GrLevel == '10' and Section == 'Topaz':
        display(f'Please secure a medical certificate.', target='output')        

    elif Registration == 'No' and Medcert == 'Yes' and GrLevel == '10' and Section == 'Emerald':
        display(f'Register online to be eligible for participation', target='output')   

    elif Registration == 'No' and Medcert == 'Yes' and GrLevel == '10' and Section == 'Ruby':
        display(f'Register online to be eligible for participation', target='output')        

    elif Registration == 'No' and Medcert == 'Yes' and GrLevel == '10' and Section == 'Sapphire':
        display(f'Register online to be eligible for participation', target='output')       

    elif Registration == 'No' and Medcert == 'Yes' and GrLevel == '10' and Section == 'Topaz':
        display(f'Register online to be eligible for participation', target='output')

    elif Registration == 'No' and Medcert == 'No' and GrLevel == '10' and Section == 'Emerald':
        display(f'Register first before being able to participate', target='output')   

    elif Registration == 'No' and Medcert == 'No' and GrLevel == '10' and Section == 'Ruby':
        display(f'Register first before being able to participate', target='output')    

    elif Registration == 'No' and Medcert == 'No' and GrLevel == '10' and Section == 'Sapphire':
       display(f'Register first before being able to participate', target='output')     

    elif Registration == 'No' and Medcert == 'No' and GrLevel == '10' and Section == 'Topaz':
        display(f'Register first before being able to participate', target='output')     

    else: 
        display(f'Invalid Input', target='output')