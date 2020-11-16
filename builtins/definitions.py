from shared.userdata import user
def CreateApp(appstartupmessage):
    Application = True
    if Application == 'True':
        print(appstartupmessage)
    
def Log():
    user.UserLog  

class Application():
    def user(self, boolean): # Capture User Data
        if boolean == True:
            CreateApp()
            
            
            
            
