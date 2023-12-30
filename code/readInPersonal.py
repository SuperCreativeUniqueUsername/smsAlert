class PersonalData(): 
    def __init__(self, filename='personal') -> None:
        self.personalData = {
            'X': None,
            'Y': None,
            'email': None,
            'password': None,
            'phone': None
        }
        self.filename = filename    
        # read in the data; give an error if it doesn't work
        try:
            self.read_file()
        except FileNotFoundError:
            raise Exception(f'Personal file not found: {self.filename}')

    def __str__(self) -> str:
        result = ''
        for key in self.personalData:
            result += f'{key}: {self.personalData[key]}\n'
        return result.strip()

    def read_file(self):
        # this method updates self.personalData from the file
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    key, value = map(str.strip, line.split(':', 1))
                    self.personalData[key] = value
        except FileNotFoundError:
            raise Exception(f'Personal file not found: {self.filename}')

    def get(self, value='X'):
        return self.personalData.get(value, f'Error: {value} is not a valid key')


if __name__ == "__main__":
    test = PersonalData()
    print(test)
