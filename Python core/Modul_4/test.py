# def is_valid_password(password):
#     print(password)
#     if len(password) == 0:
#         return False
#     if len(password) < 8:
#         return False
#     if any(ch.isdigit() for ch in password):
#         if any(ch.isupper() for ch in password):
#             if any(ch.lower() for ch in password):
#                     print("Password is fine")
#                     return True
#     else:
#          return False
    

# def is_valid_password(password):
#     letters_big = False     # 1
#     letters_small = False   # 1
#     numbers = False  
#     current = 0       # 1
    
#     if len(password) != 8:
#         return False
           
#     for pass_el in password:
        
#         if letters_big and letters_small and numbers:
#             return True
        
#         if pass_el.istitle()):
#             letters_big = True
                               
#         if pass_el.islower():
#             letters_small = True
          
#         if pass_el.isdigit():
#             numbers = True
#         current += 1

#         if current == 8:
#             return False

    

# print(is_valid_password('00345600'))


def is_valid_password(password):
    if len(password) != 8:
        return False
    if any(ch.isdigit() for ch in password) and any(ch.isupper() for ch in password) and any(ch.islower() for ch in password):
        return True
    else:
        return False
    
print(is_valid_password('S|1QY(Cb'))