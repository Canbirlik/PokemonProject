import requests
import tkinter
import json

# window
window = tkinter.Tk()
window.title("Pokemon")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

response = requests.get("https://pokeapi.co/api/v2/pokemon/")
pokemon_list = []

for item in response.json()["results"]:
    pokemon_list.append(item["name"])

# title_label
title_label = tkinter.Label(text="Select your pokemon: ", font=('Arial', 10, 'normal'))
title_label.pack()

def listbox_selected(event):
    ability_list = []
    selected_pokemon = my_pokemonbox.get(my_pokemonbox.curselection())
    response2 = requests.get("https://pokeapi.co/api/v2/pokemon/" + selected_pokemon)
    for ability in (response2.json()["abilities"]):
        ability_list.append(ability["ability"]["name"])
    pokemon_text.replace("1.0", tkinter.END, ability_list)

# listbox
my_pokemonbox = tkinter.Listbox(selectmode=tkinter.SINGLE)
for i in range(len(pokemon_list)):
    my_pokemonbox.insert(i, pokemon_list[i])
my_pokemonbox.bind("<<ListboxSelect>>", listbox_selected)
my_pokemonbox.pack()


# info_label
info_label = tkinter.Label(text="Abilities of your pokemon: ", font=('Arial', 10, 'normal'))
info_label.pack()


# pokemon_text
pokemon_text = tkinter.Text(width=40, height=10)
pokemon_text.pack()

window.mainloop()
