from ConfigParser import ConfigParser

class FCConfig(object):
    """ Parses a .ini configuration file
    This parser disregards sections, meaning option names are unique
    >>> fcc = FCConfig("config.ini")
    >>> fcc["docsFile"]
    "specific_doc_file.txt"
    """
    
    def __init__(self, configFName):
        self.confPar = ConfigParser()
        self.confPar.read(configFName)
        self.confDict = {}
        self.options = set()
        self.readConfig()

    def readConfig(self):
        """ Hard coded reading of options to ensure correct data type"""
        # for section in self.configParser.sections():
        #   for option in self.configParser.options(section):
        #       self.configDict[option] = self.configParser.get(section, option)
        self.readConfigHelper("Files", "seedFile")
        self.readConfigHelper("Files", "docsFile")
        self.readConfigHelper("Files", "labelFile")

        self.readConfigHelper("VSM Filtering", "VSMFilterModel")
        self.readConfigHelper("VSM Filtering", "minRepositoryDocNum", "int")
        self.readConfigHelper("VSM Filtering", "filterRelevantThreshold", "float")
        self.readConfigHelper("VSM Filtering", "filterIrrelevantThreshold", "float")
        self.readConfigHelper("VSM Filtering", "numFilterTopics", "int")

        self.readConfigHelper("Classifier", "classifier")
        self.readConfigHelper("Classifier", "trainDocNum", "int")
        self.readConfigHelper("Classifier", "allowAdaptive", "boolean")
        
        self.readConfigHelper("Crawling", "threshold", "float")
        

    def readConfigHelper(self, sect, opt, dataType="string"):
        """ Helper function to read in an option, based on dataType """
        if dataType.lower() == "string":
            self.confDict[opt] = self.confPar.get(sect, opt)
        elif dataType.lower() == "boolean":
            self.confDict[opt] = self.confPar.getboolean(sect, opt)
        elif dataType.lower() == "float":
            self.confDict[opt] = self.confPar.getfloat(sect, opt)
        elif dataType.lower() == "int":
            self.confDict[opt] = self.confPar.getint(sect, opt)
        self.options.add(opt)
                

    def __getitem__(self, key):
        return self.confDict[key]

    def getOptions(self):
        return self.options
    

if __name__ == "__main__":
    fc = FCConfig("config.ini")
    print fc.confDict
    print fc.getOptions()
