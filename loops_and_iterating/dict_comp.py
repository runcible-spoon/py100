from pprint import pp

squares = {f'{number}-squared': number * number
           for number in range(1, 6) }
# pp(squares)

# set comprehension

squares = { number * number for number in range(1, 6) }
print(squares)
