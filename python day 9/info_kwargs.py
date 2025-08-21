def student_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
student_info(name = "devashish",age = 20,course = "bca")