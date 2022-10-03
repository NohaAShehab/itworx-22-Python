print("----- welcome to the validation package --------")

def niceToMeetYou(name):
    print(f"Nice to you meet you ,,, {name}.")

# register your import here

from validatationpkg.greetingModule import  sayHello, sayWelcome


"""

    1- import the module 
        -----> simple module    
                import module_name 
                
                ---> how to use 
                    module_name.blockname 
        
        ---> module in the package 
            import packagename.module_name 
             ---> how to use 
                    packagename.module_name.blockname    
    --------------------------------------------------------------------
    "2- import part of the module " 
     ---> simple module 
            from module_name import blockname 
     
     ---> module in a package
            from package_name.module_name import blockname
            
            
    ----------------------------------------- package with __init__ module ---------------------------------------------
    in file __init__.py  ----> add the lines of code you want to use when you just import the package 




"""