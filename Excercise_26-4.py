# ฝึกการใช้ List comprehension โดยการแยกคำแต่ละคำออกมาแล้วนับจำนวตัวอักษรของคำ

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}

print(result)

