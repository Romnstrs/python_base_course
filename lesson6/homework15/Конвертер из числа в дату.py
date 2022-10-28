secs=input("Введите число больше 0 и меньше 8639999: ")
secs=int(secs)
days=secs//86400
secs=secs%86400
hours=secs//3600
secs=secs%3600
minutes=secs//60
secs=secs%60
days_endings=days%10
endings={0:"дней",1:"день",2:"дня",3:"дня",4:"дня",5:"дней",6:"дней",7:"дней",8:"дней",9:"дней"}
hours= str(hours).zfill(2)
minutes= str(minutes).zfill(2)
secs= str(secs).zfill(2)
answer=str(days)+" "+endings[days_endings]+", "+hours+":"+minutes+":"+secs
print(answer)