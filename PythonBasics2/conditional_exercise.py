is_magician = True
is_expert = False

# check if magician AND expert: "you are a master magician"
# check if magician but not expert: "at least you're getting there"
# check if you're not magician: "You need magic powers"

if is_magician and is_expert:
    print("You are a master magician")
elif is_magician and not (is_expert):
    print("At least you're getting there.")
elif not (is_magician):
    print("You need magic powers.")
