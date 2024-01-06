necessityEnvelop = 0  # NEC, необхідні витрати
freedomEnvelop = 0  # FFA, фінансова свобода
educationEnvelop = 0  # EDU, освіта
longTermEnvelop = 0  # LTSS, резерв та на великі покупки
playEnvelop = 0  # PLAY, розваги
giveEnvelop = 0  # GIVE, подарунки

# initializing percent rate
necRate = 0.55
ffaRate = 0.1
eduRate = 0.1
ltssRate = 0.1
playRate = 0.1
giveRate = 0.05
# initializing expected income, expected necessity and other amounts
expectedIncome = 1000
# invitation, greetings etc.
print("""Hello.\n
We gonna fill your envelops by the money you input here!\n
Please input your amounts of money income and see the results.\n
Press Ctrl+c to exit script.
\n\n Enter the amount please:""")
# initializing handler for standard input
sum = 0
while (sum < expectedIncome):
  line = int(input())
  sum += line

  necessityEnvelop += line * necRate
  freedomEnvelop += line * ffaRate
  educationEnvelop += line * eduRate
  longTermEnvelop += line * ltssRate
  playEnvelop += line * playRate
  giveEnvelop += line * giveRate

  print("\n Enter the amount please:")
line = int(input())

# final output
necessityEnvelop1 = str(int(necessityEnvelop))
freedomEnvelop1 = str(int(freedomEnvelop))
educationEnvelop1 = str(int(educationEnvelop))
longTermEnvelop1 = str(int(longTermEnvelop))
playEnvelop1 = str(int(playEnvelop))
giveEnvelop1 = str(int(giveEnvelop))

print("At the end we have:\n")

message = (f"Necessity Envelop has {necessityEnvelop1}\n"
           f"Financial Freedom Envelop has: {freedomEnvelop1}\n"
           f"Education Envelop {educationEnvelop1}\n"
           f"Long Term Saving for Spending Envelop has: {longTermEnvelop1}\n"
           f"Play Envelop has: {playEnvelop1}\n"
           f"Give Envelop has: {giveEnvelop1}\n")
print(message)
print("\n\
           _______________________________________________________________\n\
       \
           Thanks for using our software :)")
