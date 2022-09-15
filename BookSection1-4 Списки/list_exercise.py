# (3-2) + (3-3) + (3-4) + (3-5) + (3-6) + (3-7) +

guests = ['Veronika', 'Mykita', 'Maria', 'Vlad', 'Sasha']

print(f'Hello {guests[0]}, its your personal invitation to the festival of naked pussies!')
print(f'Hello {guests[1]}, its your personal invitation to the festival of naked pussies!')
print(f'Hello {guests[2]}, its your personal invitation to the festival of naked pussies!')
print(f'Hello {guests[3]}, its your personal invitation to the festival of naked pussies!')
print(f'Hello {guests[4]}, its your personal invitation to the festival of naked pussies!')
print(f'\nSorry, but {guests[1]} disliked the idea and refused to go to the festival')

guest_popped = guests.pop(1)
guests.insert(1, 'Vlad Statkevich')
print(f'\nHello {guests[0]}, its your personal invitation to the festival of naked pussies, {guest_popped} dekline our '
      f'invation so we invate {guests[1]} to our festival !')
print(f'Hello {guests[1]}, its your personal invitation to the festival of naked pussies {guest_popped} dekline our '
      f'invation so we invate {guests[1]} to our festival !')
print(f'Hello {guests[2]}, its your personal invitation to the festival of naked pussies {guest_popped} dekline our '
      f'invation so we invate {guests[1]} to our festival !')
print(f'Hello {guests[3]}, its your personal invitation to the festival of naked pussies {guest_popped} dekline our '
      f'invation so we invate {guests[1]} to our festival !')
print(f'Hello {guests[4]}, its your personal invitation to the festival of naked pussies! {guest_popped} dekline our '
      f'invation so we invate {guests[1]} to our festival !')

guests.insert(0, 'Lera')
guests.insert(2, 'Lena')
guests.append('Max')
# print(guests)
print(f'\nWe have new room, so in future i add new person to our festival!')

print(f'\nHello {guests[0]}, its your personal invitation to the festival of naked pussies!')
print(f'Hello {guests[1]}, its again your personal invitation to the festival of naked pussies, we just add some '
      f'new person!')
print(f'Hello {guests[2]}, its your personal invitation to the festival of naked pussies!')
print(f'Hello {guests[3]}, ts again your personal invitation to the festival of naked pussies, we just add some '
      f'new person!')
print(f'Hello {guests[4]}, ts again your personal invitation to the festival of naked pussies, we just add some '
      f'new person!')
print(f'Hello {guests[5]}, ts again your personal invitation to the festival of naked pussies, we just add some '
      f'new person!')
print(f'Hello {guests[6]}, its your personal invitation to the festival of naked pussies!')
print(f'Hello {guests[7]}, ts again your personal invitation to the festival of naked pussies, we just add some '
      f'new person!')

print(f'\nIm so sorry, but our new room is fired, so in room that i have can only be 3 person include me, soon '
      f'i send message to person who can stay home and cry =(')
# print(guests)

# print(f'Sorry {}, but u stay cry home')

guest_pop_one = guests.pop(7)
print(f'Sorry {guest_pop_one}, but u stay cry home')

guest_pop_two = guests.pop(6)
print(f'Sorry {guest_pop_two}, but u stay cry home')

guest_pop_three = guests.pop(4)
print(f'Sorry {guest_pop_three}, but u stay cry home')

guest_pop_four = guests.pop(3)
print(f'Sorry {guest_pop_four}, but u stay cry home')

guest_pop_five = guests.pop(2)
print(f'Sorry {guest_pop_five}, but u stay cry home')

guest_pop_six = guests.pop(0)
print(f'Sorry {guest_pop_six}, but u stay cry home')

print(f'\nHey {guests[0]} and {guests[1]} we can have fun togather, you still have invitation to the festival '
      f'of naked pussies!')

del guests[0]
del guests[0]

print(guests)
