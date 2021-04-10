def add_time(start, duration, day = None):

  start,end = start.split()

  if(end == "PM"):
      end = 1
  else:
      end = 0

  startH, startM = start.split(":")
  duraH, duraM = duration.split(":")

  newM = int(startM) + int(duraM)

  addH,newM = divmod(newM, 60)

  if(newM < 10):
      newM = "0"+str(newM)
  else:
      newM = str(newM)

  newH = int(startH) + int(duraH) + addH

  addD,newH = divmod(newH, 12)

  if(newH == 0): newH = 12

  newD,newEnd = divmod(addD + end, 2)

  if(newEnd == 1):
      newEnd = " PM"
  else:
      newEnd = " AM"
  if(newD == 0): after = ""
  elif(newD == 1):
      after = " (next day)"
  else:
      after = " (" + str(newD) + " days later)"
      
  if(day != None):
      days = {'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday': 3, 'Friday': 4,'Saturday':5,'Sunday':6}
      day = day.title()
      
      for k,v in days.items():
          if(day == k):
              day = v
              break
      newDay = newD + day
      newDay = divmod(newDay,7)[1]
      
      for k,v in days.items():
          if(newDay == v):
              newDay = k
              break

      return str(newH) + ":" + str(newM) + str(newEnd) + ", " + newDay + after
  else:
    return str(newH) + ":" + str(newM) + str(newEnd) + after