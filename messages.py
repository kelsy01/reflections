import random
if __name__ == '__main__':
  messages = ['Keep it up!','You\'re doing great!','I love you!','You\'re so smart!','You\'re so pretty!']
  reply = "Y"

  while reply.upper() == "Y":
      print (random.choice(messages))
      reply = input("Get another compliment? (enter Y for yes) \n >")


