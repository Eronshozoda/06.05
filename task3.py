## Har du shart kor mekunand


str_list=["Emma","Jon","", "Kelly",None,"Erik",""]
for i in str_list:
    if i==None or i=="":
        str_list.remove(i)
print(str_list)        

# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# res_list = []
# for i in str_list:
#     if i:
#         res_list.append(i)
# print(res_list)