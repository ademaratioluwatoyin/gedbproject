class Info : 
    def __init__(self, type, tag, title, description):
        self.type = type
        self.tag = tag
        self.title = title
        self.description = description 


class Company : 

    infos = []
    overview = ""
    def __init__(self, name, sub_industry, overview):
        self.name = name
        self.sub_industry = sub_industry
        self.overview = overview
        
    def __str__(self):
        return self.name

    
    
    