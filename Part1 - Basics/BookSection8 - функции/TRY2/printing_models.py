unprinted_designes = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []


# while unprinted_designes:
#     current_design = unprinted_designes.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)
#
# print('\nThe following models have been printed:')
# for completed_model in completed_models:
#     print(completed_model)

def print_models(unprinted_designes, completed_models):
    while unprinted_designes:
        current_design = unprinted_designes.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)


print_models(unprinted_designes[:], completed_models)
show_completed_models(completed_models)
