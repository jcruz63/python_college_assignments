first_names = ["John", "Jane", "Jimmy", "Jax"]
last_names = ["Doe", "Doe", "hendrix", "Lax"]
jobs = ["coder", "commando", "musician", "carpenter"]

dict_full_name = dict(zip(first_names, last_names))


if __name__ == '__main__':
    for (first, last, job) in zip(first_names, last_names, jobs):
        print(f'{first} {last} works as a {job}')

    for (index, name) in enumerate(first_names):
        print(f'The index of {name} is {index}')

    for (first, last) in dict_full_name.items():
        print(first, last)

