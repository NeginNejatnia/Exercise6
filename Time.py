import time

class Time:

    def __init__(self,time1,time2):
        self.time1 = time1
        self.time2 = time2


    def convert_to_seconds(self):
        """converts Time object to an integer(# of seconds)"""
        self.hours1 = (int(temp1[0]))*3600
        self.minutes1 = (int(temp1[1]))*60
        self.second1 = int(temp1[2])
        self.sum1 = self.hours1+self.minutes1+self.second1
        self.hours2 = (int(temp2[0]))*3600
        self.minutes2 = (int(temp2[1]))*60
        self.second2 = int(temp2[2])
        self.sum2 = self.hours2+self.minutes2+self.second2
        return (self.sum1,self.sum2)

    def make_time(self):
        """converts from an integer to a Time object""" 
    
        result1 = time.strftime("%H:%M:%S",time.gmtime (self.sum1))
        result2 = time.strftime("%H:%M:%S",time.gmtime (self.sum2))

        print('Hour1: ',result1)
        print('Hour2: ',result2)

    def __add__(self):
        self.hours1 = int(temp1[0])
        self.minutes1 = int(temp1[1])
        self.second1 = int(temp1[2])
        self.hours2 = int(temp2[0])
        self.minutes2 = int(temp2[1])
        self.second2 = int(temp2[2])

        add_hours = self.hours1 + self.hours2
        add_minutes = self.minutes1 + self.minutes2
        add_second = self.second1 + self.second2

        if add_second >60:
            add_second -= 60
            add_minutes += 1
            if add_minutes > 60 :
                add_minutes -= 60
                add_hours += 1
          

        print('Result add is : ',"%02d:%02d:%02d" % (add_hours,add_minutes,add_second))


    def reduce_time(self):
        self.hours1 = int(temp1[0])
        self.minutes1 = int(temp1[1])
        self.second1 = int(temp1[2])
        self.hours2 = int(temp2[0])
        self.minutes2 = int(temp2[1])
        self.second2 = int(temp2[2])

        add_hours = self.hours1 - self.hours2
        add_minutes = self.minutes1 - self.minutes2
        add_second = self.second1 - self.second2

        if add_second<0:
            add_second = self.second2 - self.second1
            if add_minutes <0:
                add_minutes = self.minutes2 - self.minutes1
                if add_hours <0:
                    add_hours = self.hours2 - self.hours1
            

        print('Result Reduce is : ',"%02d:%02d:%02d" % (add_hours,add_minutes,add_second))
        
  
time1 = input("Enter hour1: ")
time2 = input("Enter hour2: ")
temp1 = time1.split(':')
temp2 = time2.split(':')


my_time = Time (time1,time2) 

print('Result of converting is : ',my_time.convert_to_seconds())
my_time.make_time()
my_time.__add__()
my_time.reduce_time()
