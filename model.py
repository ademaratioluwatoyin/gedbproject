class Info : 
    def __init__(self, type, tag, title, description):
        self.type = type
        self.tag = tag
        self.title = title
        self.description = description 


class Company : 

    infos = []
    overview = ""
    def __init__(self, name, sub_industry):
        self.name = name
        self.sub_industry = sub_industry
        
    def __str__(self):
        return self.name

    def addInfo(self, info) : 
        for inf in info : 
            self.infos.append((inf))
    
    