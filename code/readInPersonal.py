# this class will read in an the personal file and store the data for easy access

class PersonalData(): 
    def __init__(self,filename = 'personal') -> None:
        self.personalData = {
            'X' : None,
            'Y' : None,
            'email' : None,
            'password' : None
        }
        self.filename = filename    
        # read in the data give an error if it doesnt work
        if not(self.readfile()):
            print('Personal file error')
    
    def __str__(self) -> str:
        str = ''
        for key in self.personalData:
            str += key
            str += ': '
            str += self.personalData[key]
            str += '\n'
        return str.strip()


    def readfile(self):
        # this method updates self.personalData from the file
        try:
            with open(self.filename, 'r') as file:
                line = file.readline()
                while line:
                    # places the data from the file into the class for easy access
                    self.personalData[line.split(':')[0].strip()] = \
                    line.split(':')[1].strip()
                    line = file.readline()
                return 1
        except:
            return 0
        
    def get(self, value = None):
        if (value == None):
            print('error invalid value')
        else:
            return self.personalData[value]
        
if __name__ == "__main__":
    test = PersonalData()
    print(test.get('X'))
    print(test.get('Y'))
    print(test.get('email'))
    print(test.get('password'))
    print(test)