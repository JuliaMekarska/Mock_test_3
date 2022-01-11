class C():
    
    def __init__(self, sentence):
        
        self.sen = sentence
        
    def m(self):
        
        counter = 0
        
        for i in self.sen:
            
            for j in self.sen:
                
                if i == j:
                    
                    counter += 1
                    
            if counter > 1:
                        
                return False
                    
            else:
                        
                return True
                    
                
c = C("red sun")                
c.m()
