class Car():
    
    def __init__(self,model,color,year,brand,engine):
        self.color=color
        self.model=model
        self.year=year
        self.brand=brand
        self.engine=engine

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelerated")

Audi=Car("A6","blue",2018,"Audi","V6")

print(Audi.stop())
print(Audi.model)
print(Audi.year)
