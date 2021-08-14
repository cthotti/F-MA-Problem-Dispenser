import discord
import random
import time
#You have make the discord bot running
from main_keep_running import keep_alive 

client=discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))


#all of the global values
count=2
b=""
a=0
ans=""
start=0
year=0
year_min=2007
#year comment
year_max=2009

test=False
ez_count=9
med_count=8
mhard_count=8
test_count=1
b_check=False
actual_answer=[]
answer_input=[]
start=0
quit=False
score=0
easy=False
med=False
hard=False
problem=False

#You have to make a file where you can put all the pictures. 
#Take a screenshot of every problem, if the problem has two parts to it, then take a screenshot of the first part, then the second part wiht the first part. 
#Easy problems are 1-9 inclusive. Medium problems are 10-17 inclusive. Hard problems are 18-25 inclusive. 
#For easy problems type, fma(year)_ez_(number of problem), as header and it has to be a jpg 
#Make an fma_ez.env folder where you can type the answers from problems 1-9
#For medium problems type, fma(year)_med_(number of problem-9), as header and it has to be jpg
#Make an fma_med.env folder where you can type the answers from problems 10-17
#For hard problems type, fma(year)_mhard_(number of problem-17), as header and it has to be jpg
#Make an fma_mhard.env folder where you can type the answers from problems 18-25
#Go the year comment above and update the year_max

@client.event
async def on_message(message):
  global b,a,count,ans,start,year,points,test,ez_count,med_count,mhard_count,test_count,b_check,actual_answer,answer_input,quit,score,easy,med,hard,problem
  b=message.content

  if message.author == client.user:
    return

  if b=="$quit":
    quit=True
  
  if test==False:
    if message.content.startswith('$fma ez' or '$fma easy'):
      year=random.randint(year_min,year_max)
      ans_file=open("fma_ez.env","r")
      ans=ans_file.readlines()
      number_lines=0
      for i in range(0,len(ans)):
        number_lines+=1
      a=random.randint(1,number_lines)
      c=a%9
      if c==0:
        c=9
      count=2
      a=year%year_min*9+c
      await message.channel.send("Answer problem "+str(c)+" in the year "+str(year)+":")
      await message.channel.send(file=discord.File("fma"+str(year)+"_ez_"+str(c)+'.jpg'))
      start=time.time()
      ans_file.close()
      easy=True
      problem=True
      quit=False
  
  if test==False:
    if message.content.startswith('$fma med' or '$fma medium'):
      year=random.randint(year_min,year_max)
      ans_file=open("fma_med.env","r")
      ans=ans_file.readlines()
      number_lines=0
      for i in range(0,len(ans)):
        number_lines+=1
      a=random.randint(1,number_lines)
      c=a%8
      if c==0:
        c=8
      count=2
      a=year%year_min*8+c
      await message.channel.send("Answer problem "+str(c+9)+" in the year "+str(year)+":")
      await message.channel.send(file=discord.File("fma"+str(year)+"_med_"+str(c)+'.jpg'))
      start=time.time()
      ans_file.close()
      med=True
      quit=False
      problem=True
  
  if test==False:
    if message.content.startswith('$fma hard'):
      year=random.randint(year_min,year_max)
      ans_file=open("fma_mhard.env","r")
      ans=ans_file.readlines()
      number_lines=0
      for i in range(0,len(ans)):
        number_lines+=1
      a=random.randint(1,number_lines)
      c=a%8
      if c==0:
        c=8
      count=2
      a=year%year_min*8+c
      await message.channel.send("Answer problem "+str(c+17)+" in the year "+str(year)+":")
      await message.channel.send(file=discord.File("fma"+str(year)+"_mhard_"+str(c)+'.jpg'))
      start=time.time()
      ans_file.close()
      hard=True
      quit=False
      problem=True

  if test==False:
    if message.content.startswith('$stats'):
      await message.channel.send(str(message.author)+" has a score of "+str(score))
  
  if test==False:
    if message.content.startswith('$test'):
      await message.channel.send("You have 25 questions to solve in 75 min. 9 easy questions, 8 medium questions, and 8 hard questions. This is not from pervious tests but are randomly generated. No cheating allow. Calculators are permitted.")
      quit=False  
      year=random.randint(year_min,year_max)
      ans_file=open("fma_ez.env","r")
      ans=ans_file.readlines()
      number_lines=0
      for i in range(0,len(ans)):
        number_lines+=1
      a=year%year_min*9+test_count
      actual_answer.append("$ans "+ans[a-1][0])
      await message.channel.send(str(test_count)+".")
      await message.channel.send("Answer problem "+str(test_count)+":")
      b_check=False
      await message.channel.send(file=discord.File("fma"+str(year)+"_ez_"+str(test_count)+'.jpg'))
      ans_file.close()
      test=True
      test_count+=1
      start=time.time()
    
  if test==True:
    if quit==False:
      end=time.time()
      if b=="$time":
        time_actual=round(end-start)
        taken_time=(4500-time_actual)
        min=0
        if taken_time>60:
          while taken_time>60:
            taken_time-=60
            min+=1
          await message.channel.send("You have "+str(min)+"min and "+str(taken_time)+" left.")
        else:
          await message.channel.send("You have "+str(taken_time)+" left.")
      output=""
      if len(b)==6:
        for i in range(0,5):
          output+=b[i]
        if output=="$ans ":
          b_check=True
          answer_input.append(b)
          
          if test_count<=9 and b_check==True:
            year=random.randint(year_min,year_max)
            ans_file=open("fma_ez.env","r")
            ans=ans_file.readlines()
            number_lines=0
            for i in range(0,len(ans)):
              number_lines+=1
            c=test_count%9
            if c==0:
              c=9
            a=year%year_min*9+c
            actual_answer.append("$ans "+ans[a-1][0])
            await message.channel.send(str(test_count)+".")
            await message.channel.send("Answer problem "+str(test_count)+":")
            b_check=False
            await message.channel.send(file=discord.File("fma"+str(year)+"_ez_"+str(test_count)+'.jpg'))
            ans_file.close()
            test_count+=1
            
          if test_count>9 and test_count<=17 and b_check==True:
            year=random.randint(year_min,year_max)
            ans_file=open("fma_med.env","r")
            ans=ans_file.readlines()
            number_lines=0
            for i in range(0,len(ans)):
              number_lines+=1
            c=test_count-9
            c=test_count%8
            if c==0:
              c=8
            a=year%year_min*8+c
            actual_answer.append("$ans "+ans[a-1][0])
            await message.channel.send(str(test_count)+".")
            await message.channel.send("Answer problem "+str(test_count)+":")
            b_check=False
            await message.channel.send(file=discord.File("fma"+str(year)+"_med_"+str(c)+'.jpg'))
            ans_file.close()
            test_count+=1
          
          if test_count>17 and test_count<=25 and b_check==True:
            year=random.randint(year_min,year_max)
            ans_file=open("fma_mhard.env","r")
            ans=ans_file.readlines()
            number_lines=0
            for i in range(0,len(ans)):
              number_lines+=1
            c=test_count-17
            c=test_count%8
            if c==0:
              c=8
            a=year%year_min*8+c
            actual_answer.append("$ans "+ans[a-1][0])
            await message.channel.send(str(test_count)+".")
            await message.channel.send("Answer problem "+str(test_count)+":")
            b_check=False
            await message.channel.send(file=discord.File("fma"+str(year)+"_mhard_"+str(c)+'.jpg'))
            ans_file.close()
            test_count+=1
          
          if test_count==26 and b_check==True:
            correct=0
            incorrect=""
            for i in range(0,len(answer_input)):
              if answer_input[i]==actual_answer[i]:
                correct+=1
                if i+1<=9:
                  score+=1
                if i+1>9 and i+1<=17:
                  score+=2
                if i+1>17 and i+1<=25:
                  score+=3
              else:
                incorrect+=str(i+1)+"; "+str(actual_answer[i])+", "
            await message.channel.send("You got "+str(correct)+"/25")
            await message.channel.send("You got these questions wrong: "+incorrect+"   ")
            test=False
            test_count=0
            return

          if round(end-start)>4500:
            correct=0
            incorrect=""
            for i in range(0,len(answer_input)):
              if answer_input[i]==actual_answer[i]:
                correct+=1
              else:
                incorrect+=str(i+1)+"; "+str(actual_answer[i])+", "
            await message.channel.send("You ran out of time.")
            await message.channel.send("You got "+str(correct)+"/25")
            await message.channel.send("You got these questions wrong: "+incorrect)
            test=False
            test_count=0
            return
    else:
      correct=0
      incorrect=""
      for i in range(0,len(answer_input)):
        if answer_input[i]==actual_answer[i]:
          correct+=1
        else:
          incorrect+=str(i+1)+"; "+str(actual_answer[i])+", "
      await message.channel.send("You got "+str(correct)+"/25")
      await message.channel.send("You got these questions wrong: "+incorrect+"   ")
      test=False
      test_count=0
      quit=False
      return
    
  
  
  if test==False:
    if message.content.startswith('$help'):
      fma_help=open("fma_help.env","r")
      await message.channel.send(fma_help.read())
      fma_help.close()

  if test==False:
    if problem==True:
      if quit==False:
        output=""
        if len(b)==6:
          for i in range(0,4):
            output+=b[i]
          if output=="$ans":
            if count>=1:
              if b=="$ans "+str(ans[a-1][0]):
                await message.channel.send("Correct!")
                if easy==True:
                  score+=1
                if med==True:
                  score+=2
                if hard==True:
                  score+=3
                end=time.time()
                taken_time=round(end-start)
                min=0
                easy=False
                med=False
                hard=False
                problem=False
                if taken_time>60:
                  while taken_time>60:
                    taken_time-=60
                    min+=1
                  await message.channel.send("It took you: "+str(min)+" min "+str(taken_time)+" sec")
                  return
                else:
                  await message.channel.send("It took you: "+str(taken_time)+" sec")
                  return

              else:
                if count>1:
                  await message.channel.send("Incorrect! You have "+str(count-1)+" try left!")
                  count-=1
                  return
                else:
                  easy=False
                  med=False
                  hard=False
                  await message.channel.send("Wrong answer, the correct answer is "+str(ans[a-1][0]))
                  end=time.time()
                  taken_time=round(end-start)
                  min=0
                  problem=False
                  if taken_time>60:
                    while taken_time>60:
                      taken_time-=60
                      min+=1
                    await message.channel.send("It took you: "+str(min)+" min "+str(taken_time)+" sec")
                    return
                  else:
                    await message.channel.send("It took you: "+str(taken_time)+" sec")
                    return
      else:
        await message.channel.send("Wrong answer, the correct answer is "+str(ans[a-1][0]))
        problem=False
        end=time.time()
        taken_time=round(end-start)
        min=0
        if taken_time>60:
          while taken_time>60:
            taken_time-=60
            min+=1
          await message.channel.send("It took you: "+str(min)+" min "+str(taken_time)+" sec")
          quit=False
          return
        else:
          await message.channel.send("It took you: "+str(taken_time)+" sec")
          quit=False
          return


keep_alive()
client.run('Token')
