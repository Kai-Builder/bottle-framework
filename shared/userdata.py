from datetime import datetime # DateTime Module


d = datetime.now()


class user(): # Making User class
    def UserLog(self): # UserLogging Function
        file = open(d,'LOG.log', "w") # Logging Time whenever Log Function is called
        file.write(f'@ {d}, User has been logged.') # Customization Coming soon
        file.close()
    def GetInputData(self, args, con, out): # Get Input for Console Side-Applications.
        a = input(args) # Give user a prompt.
        if a == con:
            print(out) # 
            
    def IsAddition(self, TF):
        if TF == True:
            Addon = open('addon.json', "w")
            Addon.write('{\n\n\n\n\n\t"addon_Name": "HelloWorld",\n\t"AddonVersion": "YourString"\n\n\n\n\n\n\n\n\n\n\n\n\n}')
            
           

