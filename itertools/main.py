def main() -> None:
    countries = ("Germany", "France", "Italy", "Spain", "Portugal", "Greece")
    country_iter = iter(countries)

    while True:
        try:
            country = next(country_iter)
        except StopIteration:
            break
        else:
            print(country)

if __name__ == "__main__":
    main()