# # a = 1
# # b = 2
# # print(a+b)

# # BANANA

# def minion_game(string):
#     vowel = 0
#     cons = 0
#     s = len(string)
#     for i in range(s):
#         if string[i] in 'AEIOU':
#             vowel = vowel+(s-i)
#             # print(vowel)
#         else:
#             cons = cons+(s-i)

#     if cons>vowel:
#         print("Stuart {}".format(cons))
    
#     elif cons == vowel:
#         print("Draw")
    
#     else:
#         print("Kevin {}".format(vowel))
    

# minion_game(string="BANANA")
            



# k = 3
# string= "AABCAAADA"
# s = ""
# c = 0
# for ele in string:
#     if ele not in s:
#         s = s+ele
#     c+=1
#     if(c==k):
#         print(s)
#         c =0
#         s=""
# for i in range(0,len(k2)):
#     print(k2[i],end="")
# print(k2)


# # j = ["AAB","CAA","ADA"]
# k = "AABCAAADA"
# print(k.split())

# m = "ADA"
# l = "AABCAAADA"
# # k = "AABCAAADA"
# k = []
# for ele in l:
#     if ele not in k:
#         k.append(ele)

# print(k)
# # for i in range(0,len(m)):
# #     print(m[i])

# j = ["AAB,CAA,ADA"]
# m = []

# for i in range(0,len(j)):
#     for ele in j[i]:
#         if ele not in m:
#             m.append(ele)
# print(m)
