# 8-6

def city_country(city, country):
    """Повертає відформатоване місто та країну."""
    capital_of_country = f"{city}, {country}"
    return capital_of_country.title()


capital = city_country('Kyiv', 'Ukraine')
print(capital)

# 8-6 (Роблю ще бо не викупив)
# (Функція про пк, де проц і відеокарта. Вивід це сетап...)

def pc_setup(gpu, cpu):
    """"Повертає цілий сетап для пк"""
    setup = f"This pc include {gpu} and {cpu}"
    return setup


pc = pc_setup('rtx 2070', 'ryzen 5 5600')
print(pc)

# 8-7

def make_album(name, album, track=None):
    """Повертає словник для опису муз. альбому"""
    album_info = {
        "artist_name": name,
        "album_name": album
    }
    if track:
        album_info["track"] = track
    return album_info


album1 = make_album('xxx', 'depression')
album2 = make_album('lil nas x', 'montero')
album3 = make_album('50 cent', 'candy', track=1)

print(album1)
print(album2)
print(album3)

# 8-8

def make_album(name, album, track=None):
    """Повертає текст для опису муз. альбому"""
    album_info = f'{name} {album} {track}'
    return album_info


while True:
    print("\nPlease tell your favorite album and name of person who made it")
    print('enter "q" at any time to quit.')
    n_name = input("Enter artist name: ")
    if n_name == 'q':
        break
    a_name = input("Enter album name: ")
    if a_name == 'q':
        break
    t_count = input("Enter count of tracks:  ")
    if t_count == 'q':
        break

    all_info_togather = make_album(n_name, a_name, t_count)
    print(f"\nThat is info  {all_info_togather}")


# 8-8
# Опять делаем свое на примере пк

def pc_details(cpu, gpu, ram):
    """Повертає текст для опису пк"""
    all_info_togather = f'{cpu}, {gpu}, {ram}'
    return all_info_togather


while True:
    print("Enter details that you want in your pc: ")
    print("enter 'q' at any time to quit.")
    cpu_name = input("Enter cpu name: ")
    if cpu_name == 'q':
        break
    gpu_name = input("Enter gpu name: ")
    if gpu_name == 'q':
        break
    ram_name = input("Enter ram name: ")
    if ram_name == 'q':
        break

    full_pc_list = pc_details(cpu_name, gpu_name, ram_name)
    print(f"\nHere is your setup {full_pc_list}")