from countryinfo import CountryInfo

print("\nWellcome to Country Finder 2023!")

is_running_main = True
while is_running_main:
    try:
        country_name = input("\nEnter a country or ISO code: ")
        country_data = CountryInfo(country_name)

        # print(country_data.info())
        print("\n* COUNTRY: ", country_data.info()['name'])

        is_running = True
        while is_running:
            try:
                option = int(input("""\n\tWhat do you want to know?: 
        ------------------
            1. Capital
            2. Provinces
            3. Currencies
            4. Region
            5. Sub-region
            6. Timezones
            7. ISO codes
            8. Wikipedia URL
            9. Search other country
            10. Exit

            Chose: """))

                if option == 1:
                    print("\n* Capital is:", country_data.capital())
                elif option == 2:
                    print("\n* Provinces are:")
                    for i, province in enumerate(country_data.provinces()):
                        print(f"\t{i+1}", province)
                elif option == 3:
                    print("\n* Currencies are:")
                    for currency in country_data.currencies():
                        print("\t", currency)
                elif option == 4:
                    print("\n* Region is:", country_data.region())
                elif option == 5:
                    print("\n* Subregion is:", country_data.subregion())
                elif option == 6:
                    print("\n* Timezones are:")
                    for timezone in country_data.timezones():
                        print("\t", timezone)
                elif option == 7:
                    print("\n* ISO codes are:")
                    for key, value in country_data.iso().items():
                        print("\t", value)
                elif option == 8:
                    print("\n* Wiki URL:", country_data.wiki())
                elif option == 9:
                    is_running = False
                elif option == 10:
                    is_running = False
                    is_running_main = False
                else:
                    print("That's not an option...")
            except:
                print("\nThat's a number, ha!...")
    except:
        print("That's not a valid option!...")

print("\nThanks for try me. Until next time!")
