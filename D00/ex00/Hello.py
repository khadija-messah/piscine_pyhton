ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"


ft_set.remove("tutu!")
ft_set.add("Hello")
ft_set.add("casablanca!")

tmp = list(ft_tuple)
tmp[1] = "Morocco!"
ft_tuple = tmp

ft_dict["Hello"] = "1337-benguerir!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)