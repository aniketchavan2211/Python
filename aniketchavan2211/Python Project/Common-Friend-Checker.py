#!/bin/python 

def is_common_friend(user, friend_a, friend_b):
  
  is_friend_a = friend_a.count(user) >= 1
  is_friend_b = friend_b.count(user) >= 1

  is_common = is_friend_a & is_friend_b

  return is_common

friends_jeo = ["Sam", "Alex", "Zeo"]
friends_may = ["Kim", "Alex", "Cy", "Ted"]
common_alex = is_common_friend("Alex", friends_jeo, friends_may)
print (f"Alex is a common friend: {common_alex}")
