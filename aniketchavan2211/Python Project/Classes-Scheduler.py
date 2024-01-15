#!/bin/python

def schedule_classes(classes, times):
  schedule = []
  
  index = 0
  while index < len(classes):
    schedule_class = classes[index] + ":" + times[index]
    schedule.append(schedule_class)
    index += 1
  return schedule

classes = ["Algebra", "History", "Biology", "Swimming"]

times = ["9a.m.", "11a.m.", "1p.m.", "3p.m."]

schedule = schedule_classes(classes, times)

print (f"Monday's schedule: {schedule}")
